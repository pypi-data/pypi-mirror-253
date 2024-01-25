# ruff: noqa: D415, UP007, D103
"""DoData functions for projects."""
from __future__ import annotations

import requests

from .common import url as base_url, post


def create(
    project_name: str,
    cell_name: str,
    attributes: dict[str, int | float | str] | None = None,
) -> requests.Response:
    """Create a new cell for an existing project in DoData.

    Args:
        project_name: Name of the project to create the cell in.
        cell_name: Name of the cell.
        attributes: Additional information about the cell.
            Must be a one-dimensional dictionary with int/float/str values.

    Example:
        dd.api.cell.create(
            project_name="TEST",
            cell_name="test_cell"
        )
    """
    url = f"{base_url}/cell"
    params = {"project_name": project_name, "cell_name": cell_name}
    return post(url, params=params, data={"attributes": attributes or {}})
