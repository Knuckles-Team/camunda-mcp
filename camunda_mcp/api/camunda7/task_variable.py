"""Operaton / Camunda 7 engine REST: the Task Variable operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase, upload_part


class Camunda7TaskVariable(ApiClientBase):
    """Task Variable: 7 engine REST operation(s)."""

    def delete_task_variable(
        self,
        id: str,
        var_name: str,
    ) -> Any:
        """Delete Task Variable.

        Removes a variable that is visible to a task. A variable is visible to a
        task if it is a local task variable or declared in a parent scope of the
        task. See documentation on visibility of variables.

        DELETE /task/{id}/variables/{varName}
        """
        return self._call(
            "DELETE",
            "/task/{id}/variables/{varName}",
            path={"id": id, "varName": var_name},
        )

    def get_task_variable(
        self,
        id: str,
        var_name: str,
        *,
        deserialize_value: bool | None = None,
    ) -> Any:
        """Get Task Variable.

        Retrieves a variable from the context of a given task. The variable must be
        visible from the task. It is visible from the task if it is a local task
        variable or declared in a parent scope of the task. See documentation on
        visibility of variables.

        GET /task/{id}/variables/{varName}
        """
        return self._call(
            "GET",
            "/task/{id}/variables/{varName}",
            path={"id": id, "varName": var_name},
            params={
                "deserializeValue": deserialize_value,
            },
        )

    def get_task_variable_binary(
        self,
        id: str,
        var_name: str,
    ) -> Any:
        """Get Task Variable (Binary).

        Retrieves a binary variable from the context of a given task. Applicable for
        byte array and file variables. The variable must be visible from the task.
        It is visible from the task if it is a local task variable or declared in a
        parent scope of the task. See documentation on visibility of variables.

        GET /task/{id}/variables/{varName}/data
        """
        return self._call(
            "GET",
            "/task/{id}/variables/{varName}/data",
            path={"id": id, "varName": var_name},
        )

    def get_task_variables(
        self,
        id: str,
        *,
        deserialize_values: bool | None = None,
    ) -> Any:
        """Get Task Variables.

        Retrieves all variables visible from the task. A variable is visible from
        the task if it is a local task variable or declared in a parent scope of the
        task. See documentation on visibility of variables.

        GET /task/{id}/variables
        """
        return self._call(
            "GET",
            "/task/{id}/variables",
            path={"id": id},
            params={
                "deserializeValues": deserialize_values,
            },
        )

    def modify_task_variables(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Update/Delete Task Variables.

        Updates or deletes the variables visible from the task. Updates precede
        deletions. So, if a variable is updated AND deleted, the deletion overrides
        the update. A variable is visible from the task if it is a local task
        variable or declared in a parent scope of the task. See documentation on
        visibility of variables. Request body: an object with modifications,
        deletions.

        POST /task/{id}/variables
        """
        return self._call(
            "POST",
            "/task/{id}/variables",
            path={"id": id},
            body=body,
        )

    def put_task_variable(
        self,
        id: str,
        var_name: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Update Task Variable.

        Updates a process variable that is visible from the Task scope. A variable
        is visible from the task if it is a local task variable, or declared in a
        parent scope of the task. See the documentation on variable scopes and
        visibility. **Note**: If a variable doesn't exist, the variable is created
        in the top-most scope visible from the task. Request body: an object with
        value, type, valueInfo.

        PUT /task/{id}/variables/{varName}
        """
        return self._call(
            "PUT",
            "/task/{id}/variables/{varName}",
            path={"id": id, "varName": var_name},
            body=body,
        )

    def set_binary_task_variable(
        self,
        id: str,
        var_name: str,
        *,
        data: str | None = None,
        value_type: str | None = None,
        filename: str | None = None,
    ) -> Any:
        """Update Task Variable (Binary).

        Sets the serialized value for a binary variable or the binary value for a
        file variable visible from the task. A variable is visible from the task if
        it is a local task variable or declared in a parent scope of the task. See
        documentation on visibility of variables.

        POST /task/{id}/variables/{varName}/data
        """
        return self._call(
            "POST",
            "/task/{id}/variables/{varName}/data",
            path={"id": id, "varName": var_name},
            form={
                "valueType": value_type,
            },
            files=upload_part("data", data, filename),
        )
