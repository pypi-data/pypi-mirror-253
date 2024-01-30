# Copyright 2023 Q-CTRL. All rights reserved.
#
# Licensed under the Q-CTRL Terms of service (the "License"). Unauthorized
# copying or use of this file, via any medium, is strictly prohibited.
# Proprietary and confidential. You may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#    https://q-ctrl.com/terms
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS. See the
# License for the specific language.
"""
Utility functions.
"""

from collections import namedtuple
from enum import Enum
from typing import (
    Any,
    Dict,
    List,
    Optional,
    Union,
)

import numpy as np
from inflection import camelize

from qctrlcommons import serializers
from qctrlcommons.exceptions import QctrlFieldError
from qctrlcommons.validation.messages import Messages


# pylint: disable=invalid-name
def read_numpy_array(
    shape: List[int],
    sparseEntries: List[Dict[str, Any]] = None,
    denseEntries: Dict[str, List[Union[float, int]]] = None,
) -> np.ndarray:
    """
    Returns a NumPy array parsed from the given GraphQL data.

    Parameters
    ----------
    shape : List[int]
        The size of each dimension of the array.
    sparseEntries : List[Dict[str, Any]], optional
        The non-zero entries of the array. Each item of the list is a dict with entries
        "coordinates", which is a list of the coordinates of the entry, and "value", which is the
        complex value. Defaults to an empty list if omitted or None.
    denseEntries : Dict[str, List[Union[float, int]]], optional
        The dict containing the "real" and "imag" lists to rebuild the array.
        Defaults to an empty dict if omitted or None.

    Returns
    -------
    np.ndarray
        The array.
    """
    return serializers.read_numpy_array(
        shape, sparse_entries=sparseEntries, dense_entries=denseEntries
    )


def write_numpy_array(array: np.ndarray) -> Dict[str, Any]:
    """
    Writes a NumPy array to a GraphQL-compatible dictionary.

    Parameters
    ----------
    array : np.ndarray
        The NumPy array to write.

    Returns
    -------
    dict
        A GraphQL-compatible dictionary representing the given array. The entries are ordered in
        row-major order (i.e. with the last coordinate index varying fastest).
    """
    return {
        camelize(key, False): value
        for key, value in serializers.write_numpy_array(array).items()
    }


def check_sample_times(sample_times: List[float], duration: float) -> None:
    """
    Sample times must be in ascending order, and between 0 and duration.

    Parameters
    ----------
    sample_times : List[float]
        Times of samples.
    duration : float
        Total time of controls.

    Raises
    ------
    QctrlFieldError
        Validation check failed.
    """
    error_message = None
    sample_times = np.asarray(sample_times)

    if len(sample_times) == 0:
        error_message = Messages(
            field_name="sampleTimes", min_length=0
        ).items_greater_than
    elif not np.all(sample_times[:-1] <= sample_times[1:]):
        error_message = Messages(field_name="sampleTimes").in_ascending_order
    elif sample_times[0] < 0 or sample_times[-1] > duration:
        error_message = Messages(
            field_name="sampleTimes", minimum=0, maximum=duration
        ).value_between

    if error_message:
        raise QctrlFieldError(message=error_message, fields=["sampleTimes"])


def check_initial_state_vector(state: np.ndarray) -> None:
    """
    Initial state must be a normalized vector.

    Parameters
    ----------
    state : np.ndarray
        1D array representing a system state.

    Raises
    ------
    QctrlFieldError
        Validation check failed.
    """
    if not (len(state.shape) == 1 or (len(state.shape) == 2 and state.shape[1] == 1)):
        raise QctrlFieldError(
            message=f"Initial state vector must be a 1D array, got {state} instead.",
            fields=["initialStateVector"],
        )
    if not np.isclose(np.sum(np.abs(state) ** 2), 1):
        raise QctrlFieldError(
            message=f"Initial state vector must be normalized, got {state} instead.",
            fields=["initialStateVector"],
        )


def check_target(target: np.ndarray) -> None:
    """
    Target must be a partial isometry.

    Parameters
    ----------
    target : np.ndarray
        2D array representing a partial isometry.

    Raises
    ------
    QctrlFieldError
        Validation check failed.
    """
    if not (len(target.shape) == 2 and target.shape[0] == target.shape[1]):
        raise QctrlFieldError(
            message=f"Target must be a 2D array, got {target} instead.",
            fields=["target"],
        )
    if not np.allclose(np.linalg.multi_dot([target, target.T.conj(), target]), target):
        raise QctrlFieldError(
            message=f"Target must be a partial isometry, got {target} instead.",
            fields=["target"],
        )


def _is_hermitian(operator: np.ndarray) -> bool:
    return (
        len(operator.shape) == 2
        and operator.shape[0] == operator.shape[1]
        and np.allclose(operator, operator.T.conj())
    )


def _is_non_hermitian(operator: np.ndarray) -> bool:
    return (
        len(operator.shape) == 2
        and operator.shape[0] == operator.shape[1]
        and not np.allclose(operator, operator.T.conj())
    )


# Named tuple to describe the Hamiltonian term
# name : str, the name of the component, should be one of "Drive", 'Drift", and "Shift"
# type : str, operator type of the term
# validator: Callable, validate the operator type
Component = namedtuple("Component", ["name", "type", "validator"])


class HamiltonianTerm(Enum):
    """
    Terms of a given Hamiltonian.
    """

    DRIVE = Component("Drive", "non-Hermitian", _is_non_hermitian)
    DRIFT = Component("Drift", "Hermitian", _is_hermitian)
    SHIFT = Component("Shift", "Hermitian", _is_hermitian)


