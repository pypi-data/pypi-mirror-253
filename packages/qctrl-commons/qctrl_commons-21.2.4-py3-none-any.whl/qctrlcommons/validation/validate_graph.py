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
Validator for core__calculateGraph mutation.
"""
from qctrlcommons.exceptions import QctrlFieldError
from qctrlcommons.validation.base import BaseMutationInputValidator
from qctrlcommons.validation.messages import Messages


class CalculateGraphValidator(BaseMutationInputValidator):
    """
    Validator for core__calculateGraph mutation.
    """

    def check_optimizable_variables(self, input_: dict):  # pylint:disable=no-self-use
        """
        Checks no optimizable variables are present in the graph input.

        Parameters
        ----------
        input_ : dict
            the GraphQL input.

        Raises
        ------
        QctrlFieldError
            validation check failed
        """

        graph_operations = input_["graph"]["operations"]
        for operation in graph_operations.values():
            if operation["optimizable_variable"]:
                raise QctrlFieldError(
                    message=f"The operation '{operation['operation_name']}' is not available to use"
                    + " as part of the calculate graph function.",
                    fields=["graph"],
                )

    def check_output_node_names(self, input_: dict):  # pylint:disable=no-self-use
        """
        Checks the following:
        1. At least 1 element in `outputNodeNames`
        2. All elements in `outputNodeNames` correspond to nodes in graph.

        Parameters
        ----------
        input_ : dict
            the GraphQL input.

        Raises
        ------
        QctrlFieldError
            validation check failed
        """
        output_node_names = input_["outputNodeNames"]
        graph_operations = input_["graph"]["operations"]

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
