"""Operaton / Camunda 7 engine REST: the Variable Instance operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7VariableInstance(ApiClientBase):
    """Variable Instance: 6 engine REST operation(s)."""

    def get_variable_instance(
        self,
        id: str,
        *,
        deserialize_value: bool | None = None,
    ) -> Any:
        """Get Variable Instance.

        Retrieves a variable by id.

        GET /variable-instance/{id}
        """
        return self._call(
            "GET",
            "/variable-instance/{id}",
            path={"id": id},
            params={
                "deserializeValue": deserialize_value,
            },
        )

    def get_variable_instance_binary(
        self,
        id: str,
    ) -> Any:
        """Get Variable Instance (Binary).

        Retrieves the content of a variable by id. Applicable for byte array and
        file variables.

        GET /variable-instance/{id}/data
        """
        return self._call(
            "GET",
            "/variable-instance/{id}/data",
            path={"id": id},
        )

    def get_variable_instances(
        self,
        *,
        variable_name: str | None = None,
        variable_name_like: str | None = None,
        process_instance_id_in: str | None = None,
        execution_id_in: str | None = None,
        case_instance_id_in: str | None = None,
        case_execution_id_in: str | None = None,
        task_id_in: str | None = None,
        batch_id_in: str | None = None,
        activity_instance_id_in: str | None = None,
        tenant_id_in: str | None = None,
        variable_values: str | None = None,
        variable_names_ignore_case: bool | None = None,
        variable_values_ignore_case: bool | None = None,
        variable_scope_id_in: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
        deserialize_values: bool | None = None,
    ) -> Any:
        """Get Variable Instances.

        Query for variable instances that fulfill given parameters. Parameters may
        be the properties of variable instances, such as the name or type. The size
        of the result set can be retrieved by using the Get Variable Instance Count
        method.

        GET /variable-instance
        """
        return self._call(
            "GET",
            "/variable-instance",
            params={
                "variableName": variable_name,
                "variableNameLike": variable_name_like,
                "processInstanceIdIn": process_instance_id_in,
                "executionIdIn": execution_id_in,
                "caseInstanceIdIn": case_instance_id_in,
                "caseExecutionIdIn": case_execution_id_in,
                "taskIdIn": task_id_in,
                "batchIdIn": batch_id_in,
                "activityInstanceIdIn": activity_instance_id_in,
                "tenantIdIn": tenant_id_in,
                "variableValues": variable_values,
                "variableNamesIgnoreCase": variable_names_ignore_case,
                "variableValuesIgnoreCase": variable_values_ignore_case,
                "variableScopeIdIn": variable_scope_id_in,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
                "deserializeValues": deserialize_values,
            },
        )

    def get_variable_instances_count(
        self,
        *,
        variable_name: str | None = None,
        variable_name_like: str | None = None,
        process_instance_id_in: str | None = None,
        execution_id_in: str | None = None,
        case_instance_id_in: str | None = None,
        case_execution_id_in: str | None = None,
        task_id_in: str | None = None,
        batch_id_in: str | None = None,
        activity_instance_id_in: str | None = None,
        tenant_id_in: str | None = None,
        variable_values: str | None = None,
        variable_names_ignore_case: bool | None = None,
        variable_values_ignore_case: bool | None = None,
        variable_scope_id_in: str | None = None,
    ) -> Any:
        """Get Variable Instance Count.

        Query for the number of variable instances that fulfill given parameters.
        Takes the same parameters as the Get Variable Instances method.

        GET /variable-instance/count
        """
        return self._call(
            "GET",
            "/variable-instance/count",
            params={
                "variableName": variable_name,
                "variableNameLike": variable_name_like,
                "processInstanceIdIn": process_instance_id_in,
                "executionIdIn": execution_id_in,
                "caseInstanceIdIn": case_instance_id_in,
                "caseExecutionIdIn": case_execution_id_in,
                "taskIdIn": task_id_in,
                "batchIdIn": batch_id_in,
                "activityInstanceIdIn": activity_instance_id_in,
                "tenantIdIn": tenant_id_in,
                "variableValues": variable_values,
                "variableNamesIgnoreCase": variable_names_ignore_case,
                "variableValuesIgnoreCase": variable_values_ignore_case,
                "variableScopeIdIn": variable_scope_id_in,
            },
        )

    def query_variable_instances(
        self,
        *,
        first_result: int | None = None,
        max_results: int | None = None,
        deserialize_values: bool | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Get Variable Instances (POST).

        Query for variable instances that fulfill given parameters through a JSON
        object. This method is slightly more powerful than the Get Variable
        Instances method because it allows filtering by multiple variable instances
        of types `String`, `Number` or `Boolean`. Request body: an object with
        variableName, variableNameLike, processInstanceIdIn, executionIdIn,
        caseInstanceIdIn, caseExecutionIdIn, taskIdIn, batchIdIn,
        activityInstanceIdIn, tenantIdIn, variableValues, variableNamesIgnoreCase,
        variableValuesIgnoreCase, variableScopeIdIn, sorting.

        POST /variable-instance
        """
        return self._call(
            "POST",
            "/variable-instance",
            params={
                "firstResult": first_result,
                "maxResults": max_results,
                "deserializeValues": deserialize_values,
            },
            body=body,
        )

    def query_variable_instances_count(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Get Variable Instance Count (POST).

        Query for the number of variable instances that fulfill given parameters.
        This method takes the same message body as the Get Variable Instances POST
        method and therefore it is slightly more powerful than the Get Variable
        Instance Count method. Request body: an object with variableName,
        variableNameLike, processInstanceIdIn, executionIdIn, caseInstanceIdIn,
        caseExecutionIdIn, taskIdIn, batchIdIn, activityInstanceIdIn, tenantIdIn,
        variableValues, variableNamesIgnoreCase, variableValuesIgnoreCase,
        variableScopeIdIn, sorting.

        POST /variable-instance/count
        """
        return self._call(
            "POST",
            "/variable-instance/count",
            body=body,
        )
