"""Common API calls to device_data namespace."""
from __future__ import annotations
import json
from tqdm.auto import tqdm

import requests

from concurrent.futures import ThreadPoolExecutor, Future, as_completed
from io import BytesIO
from PIL import Image
from .common import url as base_url, post, get
from .. import settings
from ..db.analysis import (
    get_analyses_for_die,
    get_analyses_for_wafer,
    get_analyses_for_device_data,
)
from doplaydo.dodata_core.models import Analysis
from collections.abc import Sequence
from typing import Literal


def trigger_by_id(
    function_name: str,
    target_model_id: int,
    target_model_name: str = "die",
    parameters: dict | None = None,
) -> requests.Response:
    """Trigger analysis.

    Args:
        function_name: Name of the function to trigger.
        target_model_id: ID of the target model to upload to.
        target_model_name: 'device', 'die' or 'wafer'.
        parameters: for triggering analysis.
    """
    url = f"{base_url}/analysis/"
    parameters = parameters or {}
    params = {
        "function_name": function_name,
        "target_model_id": target_model_id,
        "target_model": target_model_name,
    }
    json_parameters = json.dumps(parameters)

    r = post(url, params=params, json=json_parameters)
    if r.status_code != 200:
        raise requests.HTTPError(r.text)
    return r


def trigger_device_data(
    project_name: str,
    device_name: str,
    function_name: str,
    parameters: dict | None = None,
) -> list[Analysis]:
    """Trigger device data analysis.

    Args:
        project_name: Name of the project to upload to.
        device_name: Name of the device to upload to.
        function_name: Name of the function to trigger.
        parameters: for triggering analysis.
    """
    url = f"{base_url}/device_data/{project_name}/{device_name}/model_data"
    response = get(url)

    if response.status_code != 200:
        raise requests.HTTPError(response.text)

    device_data_count = len(response.json())
    device_data_ids = [device_data["id"] for device_data in response.json()]

    if device_data_count == 0:
        raise ValueError(f"No device data found for {project_name}/{device_name}")

    analyses = []

    for device_data_id in device_data_ids:
        r = trigger_by_id(
            function_name=function_name,
            target_model_id=device_data_id,
            target_model_name="device_data",
            parameters=parameters,
        )
        if r.status_code != 200:
            raise requests.HTTPError(r.text)

        analyses.append(Analysis(**r.json()))
    return analyses


def trigger_device_data_multi(
    device_data_ids: list[int],
    function_name: str,
    parameters: list[dict[str, int | list | dict] | None] | None = None,
    progress_bar: bool = False,
    n_threads: int = settings.n_threads,
) -> list[Analysis]:
    """Trigger multiple device analysis in parallel.

    The triggering is handled with a ThreadPoolExecutor.

    Args:
        device_data_ids: List of unique device ids to trigger.
        function_name: Name of the function to trigger.
        parameters: List of parameters for triggering analysis.
        progress_bar: Whether to display a progress bar.
        n_threads: Number of threads to use for the upload.

    Raises:
        IndexError: All the lists in the args/kwargs must have the same length.
    """
    parameters = parameters or []

    with ThreadPoolExecutor(max_workers=n_threads) as e:
        futures: list[Future[requests.Response]] = []
        for did, params in zip(device_data_ids, parameters):
            futures.append(
                e.submit(
                    trigger_by_id,
                    target_model_id=did,
                    target_model_name="device_data",
                    function_name=function_name,
                    parameters=params,
                )
            )
        analysis_list: list[Analysis] = []
        if progress_bar:
            for future in tqdm(as_completed(futures), total=len(futures)):
                response = future.result()

                if response.status_code != 200:
                    e.shutdown(wait=False, cancel_futures=True)
                    raise requests.HTTPError(response.text)
                analysis_list.append(Analysis(**response.json()))

        else:
            for future in as_completed(futures):
                response = future.result()

                if response.status_code != 200:
                    e.shutdown(wait=False, cancel_futures=True)
                    raise requests.HTTPError(response.text)
                analysis_list.append(Analysis(**response.json()))
        return analysis_list


