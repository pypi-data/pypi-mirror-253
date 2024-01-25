"""Aggregate analysis."""

from typing import Any
import matplotlib.colors as mcolors
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.figure import Figure

import doplaydo.dodata as dd


def plot_wafermap(
    result: dict[tuple[int, int], float],
    lower_spec: float,
    upper_spec: float,
    metric: str,
    device_attributes: dict[str, Any] | None = None,
) -> Figure:
    """Plot a wafermap of the result.

    Args:
        result: Dictionary of result.
        lower_spec: Lower specification limit.
        upper_spec: Upper specification limit.
        device_attributes: Settings to filter devices by.
        metric: Metric to analyze.
    """
    fontsize = 20

    # Calculate the bounds and center of the data
    die_xs, die_ys = zip(*result.keys())
    die_x_min, die_x_max = min(die_xs), max(die_xs)
    die_y_min, die_y_max = min(die_ys), max(die_ys)

    # Create the data array
    data = np.full((die_y_max - die_y_min + 1, die_x_max - die_x_min + 1), np.nan)
    for (i, j), v in result.items():
        data[j - die_y_min, i - die_x_min] = v

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6.8))

    # First subplot: Heatmap
    ax1.set_xlabel("Die X", fontsize=fontsize)
    ax1.set_ylabel("Die Y", fontsize=fontsize)
    title = f"{metric} {device_attributes}"
    ax1.set_title(title, fontsize=fontsize, pad=10)

    cmap = plt.get_cmap("viridis")
    vmin, vmax = (
        min(v for v in result.values() if not np.isnan(v)),
        max(result.values()),
    )

    heatmap = ax1.imshow(
        data,
        cmap=cmap,
        extent=[die_x_min - 0.5, die_x_max + 0.5, die_y_min - 0.5, die_y_max + 0.5],
        origin="lower",
        vmin=vmin,
        vmax=vmax,
    )

    ax1.set_xlim(die_x_min - 0.5, die_x_max + 0.5)
    ax1.set_ylim(die_y_min - 0.5, die_y_max + 0.5)

    for (i, j), v in result.items():
        if not np.isnan(v):
            ax1.text(
                i,
                j,
                f"{v:.2f}",
                ha="center",
                va="center",
                color="white",
                fontsize=fontsize,
            )

    plt.colorbar(heatmap, ax=ax1)

    # Second subplot: Binary map based on specifications
    binary_map = np.where(
        np.isnan(data),
        np.nan,
        np.where((data >= lower_spec) & (data <= upper_spec), 1, 0),
    )

    cmap_binary = mcolors.ListedColormap(["red", "green"])
    heatmap_binary = ax2.imshow(
        binary_map,
        cmap=cmap_binary,
        extent=[die_x_min - 0.5, die_x_max + 0.5, die_y_min - 0.5, die_y_max + 0.5],
        origin="lower",
        vmin=0,
        vmax=1,
    )

    ax2.set_xlim(die_x_min - 0.5, die_x_max + 0.5)
    ax2.set_ylim(die_y_min - 0.5, die_y_max + 0.5)

    for (i, j), v in result.items():
        if not np.isnan(v):
            ax2.text(
                i,
                j,
                f"{v:.2f}",
                ha="center",
                va="center",
                color="white",
                fontsize=fontsize,
            )

    ax2.set_xlabel("Die X", fontsize=fontsize)
    ax2.set_ylabel("Die Y", fontsize=fontsize)
    ax2.set_title('KGD "Pass/Fail"', fontsize=fontsize, pad=10)
    plt.colorbar(heatmap_binary, ax=ax2, ticks=[0, 1]).set_ticklabels(
        ["Outside Spec", "Within Spec"]
    )
    return fig


def run(
    wafer_id: int,
    lower_spec: float,
    upper_spec: float,
    function_name: str,
    metric: str,
    device_attributes: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Returns wafer map of metric after function_name.

    Args:
        wafer_id: ID of the wafer to analyze.
        lower_spec: Lower specification limit.
        upper_spec: Upper specification limit.
        function_name: Name of the die function to analyze.
        metric: Metric to analyze.
        device_attributes: Settings to filter devices by.
    """
    device_attributes = device_attributes or {}
    device_datas = dd.get_data_by_query(
        [dd.Wafer.id == wafer_id]
        + [
            dd.attribute_filter(dd.Cell, key, value)
            for key, value in device_attributes.items()
        ],
    )

    if not device_datas:
        raise ValueError(
            f"No device data found with wafer_id {wafer_id}, device_attributes {device_attributes}"
        )

    result = {}
    devices = [data[0] for data in device_datas]
    device_die_analysis = [
        (device.die, device.analysis) for device in devices if device.analysis
    ]

    for die, analysis in device_die_analysis:
        analysis_ids = [a.id for a in analysis]
        max_analysis_index = np.argmax(analysis_ids)
        last_analysis = analysis[max_analysis_index]
        o = last_analysis.output[metric]  # get the last analysis (most recent)
        if not isinstance(o, float | int):
            raise ValueError(f"Analysis output {o} is not a float or int")
        result[(die.x, die.y)] = o

    result_list = [value for value in result.values() if isinstance(value, int | float)]
    result_array = np.array(result_list)
    if np.any(np.isnan(result_array)) or not result:
        raise ValueError(
            f"No analysis for function_name={function_name!r} and device_name {device_name!r} found."
        )

    summary_plot = plot_wafermap(
        result=result,
        lower_spec=lower_spec,
        upper_spec=upper_spec,
        metric=metric,
        device_attributes=device_attributes,
    )

    return dict(
        output={"result": result_list},
        summary_plot=summary_plot,
        wafer_id=wafer_id,
    )


if __name__ == "__main__":
    # d = run(478, key="components", metric="component_loss", function_name="cutback")
    # print(d["output"]["result"])
    project_name = "rings-archie"
    device_data20, df = dd.get_data_by_query(
        [
            dd.Project.name == project_name,
            dd.attribute_filter(dd.Cell, "radius_um", 20),
            dd.attribute_filter(dd.Cell, "gap_um", 0.2),
        ],
        limit=1,
    )[0]
    device_name = device_data20.device.name
    dd.analysis.trigger_device_data(
        project_name=project_name,
        device_name=device_name,
        function_name="device_fsr",
        parameters=dict(height=-0.02),
    )
    d = run(
        14,
        device_attributes=dict(radius_um=20),
        metric="fsr_mean",
        function_name="device_fsr",
        lower_spec=0.1,
        upper_spec=0.2,
    )
