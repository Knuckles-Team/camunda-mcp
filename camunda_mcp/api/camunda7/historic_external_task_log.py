"""Operaton / Camunda 7 engine REST: the Historic External Task Log operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7HistoricExternalTaskLog(ApiClientBase):
    """Historic External Task Log: 6 engine REST operation(s)."""

    def get_error_details_historic_external_task_log(
        self,
        id: str,
    ) -> Any:
        """Get External Task Log Error Details.

        Retrieves the corresponding error details of the passed historic external
        task log by id.

        GET /history/external-task-log/{id}/error-details
        """
        return self._call(
            "GET",
            "/history/external-task-log/{id}/error-details",
            path={"id": id},
        )

    def get_historic_external_task_log(
        self,
        id: str,
    ) -> Any:
        """Get External Task Log.

        Retrieves a historic external task log by id.

        GET /history/external-task-log/{id}
        """
        return self._call(
            "GET",
            "/history/external-task-log/{id}",
            path={"id": id},
        )

    def get_historic_external_task_logs(
        self,
        *,
        log_id: str | None = None,
        external_task_id: str | None = None,
        topic_name: str | None = None,
        worker_id: str | None = None,
        error_message: str | None = None,
        activity_id_in: str | None = None,
        activity_instance_id_in: str | None = None,
        execution_id_in: str | None = None,
        process_instance_id: str | None = None,
        process_definition_id: str | None = None,
        process_definition_key: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        priority_lower_than_or_equals: int | None = None,
        priority_higher_than_or_equals: int | None = None,
        creation_log: bool | None = None,
        failure_log: bool | None = None,
        success_log: bool | None = None,
        deletion_log: bool | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
    ) -> Any:
        """Get External Task Logs.

        Queries for historic external task logs that fulfill the given parameters.
        The size of the result set can be retrieved by using the Get External Task
        Log Count method.

        GET /history/external-task-log
        """
        return self._call(
            "GET",
            "/history/external-task-log",
            params={
                "logId": log_id,
                "externalTaskId": external_task_id,
                "topicName": topic_name,
                "workerId": worker_id,
                "errorMessage": error_message,
                "activityIdIn": activity_id_in,
                "activityInstanceIdIn": activity_instance_id_in,
                "executionIdIn": execution_id_in,
                "processInstanceId": process_instance_id,
                "processDefinitionId": process_definition_id,
                "processDefinitionKey": process_definition_key,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "priorityLowerThanOrEquals": priority_lower_than_or_equals,
                "priorityHigherThanOrEquals": priority_higher_than_or_equals,
                "creationLog": creation_log,
                "failureLog": failure_log,
                "successLog": success_log,
                "deletionLog": deletion_log,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
            },
        )

    def get_historic_external_task_logs_count(
        self,
        *,
        log_id: str | None = None,
        external_task_id: str | None = None,
        topic_name: str | None = None,
        worker_id: str | None = None,
        error_message: str | None = None,
        activity_id_in: str | None = None,
        activity_instance_id_in: str | None = None,
        execution_id_in: str | None = None,
        process_instance_id: str | None = None,
        process_definition_id: str | None = None,
        process_definition_key: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        priority_lower_than_or_equals: int | None = None,
        priority_higher_than_or_equals: int | None = None,
        creation_log: bool | None = None,
        failure_log: bool | None = None,
        success_log: bool | None = None,
        deletion_log: bool | None = None,
    ) -> Any:
        """Get External Task Log Count.

        Queries for the number of historic external task logs that fulfill the given
        parameters. Takes the same parameters as the Get External Task Logs method.

        GET /history/external-task-log/count
        """
        return self._call(
            "GET",
            "/history/external-task-log/count",
            params={
                "logId": log_id,
                "externalTaskId": external_task_id,
                "topicName": topic_name,
                "workerId": worker_id,
                "errorMessage": error_message,
                "activityIdIn": activity_id_in,
                "activityInstanceIdIn": activity_instance_id_in,
                "executionIdIn": execution_id_in,
                "processInstanceId": process_instance_id,
                "processDefinitionId": process_definition_id,
                "processDefinitionKey": process_definition_key,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "priorityLowerThanOrEquals": priority_lower_than_or_equals,
                "priorityHigherThanOrEquals": priority_higher_than_or_equals,
                "creationLog": creation_log,
                "failureLog": failure_log,
                "successLog": success_log,
                "deletionLog": deletion_log,
            },
        )

    def query_historic_external_task_logs(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Get External Task Logs (POST).

        Queries for historic external task logs that fulfill the given parameters.
        This method is slightly more powerful than the Get External Task Logs method
        because it allows filtering by historic external task logs values of the
        different types `String`, `Number` or `Boolean`. Request body: an object
        with logId, externalTaskId, topicName, workerId, errorMessage, activityIdIn,
        activityInstanceIdIn, executionIdIn, processInstanceId, processDefinitionId,
        processDefinitionKey, tenantIdIn, withoutTenantId,
        priorityLowerThanOrEquals, priorityHigherThanOrEquals, creationLog,
        failureLog, successLog, deletionLog, sorting.

        POST /history/external-task-log
        """
        return self._call(
            "POST",
            "/history/external-task-log",
            body=body,
        )

    def query_historic_external_task_logs_count(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Get External Task Log Count (POST).

        Queries for the number of historic external task logs that fulfill the given
        parameters. This method takes the same message body as the Get External Task
        Logs (POST) method and therefore it is slightly more powerful than the Get
        External Task Log Count method. Request body: an object with logId,
        externalTaskId, topicName, workerId, errorMessage, activityIdIn,
        activityInstanceIdIn, executionIdIn, processInstanceId, processDefinitionId,
        processDefinitionKey, tenantIdIn, withoutTenantId,
        priorityLowerThanOrEquals, priorityHigherThanOrEquals, creationLog,
        failureLog, successLog, deletionLog, sorting.

        POST /history/external-task-log/count
        """
        return self._call(
            "POST",
            "/history/external-task-log/count",
            body=body,
        )
