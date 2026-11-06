"""Operaton / Camunda 7 engine REST: the Historic Variable Instance operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7HistoricVariableInstance(ApiClientBase):
    """Historic Variable Instance: 7 engine REST operation(s)."""

    def delete_historic_variable_instance(
        self,
        id: str,
    ) -> Any:
        """Delete Variable Instance.

        Deletes a historic variable instance by id.

        DELETE /history/variable-instance/{id}
        """
        return self._call(
            "DELETE",
            "/history/variable-instance/{id}",
            path={"id": id},
        )

    def get_historic_variable_instance(
        self,
        id: str,
        *,
        deserialize_values: bool | None = None,
    ) -> Any:
        """Get Variable Instance.

        Retrieves a historic variable by id.

        GET /history/variable-instance/{id}
        """
        return self._call(
            "GET",
            "/history/variable-instance/{id}",
            path={"id": id},
            params={
                "deserializeValues": deserialize_values,
            },
        )

    def get_historic_variable_instance_binary(
        self,
        id: str,
    ) -> Any:
        """Get Variable Instance (Binary).

        Retrieves the content of a historic variable by id. Applicable for variables
        that are serialized as binary data.

        GET /history/variable-instance/{id}/data
        """
        return self._call(
            "GET",
            "/history/variable-instance/{id}/data",
            path={"id": id},
        )

    def get_historic_variable_instances(
        self,
        *,
        variable_name: str | None = None,
        variable_name_like: str | None = None,
        variable_value: str | None = None,
        variable_names_ignore_case: bool | None = None,
        variable_values_ignore_case: bool | None = None,
        variable_type_in: str | None = None,
        include_deleted: bool | None = None,
        process_instance_id: str | None = None,
        process_instance_id_in: str | None = None,
        process_definition_id: str | None = None,
        process_definition_key: str | None = None,
        execution_id_in: str | None = None,
        case_instance_id: str | None = None,
        case_execution_id_in: str | None = None,
        case_activity_id_in: str | None = None,
        task_id_in: str | None = None,
        activity_instance_id_in: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        variable_name_in: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
        deserialize_values: bool | None = None,
    ) -> Any:
        """Get Variable Instances.

        Queries for historic variable instances that fulfill the given parameters.
        The size of the result set can be retrieved by using the Get Variable
        Instance Count method.

        GET /history/variable-instance
        """
        return self._call(
            "GET",
            "/history/variable-instance",
            params={
                "variableName": variable_name,
                "variableNameLike": variable_name_like,
                "variableValue": variable_value,
                "variableNamesIgnoreCase": variable_names_ignore_case,
                "variableValuesIgnoreCase": variable_values_ignore_case,
                "variableTypeIn": variable_type_in,
                "includeDeleted": include_deleted,
                "processInstanceId": process_instance_id,
                "processInstanceIdIn": process_instance_id_in,
                "processDefinitionId": process_definition_id,
                "processDefinitionKey": process_definition_key,
                "executionIdIn": execution_id_in,
                "caseInstanceId": case_instance_id,
                "caseExecutionIdIn": case_execution_id_in,
                "caseActivityIdIn": case_activity_id_in,
                "taskIdIn": task_id_in,
                "activityInstanceIdIn": activity_instance_id_in,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "variableNameIn": variable_name_in,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
                "deserializeValues": deserialize_values,
            },
        )

    def get_historic_variable_instances_count(
        self,
        *,
        variable_name: str | None = None,
        variable_name_like: str | None = None,
        variable_value: str | None = None,
        variable_names_ignore_case: bool | None = None,
        variable_values_ignore_case: bool | None = None,
        variable_type_in: str | None = None,
        include_deleted: bool | None = None,
        process_instance_id: str | None = None,
        process_instance_id_in: str | None = None,
        process_definition_id: str | None = None,
        process_definition_key: str | None = None,
        execution_id_in: str | None = None,
        case_instance_id: str | None = None,
        case_execution_id_in: str | None = None,
        case_activity_id_in: str | None = None,
        task_id_in: str | None = None,
        activity_instance_id_in: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        variable_name_in: str | None = None,
    ) -> Any:
        """Get Variable Instance Count.

        Queries for the number of historic variable instances that fulfill the given
        parameters. Takes the same parameters as the Get Variable Instances method.

        GET /history/variable-instance/count
        """
        return self._call(
            "GET",
            "/history/variable-instance/count",
            params={
                "variableName": variable_name,
                "variableNameLike": variable_name_like,
                "variableValue": variable_value,
                "variableNamesIgnoreCase": variable_names_ignore_case,
                "variableValuesIgnoreCase": variable_values_ignore_case,
                "variableTypeIn": variable_type_in,
                "includeDeleted": include_deleted,
                "processInstanceId": process_instance_id,
                "processInstanceIdIn": process_instance_id_in,
                "processDefinitionId": process_definition_id,
                "processDefinitionKey": process_definition_key,
                "executionIdIn": execution_id_in,
                "caseInstanceId": case_instance_id,
                "caseExecutionIdIn": case_execution_id_in,
                "caseActivityIdIn": case_activity_id_in,
                "taskIdIn": task_id_in,
                "activityInstanceIdIn": activity_instance_id_in,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "variableNameIn": variable_name_in,
            },
        )

    def query_historic_variable_instances(
        self,
        *,
        first_result: int | None = None,
        max_results: int | None = None,
        deserialize_values: bool | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Get Variable Instances (POST).

        Queries for historic variable instances that fulfill the given parameters.
        This method is slightly more powerful than the Get Variable Instances method
        because it allows filtering by variable values of the different types
        `String`, `Number` or `Boolean`. Request body: an object with variableName,
        variableNameLike, variableValue, variableNamesIgnoreCase,
        variableValuesIgnoreCase, variableTypeIn, includeDeleted, processInstanceId,
        processInstanceIdIn, processDefinitionId, processDefinitionKey,
        executionIdIn, caseInstanceId, caseExecutionIdIn, caseActivityIdIn,
        taskIdIn, activityInstanceIdIn, tenantIdIn, withoutTenantId, variableNameIn,
        sorting.

        POST /history/variable-instance
        """
        return self._call(
            "POST",
            "/history/variable-instance",
            params={
                "firstResult": first_result,
                "maxResults": max_results,
                "deserializeValues": deserialize_values,
            },
            body=body,
        )

    def query_historic_variable_instances_count(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Get Variable Instance Count (POST).

        Queries for historic variable instances that fulfill the given parameters.
        This method takes the same message body as the Get Variable Instances (POST)
        method and therefore it is more powerful regarding variable values than the
        Get Variable Instance Count method. Request body: an object with
        variableName, variableNameLike, variableValue, variableNamesIgnoreCase,
        variableValuesIgnoreCase, variableTypeIn, includeDeleted, processInstanceId,
        processInstanceIdIn, processDefinitionId, processDefinitionKey,
        executionIdIn, caseInstanceId, caseExecutionIdIn, caseActivityIdIn,
        taskIdIn, activityInstanceIdIn, tenantIdIn, withoutTenantId, variableNameIn,
        sorting.

        POST /history/variable-instance/count
        """
        return self._call(
            "POST",
            "/history/variable-instance/count",
            body=body,
        )
