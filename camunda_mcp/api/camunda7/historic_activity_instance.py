"""Operaton / Camunda 7 engine REST: the Historic Activity Instance operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7HistoricActivityInstance(ApiClientBase):
    """Historic Activity Instance: 5 engine REST operation(s)."""

    def get_historic_activity_instance(
        self,
        id: str,
    ) -> Any:
        """Get.

        Retrieves a historic activity instance by id, according to the
        `HistoricActivityInstance` interface in the engine.

        GET /history/activity-instance/{id}
        """
        return self._call(
            "GET",
            "/history/activity-instance/{id}",
            path={"id": id},
        )

    def get_historic_activity_instances(
        self,
        *,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
        activity_instance_id: str | None = None,
        process_instance_id: str | None = None,
        process_definition_id: str | None = None,
        execution_id: str | None = None,
        activity_id: str | None = None,
        activity_name: str | None = None,
        activity_type: str | None = None,
        task_assignee: str | None = None,
        finished: bool | None = None,
        unfinished: bool | None = None,
        canceled: bool | None = None,
        complete_scope: bool | None = None,
        started_before: str | None = None,
        started_after: str | None = None,
        finished_before: str | None = None,
        finished_after: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
    ) -> Any:
        """Get List.

        Queries for historic activity instances that fulfill the given parameters.
        The size of the result set can be retrieved by using the Get Historic
        Activity Instance Count method.

        GET /history/activity-instance
        """
        return self._call(
            "GET",
            "/history/activity-instance",
            params={
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
                "activityInstanceId": activity_instance_id,
                "processInstanceId": process_instance_id,
                "processDefinitionId": process_definition_id,
                "executionId": execution_id,
                "activityId": activity_id,
                "activityName": activity_name,
                "activityType": activity_type,
                "taskAssignee": task_assignee,
                "finished": finished,
                "unfinished": unfinished,
                "canceled": canceled,
                "completeScope": complete_scope,
                "startedBefore": started_before,
                "startedAfter": started_after,
                "finishedBefore": finished_before,
                "finishedAfter": finished_after,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
            },
        )

    def get_historic_activity_instances_count(
        self,
        *,
        activity_instance_id: str | None = None,
        process_instance_id: str | None = None,
        process_definition_id: str | None = None,
        execution_id: str | None = None,
        activity_id: str | None = None,
        activity_name: str | None = None,
        activity_type: str | None = None,
        task_assignee: str | None = None,
        finished: bool | None = None,
        unfinished: bool | None = None,
        canceled: bool | None = None,
        complete_scope: bool | None = None,
        started_before: str | None = None,
        started_after: str | None = None,
        finished_before: str | None = None,
        finished_after: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
    ) -> Any:
        """Get List Count.

        Queries for the number of historic activity instances that fulfill the given
        parameters. Takes the same parameters as the Get Historic Activity Instance
        method.

        GET /history/activity-instance/count
        """
        return self._call(
            "GET",
            "/history/activity-instance/count",
            params={
                "activityInstanceId": activity_instance_id,
                "processInstanceId": process_instance_id,
                "processDefinitionId": process_definition_id,
                "executionId": execution_id,
                "activityId": activity_id,
                "activityName": activity_name,
                "activityType": activity_type,
                "taskAssignee": task_assignee,
                "finished": finished,
                "unfinished": unfinished,
                "canceled": canceled,
                "completeScope": complete_scope,
                "startedBefore": started_before,
                "startedAfter": started_after,
                "finishedBefore": finished_before,
                "finishedAfter": finished_after,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
            },
        )

    def query_historic_activity_instances(
        self,
        *,
        first_result: int | None = None,
        max_results: int | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Get List (POST).

        Queries for historic activity instances that fulfill the given parameters.
        The size of the result set can be retrieved by using the Get Historic
        Activity Instance Count method. Request body: an object with
        activityInstanceId, processInstanceId, processDefinitionId, executionId,
        activityId, activityName, activityType, taskAssignee, finished, unfinished,
        canceled, completeScope, startedBefore, startedAfter, finishedBefore,
        finishedAfter, tenantIdIn, withoutTenantId, sorting.

        POST /history/activity-instance
        """
        return self._call(
            "POST",
            "/history/activity-instance",
            params={
                "firstResult": first_result,
                "maxResults": max_results,
            },
            body=body,
        )

    def query_historic_activity_instances_count(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Get List Count (POST).

        Queries for the number of historic activity instances that fulfill the given
        parameters. Request body: an object with activityInstanceId,
        processInstanceId, processDefinitionId, executionId, activityId,
        activityName, activityType, taskAssignee, finished, unfinished, canceled,
        completeScope, startedBefore, startedAfter, finishedBefore, finishedAfter,
        tenantIdIn, withoutTenantId, sorting.

        POST /history/activity-instance/count
        """
        return self._call(
            "POST",
            "/history/activity-instance/count",
            body=body,
        )
