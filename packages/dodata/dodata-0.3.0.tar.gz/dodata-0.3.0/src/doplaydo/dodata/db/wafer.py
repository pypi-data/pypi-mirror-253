"""This modules contains functions for querying the database for wafer objects."""
from doplaydo.dodata_core import models as m
from sqlmodel.sql.expression import SelectOfScalar
from sqlalchemy.sql import ColumnElement
from .. import session, select
from collections.abc import Sequence
from .die import _get_die_joined_query


def _get_wafer_joined_query() -> SelectOfScalar[m.Wafer]:
    return (
        select(m.Wafer)
        .join(m.Die)
        .join(m.Project, m.Wafer.project_id == m.Project.id)
        .join(m.Analysis, m.Analysis.wafer_id == m.Wafer.id, isouter=True)
        .join(
            m.AnalysisFunction,
            onclause=m.Analysis.analysis_function_id == m.AnalysisFunction.id,
            isouter=True,
        )
    )


def get_wafers_by_query(clauses: list[ColumnElement[bool] | bool]) -> Sequence[m.Wafer]:
    """Return a list of filtered wafers."""
    statement = _get_wafer_joined_query()

    for clause in clauses:
        statement = statement.where(clause)

    _wafers = session.exec(statement).all()

    return _wafers


def get_by_name(project_name: str, wafer_name: str) -> Sequence[m.Wafer]:
    """Get a wafer by project name and wafer name."""
    return get_wafers_by_query(
        [m.Project.name == project_name, m.Wafer.name == wafer_name]
    )


def get_by_id(wafer_id: int) -> m.Wafer:
    """Get a wafer by its unique id."""
    _wafers = get_wafers_by_query([m.Wafer.id == wafer_id])

    if not _wafers:
        raise ValueError(f"Could not find wafer with {wafer_id=}")

    return _wafers[0]


def get_wafer_dies(
    wafer_name: str, project_name: str, clauses: list[ColumnElement[bool] | bool]
) -> Sequence[m.Die]:
    """Return a list of filtered wafer dies."""
    statement = _get_die_joined_query()

    clauses.append(m.Project.name == project_name)
    clauses.append(m.Wafer.name == wafer_name)

    for clause in clauses:
        statement = statement.where(clause)

    _dies = session.exec(statement).all()

    return _dies