def check_drives_drifts_shifts(
    total_duration: float,
    drives: Optional[Dict[str, Any]] = None,
    drifts: Optional[Dict[str, Any]] = None,
    shifts: Optional[Dict[str, Any]] = None,
) -> None:
    """
    Check Hamiltonian terms:
        1. each segment duration must be non-negative
        2. sum of segment durations must be the same as the total duration
        3. operators must satisfy that
            - drive: must have non Hermitian operator
            - shift: must have Hermitian operator
            - drift: must have Hermitian operator

    Parameters
    ----------
    total_duration : float
        Total duration of controls.
    drives : dict, optional
        Drive terms. If exists, has two keys "control" and "operator".
    drifts : dict, optional
        Drift terms. If exists, has one key "operator".
    shifts : dict, optional
        Shift terms. If exists, has two keys "control" and "operator".

    Raises
    ------
    QctrlFieldError
        Validation check failed.
    """
    if drives is None and shifts is None and drifts is None:
        raise QctrlFieldError(
            message="Must have at least one drive, shift, or drift.",
            fields=["drives", "shifts", "drifts"],
        )

    if drives is not None:
        _check_control_terms(drives, HamiltonianTerm.DRIVE, total_duration)

    if drifts is not None:
        _check_control_terms(drifts, HamiltonianTerm.DRIFT, total_duration)

    if shifts is not None:
        _check_control_terms(shifts, HamiltonianTerm.SHIFT, total_duration)


def _check_control_terms(
    terms: List[Dict[str, Any]], component: HamiltonianTerm, total_duration: float
) -> None:
    for term in terms:
        # check operator type
        if not component.value.validator(read_numpy_array(**term["operator"])):
            raise QctrlFieldError(
                message=f"{component.value.name} must be {component.value.type}, "
                f"got {read_numpy_array(**term['operator'])} instead.",
                fields=["operator"],
            )
        # check segment if any
        if component in [HamiltonianTerm.DRIVE, HamiltonianTerm.SHIFT]:
            control_durations = np.asarray(
                [item["duration"] for item in term["control"]]
            )
            if not np.all(control_durations >= 0):
                raise QctrlFieldError(
                    message=f"{component.value.name} segment duration must "
                    "be non-negative.",
                    fields=["control", "duration"],
                )
            if not np.isclose(sum(control_durations), total_duration):
                raise QctrlFieldError(
                    message=f"{component.value.name} total duration must match the "
                    "duration you set.",
                    fields=["duration", "control"],
                )


def validate_cost_in_optimization_graph(input_data: Dict[str, Any]):
    """
    Check whether the serialized input data has proper cost node.

    Parameters
    ----------
    input_data : Dict[str, Any]
        The GQL input data.

    Raises
    ------
    QctrlFieldError
        Validation check failed.
    """
    if input_data["costNodeName"] not in input_data["graph"]["operations"]:
        raise QctrlFieldError(
            message="A cost node must be present in the graph.",
            fields=["costNodeName", "graph"],
        )


def validate_output_node_in_optimization_graph(input_data: Dict[str, Any]):
    """
    Check whether the serialized input data has proper output nodes:
        - At least one element in `outputNodeNames`.
        - All elements in `outputNodeNames` correspond to nodes in graph.

    Parameters
    ----------
    input_data : Dict[str, Any]
        The GQL input data.

    Raises
    ------
    QctrlFieldError
        Validation check failed.
    """

    output_node_names = input_data["outputNodeNames"]
    graph_operations = input_data["graph"]["operations"]

    if len(output_node_names) < 1:
        raise QctrlFieldError(
            message=Messages(
                field_name="outputNodeNames", minimum=1, items="node name"
            ).min_items,
            fields=["outputNodeNames"],
        )
    for node_name in output_node_names:
        if node_name not in graph_operations:
            raise QctrlFieldError(
                message=f"The requested output node name '{node_name}' is not"
                + " present in the graph.",
                fields=["outputNodeNames"],
            )


def validate_optimization_variables(input_data: Dict[str, Any]):
    """
    Check that optimizable variables are present in the input graph.

    Parameters
    ----------
    input_data : Dict[str, Any]
        The GraphQL input data.

    Raises
    ------
    QctrlFieldError
        Validation check failed.
    """
    graph_operations = input_data["graph"]["operations"]

    for operation in graph_operations.values():
        if operation["optimizable_variable"]:
            return

    raise QctrlFieldError(
        message="At least one optimization variable is required in the"
        " optimization graph.",
        fields=["graph"],
    )


def validate_initial_value_for_optimization_variables(input_data: Dict[str, Any]):
    """
    Check optimization variable has valid non-default initial values.

    Parameters
    ----------
    input_data : Dict[str, Any]
        The GraphQL input data.

    Raises
    ------
    QctrlFieldError
        Validation check failed.
    """

    initial_values = []
    graph_operations = input_data["graph"]["operations"]

    for operation in graph_operations.values():
        if (
            operation["optimizable_variable"]
            and operation["kwargs"].get("initial_values") is not None
        ):
            initial_values.append(operation["kwargs"]["initial_values"])

    if len(initial_values) != 0:
        for val in initial_values[1:]:
            if not isinstance(val, type(initial_values[0])):
                raise QctrlFieldError(
                    message="Non-default initial values of optimization variables in the graph"
                    " must all either be an array or a list of arrays.",
                    fields=["Graph"],
                )

        if isinstance(initial_values[0], list):
            for val in initial_values[1:]:
                if len(val) != len(initial_values[0]):
                    raise QctrlFieldError(
                        message="Lists of initial values of optimization variables must have "
                        "the same length.",
                        fields=["Graph"],
                    )
