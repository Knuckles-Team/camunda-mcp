"""Operaton / Camunda 7 engine REST: the Historic Detail operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7HistoricDetail(ApiClientBase):
    """Historic Detail: 5 engine REST operation(s)."""

    def get_historic_details(
        self,
        *,
        process_instance_id: str | None = None,
        process_instance_id_in: str | None = None,
        execution_id: str | None = None,
        task_id: str | None = None,
        activity_instance_id: str | None = None,
        case_instance_id: str | None = None,
        case_execution_id: str | None = None,
        variable_instance_id: str | None = None,
        variable_type_in: str | None = None,
        variable_name_like: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        user_operation_id: str | None = None,
        form_fields: bool | None = None,
        variable_updates: bool | None = None,
        exclude_task_details: bool | None = None,
        initial: bool | None = None,
        occurred_before: str | None = None,
        occurred_after: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
        deserialize_values: bool | None = None,
    ) -> Any:
        """Get Historic Details.

        Queries for historic details that fulfill the given parameters. The size of
        the result set can be retrieved by using the Get Historic Detail Count
        method.

        GET /history/detail
        """
        return self._call(
            "GET",
            "/history/detail",
            params={
                "processInstanceId": process_instance_id,
                "processInstanceIdIn": process_instance_id_in,
                "executionId": execution_id,
                "taskId": task_id,
                "activityInstanceId": activity_instance_id,
                "caseInstanceId": case_instance_id,
                "caseExecutionId": case_execution_id,
                "variableInstanceId": variable_instance_id,
                "variableTypeIn": variable_type_in,
                "variableNameLike": variable_name_like,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "userOperationId": user_operation_id,
                "formFields": form_fields,
                "variableUpdates": variable_updates,
                "excludeTaskDetails": exclude_task_details,
                "initial": initial,
                "occurredBefore": occurred_before,
                "occurredAfter": occurred_after,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
                "deserializeValues": deserialize_values,
            },
        )

    def get_historic_details_count(
        self,
        *,
        process_instance_id: str | None = None,
        process_instance_id_in: str | None = None,
        execution_id: str | None = None,
        task_id: str | None = None,
        activity_instance_id: str | None = None,
        case_instance_id: str | None = None,
        case_execution_id: str | None = None,
        variable_instance_id: str | None = None,
        variable_type_in: str | None = None,
        variable_name_like: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        user_operation_id: str | None = None,
        form_fields: bool | None = None,
        variable_updates: bool | None = None,
        exclude_task_details: bool | None = None,
        initial: bool | None = None,
        occurred_before: str | None = None,
        occurred_after: str | None = None,
    ) -> Any:
        """Get Historic Detail Count.

        Queries for the number of historic details that fulfill the given
        parameters. Takes the same parameters as the Get Historic Details method.

        GET /history/detail/count
        """
        return self._call(
            "GET",
            "/history/detail/count",
            params={
                "processInstanceId": process_instance_id,
                "processInstanceIdIn": process_instance_id_in,
                "executionId": execution_id,
                "taskId": task_id,
                "activityInstanceId": activity_instance_id,
                "caseInstanceId": case_instance_id,
                "caseExecutionId": case_execution_id,
                "variableInstanceId": variable_instance_id,
                "variableTypeIn": variable_type_in,
                "variableNameLike": variable_name_like,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "userOperationId": user_operation_id,
                "formFields": form_fields,
                "variableUpdates": variable_updates,
                "excludeTaskDetails": exclude_task_details,
                "initial": initial,
                "occurredBefore": occurred_before,
                "occurredAfter": occurred_after,
            },
        )

    def historic_detail(
        self,
        id: str,
        *,
        deserialize_value: bool | None = None,
    ) -> Any:
        """Get Historic Detail.

        Retrieves a historic detail by id.

        GET /history/detail/{id}
        """
        return self._call(
            "GET",
            "/history/detail/{id}",
            path={"id": id},
            params={
                "deserializeValue": deserialize_value,
            },
        )

    def historic_detail_binary(
        self,
        id: str,
    ) -> Any:
        """Get Historic Detail (Binary).

        Retrieves the content of a historic variable update by id. Applicable for
        byte array and file variables.

        GET /history/detail/{id}/data
        """
        return self._call(
            "GET",
            "/history/detail/{id}/data",
            path={"id": id},
        )

    def query_historic_details(
        self,
        *,
        first_result: int | None = None,
        max_results: int | None = None,
        deserialize_values: bool | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Get Historic Details (POST).

        Queries for historic details that fulfill the given parameters. This method
        is slightly more powerful than the Get Historic Details method because it
        allows sorting by multiple parameters. The size of the result set can be
        retrieved by using the Get Historic Detail Count method. Request body: an
        object with processInstanceId, processInstanceIdIn, executionId, taskId,
        activityInstanceId, caseInstanceId, caseExecutionId, variableInstanceId,
        variableTypeIn, variableNameLike, tenantIdIn, withoutTenantId,
        userOperationId, formFields, variableUpdates, excludeTaskDetails, initial,
        occurredBefore, occurredAfter, sorting.

        POST /history/detail
        """
        return self._call(
            "POST",
            "/history/detail",
            params={
                "firstResult": first_result,
                "maxResults": max_results,
                "deserializeValues": deserialize_values,
            },
            body=body,
        )
