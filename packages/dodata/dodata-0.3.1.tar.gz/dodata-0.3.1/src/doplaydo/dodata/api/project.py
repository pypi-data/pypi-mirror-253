# ruff: noqa: D415, UP007, D103
"""DoData functions for projects."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

import klayout.db as kdb
import requests
from pydantic import BaseModel

from .common import url as base_url, get, post, delete as _delete


class Extraction(BaseModel):
    """Cell & Device Extraction Definition."""

    cell_name: str
    min_hierarchy_lvl: int = 0
    max_hierarchy_lvl: Optional[int] = 1
    cell_white_list: list[str] = []
    cell_black_list: list[str] = []


def create(
    eda_file: str | Path,
    project_name: Optional[str] = None,
    lyp_file: Optional[str] = None,
    description: Optional[str] = None,
    cell_extractions: list[Extraction] = [],
) -> requests.Response:
    """Upload a new project to DoData.

    Args:
        eda_file: An EDA (layout) file to upload (accepted types: .gds, .gds.gz, .oas)
        project_name: project name
        cell_extractions: A stringified JSON for defining cell and device extraction,
            see below for more explanation
        lyp_file: Layout properties file used for displaying the eda_file in the
            renderer
        description: Additional description for the project

    Example:
        dd.api.project.create(
            project_name="TEST",
            eda_file="~/Downloads/dodata.gds",
            cell_extractions=[
                dd.api.project.Extraction(
                    cell_name="TOP_CELL_A",
                    cell_white_list=[
                        "Straight_W1000_L10000_L0_ENone"
                    ]
                )
            ]
        )
    """
    if project_name is None:
        ly = kdb.Layout()
        ly.read(str(eda_file))
        assert len(ly.top_cells()) > 0, (
            "Cannot automatically determine project_name from edafile."
            " Please specify project_name or pass a non-empty edafile."
        )
        project_name = ly.top_cells()[0].name

    url = f"{base_url}/project"
    params = {"name": project_name}
    data: dict[str, str] = {
        "extraction": json.dumps([ce.model_dump() for ce in cell_extractions])
        .removeprefix("[")
        .removesuffix("]")
    }
    if description:
        params["description"] = description
    fp = Path(eda_file).expanduser().resolve()
    assert (
        fp.exists() and fp.is_file()
    ), f"{fp.resolve()} doesn't exists or is not a file"
    with open(fp, "rb") as f:
        if lyp_file:
            lp = Path(lyp_file)
            if lp.is_file():
                with open(lp, "rb") as lf:
                    return post(
                        url,
                        params=params,
                        files={"eda_file": f, "lyp_file": lf},
                        data=data,
                    )
            else:
                print(
                    f"[yellow]Warning:[/yellow] lyp file {str(lp.resolve())}"
                    " is not defined or not a file. Skipping lyp"
                )
        return post(url, params=params, files={"eda_file": f}, data=data)


def delete(
    project_name: str,
) -> requests.Response:
    """Delete a project from DoData."""
    url = f"{base_url}/project/{project_name}"
    return _delete(url)


def download_edafile(
    project_name: str,
    filepath: str | Path | None = None,
) -> Path:
    """Download the eda file for a project.

    Args:
        project_name: Name of the project.
        filepath: Path to the eda file to download.
    """
    url = f"{base_url}/project/{project_name}"
    r = get(url)
    r.raise_for_status()

    filepath = Path(filepath) if filepath else Path()

    if filepath.is_dir():
        filepath = filepath / r.headers["content-disposition"].split("; filename=")[1]

    elif not filepath.parent.is_dir():
        raise ValueError(f"Directory {filepath.parent} does not exist")

    with filepath.open("wb") as f:
        f.write(r.content)
    return filepath


def download_lyp(
    project_name: str,
    filepath: str | Path | None = None,
) -> Path:
    """Download the Klayout Layer Properties lyp file for a project.

    Args:
        project_name: Name of the project.
        filepath: Path to the lyp file to download.
    """
    url = f"{base_url}/project/{project_name}/lyp_file"
    r = get(url)
    r.raise_for_status()

    filepath = Path(filepath) if filepath else Path()

    if filepath.is_dir():
        filepath = filepath / r.headers["content-disposition"].split("; filename=")[1]

    elif not filepath.parent.is_dir():
        raise ValueError(f"Directory {filepath.parent} does not exist")

    with filepath.open("wb") as f:
        f.write(r.content)

    return filepath


def download_design_manifest(
    project_name: str,
    filepath: str | Path | None = None,
) -> Path:
    """Download the design manifest CSV file for a project.

    Args:
        project_name: Name of the project.
        filepath: Path to the file to download.
    """
    url = f"{base_url}/project/{project_name}/design_manifest"
    r = get(url)
    r.raise_for_status()

    filepath = Path(filepath) if filepath else Path()

    if filepath.is_dir():
        filepath = filepath / r.headers["content-disposition"].split("; filename=")[1]

    elif not filepath.parent.is_dir():
        raise ValueError(f"Directory {filepath.parent} does not exist")

    with filepath.open("wb") as f:
        f.write(r.content)
    return filepath


# def download_wafer_definitions(project_name: str, filepath: str | Path) -> Path:
#     """Download the wafer definitions JSON file for a project.

#     Args:
#         project_name: Name of the project.
#         filepath: Path to the file to download.
#     """
#     url = f"{base_url}/wafers/{project_name}"
#     r = get(url)
#     r.raise_for_status()

#     filepath = Path(filepath) if filepath else Path()

#     if not filepath.parent.is_dir():
#         raise ValueError(f"Directory {filepath.parent} does not exist")

#     with filepath.open("wb") as f:
#         f.write(r.content)
#     return filepath


def upload_design_manifest(
    project_name: str,
    filepath: str | Path,
) -> requests.Response:
    """Upload device manifest file for a project.

    Args:
        project_name: Name of the project.
        filepath: Path to the manifest CSV file to upload.
    """
    url = f"{base_url}/project/{project_name}/design_manifest"
    params = {"project_name": project_name}
    files = {"csv_file": open(filepath, "rb")}
    return post(url, params=params, files=files)


def upload_wafer_definitions(
    project_name: str,
    filepath: str | Path,
) -> requests.Response:
    """Upload device manifest file for a project.

    Args:
        project_name: Name of the project.
        filepath: Path to the wafer definitions JSON file.
    """
    url = f"{base_url}/wafers/{project_name}"
    params = {"project_name": project_name}
    files = {"wafer_definitions": open(filepath, "rb")}
    return post(url, params=params, files=files)
