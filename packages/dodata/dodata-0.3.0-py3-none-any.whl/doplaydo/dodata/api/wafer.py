# ruff: noqa: D101, D103, D107
"""DoData functions for wafers."""
from __future__ import annotations


import requests

from .common import url as base_url, get as _get, post

from typing_extensions import TypedDict
from pydantic import BaseModel
from collections.abc import Iterable
import json


class Wafer(TypedDict):
    project_id: int
    wafer_id: int
    x: int
    y: int


class DieDefinition(TypedDict):
    x: int
    y: int


class WaferDefinition(BaseModel):
    wafer: str
    dies: list[DieDefinition]

    def __init__(self, wafer_name: str, dies: Iterable[tuple[int, int]] | None = None):
        if dies is None:
            _dies = []
        else:
            _dies = [DieDefinition(x=x, y=y) for x, y in dies]
        super().__init__(wafer=wafer_name, dies=_dies)


def create(
    project_name: str,
    wafer_name: str,
    description: str | None = None,
    lot_name: str | None = None,
) -> requests.Response:
    """Upload a new die to DoData.

    Args:
        project_name: The name of the project which owns the die.
        wafer_name: The name of the wafer which owns the die.
        description: Additional info for the wafer in text form.
        x: x-coordinate of the die.
        y: y-coordinate of the die.
        lot_name: The name of the lot the wafer is part of.
        attributes: Additional information about the die.
    """
    url = f"{base_url}/wafer"
    params = {
        "project_name": project_name,
        "wafer_name": wafer_name,
        "description": description,
        "lot_name": lot_name,
    }
    response = post(url, params=params)

    if response.status_code != 200:
        raise requests.HTTPError(response.text, response=response)

    return response


def get(
    project_name: str,
    wafer_name: str,
) -> Wafer:
    wafer_response = _get(f"{base_url}/wafer/{project_name}/{wafer_name}")
    if wafer_response.status_code != 200:
        raise requests.HTTPError(wafer_response.text, response=wafer_response)
    return wafer_response.json()  # type: ignore[no-any-return]


def upload_wafer_definitions(
    project_name: str, wafer_definitions: list[WaferDefinition]
) -> requests.Response:
    """POST wafer definitions to DoData.

    Args:
        project_name: Name of the project in which to create the wafers and dies.
        wafer_definitions: A list of the wafer and dies as the pydantic model.

    Examples:
        uplodad_wafer_definitions(
            project_name="example_project",
            wafer_definitons=[
                WaferDefinition(wafer_name="wafer1")
            ]
        )

        uplodad_wafer_definitions(
            project_name="example_project",
            wafer_definitons=[
                WaferDefinition(wafer_name="wafer1",dies=[(0,0),(1,0),(2,0)])
            ]
        )
    """
    jsonb = json.dumps([wd.model_dump() for wd in wafer_definitions]).encode()
    return post(
        f"{base_url}/wafers/{project_name}",
        files={"wafer_definitions": ("data.json", jsonb)},
    )
