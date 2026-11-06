"""Operaton / Camunda 7 engine REST: the Task Local Variable operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase, upload_part


class Camunda7TaskLocalVariable(ApiClientBase):
    """Task Local Variable: 7 engine REST operation(s)."""

    def delete_task_local_variable(
        self,
        id: str,
        var_name: str,
    ) -> Any:
        """Delete Local Task Variable.

        Removes a local variable from a task by id.

        DELETE /task/{id}/localVariables/{varName}
        """
        return self._call(
            "DELETE",
            "/task/{id}/localVariables/{varName}",
            path={"id": id, "varName": var_name},
        )

    def get_task_local_variable(
        self,
        id: str,
        var_name: str,
        *,
        deserialize_value: bool | None = None,
    ) -> Any:
        """Get Local Task Variable.

        Retrieves a variable from the context of a given task by id.

        GET /task/{id}/localVariables/{varName}
        """
        return self._call(
            "GET",
            "/task/{id}/localVariables/{varName}",
            path={"id": id, "varName": var_name},
            params={
                "deserializeValue": deserialize_value,
            },
        )

    def get_task_local_variable_binary(
        self,
        id: str,
        var_name: str,
    ) -> Any:
        """Get Local Task Variable (Binary).

        Retrieves a binary variable from the context of a given task by id.
        Applicable for byte array and file variables.

        GET /task/{id}/localVariables/{varName}/data
        """
        return self._call(
            "GET",
            "/task/{id}/localVariables/{varName}/data",
            path={"id": id, "varName": var_name},
        )

    def get_task_local_variables(
        self,
        id: str,
        *,
        deserialize_values: bool | None = None,
    ) -> Any:
        """Get Local Task Variables.

        Retrieves all variables of a given task by id.

        GET /task/{id}/localVariables
        """
        return self._call(
            "GET",
            "/task/{id}/localVariables",
            path={"id": id},
            params={
                "deserializeValues": deserialize_values,
            },
        )

    def modify_task_local_variables(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Update/Delete Local Task Variables.

        Updates or deletes the variables in the context of a task. Updates precede
        deletions. So, if a variable is updated AND deleted, the deletion overrides
        the update. Request body: an object with modifications, deletions.

        POST /task/{id}/localVariables
        """
        return self._call(
            "POST",
            "/task/{id}/localVariables",
            path={"id": id},
            body=body,
        )

    def put_task_local_variable(
        self,
        id: str,
        var_name: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Update Local Task Variable.

        Sets a variable in the context of a given task. Request body: an object with
        value, type, valueInfo.

        PUT /task/{id}/localVariables/{varName}
        """
        return self._call(
            "PUT",
            "/task/{id}/localVariables/{varName}",
            path={"id": id, "varName": var_name},
            body=body,
        )

    def set_binary_task_local_variable(
        self,
        id: str,
        var_name: str,
        *,
        data: str | None = None,
        value_type: str | None = None,
        filename: str | None = None,
    ) -> Any:
        """Update Local Task Variable (Binary).

        Sets the serialized value for a binary variable or the binary value for a
        file variable.

        POST /task/{id}/localVariables/{varName}/data
        """
        return self._call(
            "POST",
            "/task/{id}/localVariables/{varName}/data",
            path={"id": id, "varName": var_name},
            form={
                "valueType": value_type,
            },
            files=upload_part("data", data, filename),
        )