def trigger_device_data_multi_by_ids(
    device_data_ids: list[int],
    function_name: str,
    parameters: list[dict[str, int | list | dict] | None] | None = None,
    progress_bar: bool = False,
    n_threads: int = settings.n_threads,
) -> list[Analysis]:
    """Trigger multiple device analysis in parallel.

    The triggering is handled with a ThreadPoolExecutor.

    Args:
        device_data_ids: List of unique device ids to trigger.
        function_name: Name of the function to trigger.
        parameters: List of parameters for triggering analysis.
        progress_bar: Whether to display a progress bar.
        n_threads: Number of threads to use for the upload.

    Raises:
        IndexError: All the lists in the args/kwargs must have the same length.
    """
    parameters = parameters or []

    with ThreadPoolExecutor(max_workers=n_threads) as e:
        futures: list[Future[requests.Response]] = []
        for did, params in zip(device_data_ids, parameters):
            futures.append(
                e.submit(
                    trigger_by_id,
                    target_model_id=did,
                    target_model_name="device_data",
                    function_name=function_name,
                    parameters=params,
                )
            )
        analysis_list: list[Analysis] = []
        if progress_bar:
            for future in tqdm(as_completed(futures), total=len(futures)):
                response = future.result()

                if response.status_code != 200:
                    e.shutdown(wait=False, cancel_futures=True)
                    raise requests.HTTPError(response.text)
                analysis_list.append(Analysis(**response.json()))

        else:
            for future in as_completed(futures):
                response = future.result()

                if response.status_code != 200:
                    e.shutdown(wait=False, cancel_futures=True)
                    raise requests.HTTPError(response.text)
                analysis_list.append(Analysis(**response.json()))
        return analysis_list


def trigger_die(
    project_name: str,
    function_name: str,
    wafer_name: str,
    die_x: int,
    die_y: int,
    parameters: dict | None = None,
) -> requests.Response:
    """Trigger die analysis.

    Args:
        project_name: Name of the project to upload to.
        function_name: Name of the function to trigger.
        wafer_name: name of the wafer to upload to.
        die_x: X coordinate of the die to upload to.
        die_y: Y coordinate of the die to upload to.
        parameters: for triggering analysis.
    """
    url = f"{base_url}/die/{project_name}/{wafer_name}/{die_x}/{die_y}/"
    response = get(url)
    if response.status_code != 200:
        raise requests.HTTPError(response.text)

    target_model_id = response.json()["id"]
    parameters = parameters or {}

    params = {
        "project_name": project_name,
        "function_name": function_name,
        "target_model": "die",
        "target_model_id": target_model_id,
    }

    url = f"{base_url}/analysis/"
    json_parameters = json.dumps(parameters)
    return post(url, params=params, json=json_parameters)


def trigger_die_multi(
    project_name: str,
    function_name: str,
    wafer_names: list[str],
    die_xs: list[int],
    die_ys: list[int],
    parameters: list[dict[str, int | list | dict] | None] | None = None,
    progress_bar: bool = False,
    n_threads: int = settings.n_threads,
) -> None:
    """Trigger multiple die analysis in parallel.

    The triggering is handled with a ThreadPoolExecutor.

    Args:
        project_name: project name to trigger analysis to.
        function_name: Name of the function to trigger.
        wafer_names: List of wafer names to upload to.
        die_xs: List of X coordinates of the dies to upload to.
        die_ys: List of Y coordinates of the dies to upload to.
        parameters: List of parameters for triggering analysis.
        progress_bar: Whether to display a progress bar.
        n_threads: Number of threads to use for the upload.

    Raises:
        IndexError: All the lists in the args/kwargs must have the same length.
    """
    parameters = parameters or []

    dies = set(zip(die_xs, die_ys))

    with ThreadPoolExecutor(max_workers=n_threads) as e:
        futures: list[Future[requests.Response]] = []
        for wafer in wafer_names:
            for die_x, die_y in dies:
                for params in parameters:
                    futures.append(
                        e.submit(
                            trigger_die,
                            project_name=project_name,
                            wafer_name=wafer,
                            die_x=die_x,
                            die_y=die_y,
                            function_name=function_name,
                            parameters=params,
                        )
                    )
        if progress_bar:
            for future in tqdm(as_completed(futures), total=len(futures)):
                response = future.result()

                if response.status_code != 200:
                    e.shutdown(wait=False, cancel_futures=True)
                    raise requests.HTTPError(response.text)
        else:
            for future in as_completed(futures):
                response = future.result()

                if response.status_code != 200:
                    e.shutdown(wait=False, cancel_futures=True)
                    raise requests.HTTPError(response.text)


