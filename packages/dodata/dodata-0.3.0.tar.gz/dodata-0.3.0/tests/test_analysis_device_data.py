import pathlib
import requests
import pytest
from sqlalchemy.sql import ColumnElement
from sqlmodel.sql.expression import SelectOfScalar
from sqlmodel import select
from doplaydo.dodata_core.models import Cell, Project, DeviceData, Device, Die, Wafer
import doplaydo.dodata as dd
from tqdm.auto import tqdm

module_path = pathlib.Path(__file__).parent.absolute()
repo_path = module_path.parent
notebooks_path = repo_path / "notebooks"
wafer_name = "6d4c615ff105"
spirals_data = notebooks_path / "spirals" / wafer_name

if __name__ == "__main__":
    spectrum_measurement_type = dd.api.device_data.PlottingKwargs(
        x_name="wavelength",
        y_name="output_power",
        x_col="wavelength",
        y_col=["output_power"],  # can also be a string for a single value
        # y_col="output_power",
    )

    MEASUREMENTS_PATH = spirals_data
    PROJECT_NAME = "spirals"
    data_files = list(MEASUREMENTS_PATH.glob("**/data.json"))
    project_names = []
    device_names = []
    die_xs = []
    die_ys = []
    wafer_names = []
    plotting_kwargs = []
    data_types = []
    die_names = []

    for path in data_files:
        device_name = path.parts[-2]
        die_name = path.parts[-3]
        die_x, die_y = die_name.split("_")
        wafer_name = path.parts[-4]

        device_names.append(device_name)
        die_names.append(die_name)
        die_xs.append(die_x)
        die_ys.append(die_y)
        wafer_names.append(wafer_name)
        plotting_kwargs.append(spectrum_measurement_type)
        project_names.append(PROJECT_NAME)
        data_types.append("measurement")

    die_set = set(die_names)
    wafer_set = set(wafer_names)
    database_dies = []
    widths_um = [0.3, 0.5, 0.8]

    for wafer in wafer_set:
        for die_name in tqdm(die_set):
            die_x, die_y = die_name.split("_")
            for width_um in widths_um:
                r = dd.analysis.trigger_die(
                    project_name=PROJECT_NAME,
                    wafer_name=wafer,
                    die_x=die_x,
                    die_y=die_y,
                    function_name="loss_cutback",
                    parameters={"width_um": width_um},
                )
                if r.status_code != 200:
                    raise requests.HTTPError(r.text)