def trigger_wafer(
    project_name: str,
    function_name: str,
    wafer_name: str,
    parameters: dict | None = None,
) -> requests.Response:
    """Trigger wafer analysis.

    Args:
        project_name: Name of the project to upload to.
        function_name: Name of the function to trigger.
        wafer_name: name of the wafer to upload to.
        parameters: for triggering analysis.
    """
    url = f"{base_url}/wafer/{project_name}/{wafer_name}"
    response = get(url)
    if response.status_code != 200:
        raise requests.HTTPError(response.text)

    target_model_id = response.json()["id"]
    parameters = parameters or {}

    params = {
        "project_name": project_name,
        "function_name": function_name,
        "target_model": "wafer",
        "target_model_id": target_model_id,
    }

    url = f"{base_url}/analysis/"
    json_parameters = json.dumps(parameters)
    return post(url, params=params, json=json_parameters)


def get_wafer_analysis_plots(
    project_name: str,
    wafer_name: str,
    target_model: Literal["device_data", "die", "wafer"],
) -> Sequence[Image.Image]:
    """Get plots for a wafer.

    Args:
        project_name: Name of the project to upload to.
        wafer_name: Name of the wafer to upload to.
        target_model: Whether to get device_data analyses or die analyses.
    """
    analyses = get_analyses_for_wafer(
        project_name=project_name, wafer_name=wafer_name, target_model=target_model
    )

    if not analyses:
        raise LookupError("Could not find analyses for die.")

    return _get_analysis_plots(analyses)


def get_die_analysis_plots(
    project_name: str, wafer_name: str, die_x: int, die_y: int
) -> list[Image.Image]:
    """Get plots for a die.

    Args:
        project_name: Name of the project to upload to.
        wafer_name: name of the wafer to upload to.
        die_x: X coordinate of the die to upload to.
        die_y: Y coordinate of the die to upload to.
    """
    analyses = get_analyses_for_die(
        project_name, wafer_name, die_x, die_y, target_model="die"
    )

    if not analyses:
        raise LookupError("Could not find analyses for die.")

    return _get_analysis_plots(analyses)


def get_device_data_analysis_plots(
    project_name: str,
    device_name: str,
    wafer_name: str | None = None,
    die_x: int | None = None,
    die_y: int | None = None,
) -> Sequence[Image.Image]:
    """Get plots for a device data.

    Args:
        project_name: Name of the project to upload to.
        device_name: Name of the device to upload to.
        wafer_name: name of the wafer to upload to.
        die_x: X coordinate of the die to upload to.
        die_y: Y coordinate of the die to upload to.

    """
    analyses = get_analyses_for_device_data(
        project_name=project_name,
        device_name=device_name,
        wafer_name=wafer_name,
        die_x=die_x,
        die_y=die_y,
    )
    if not analyses:
        raise LookupError("Could not find analyses for device data.")

    return _get_analysis_plots(analyses)


def _fetch_plot(analysis: Analysis) -> Image.Image:
    """Fetch plot for a given analysis."""
    url = f"{base_url}/analysis/{analysis.id}/summary_plot"
    response = get(url)
    response.raise_for_status()
    if response.status_code != 200:
        raise requests.HTTPError(response.text)
    return Image.open(BytesIO(response.content)).convert("RGB")


def _get_analysis_plots(
    analyses: Sequence[Analysis],
    n_threads: int = settings.n_threads,
) -> list[Image.Image]:
    """Get plots for a list of analyses."""
    plots: list[Image.Image] = []

    with ThreadPoolExecutor(max_workers=n_threads) as executor:
        future_plots = list(executor.map(_fetch_plot, analyses))

    plots.extend(future_plots)
    return plots
