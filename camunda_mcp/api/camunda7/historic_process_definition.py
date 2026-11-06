"""Operaton / Camunda 7 engine REST: the Historic Process Definition operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7HistoricProcessDefinition(ApiClientBase):
    """Historic Process Definition: 3 engine REST operation(s)."""

    def get_cleanable_historic_process_instance_report(
        self,
        *,
        process_definition_id_in: str | None = None,
        process_definition_key_in: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        compact: bool | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
    ) -> Any:
        """Get Cleanable Process Instance Report.

        Retrieves a report about a process definition and finished process instances
        relevant to history cleanup (see History cleanup) so that you can tune the
        history time to live. These reports include the count of the finished
        historic process instances, cleanable process instances and basic process
        definition data - id, key, name and version.

        GET /history/process-definition/cleanable-process-instance-report
        """
        return self._call(
            "GET",
            "/history/process-definition/cleanable-process-instance-report",
            params={
                "processDefinitionIdIn": process_definition_id_in,
                "processDefinitionKeyIn": process_definition_key_in,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "compact": compact,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
            },
        )

    def get_cleanable_historic_process_instance_report_count(
        self,
        *,
        process_definition_id_in: str | None = None,
        process_definition_key_in: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        compact: bool | None = None,
    ) -> Any:
        """Get Cleanable Process Instance Report Count.

        Queries for the number of report results about a process definition and
        finished process instances relevant to history cleanup (see History
        cleanup). Takes the same parameters as the Get Cleanable Process Instance
        Report method.

        GET /history/process-definition/cleanable-process-instance-report/count
        """
        return self._call(
            "GET",
            "/history/process-definition/cleanable-process-instance-report/count",
            params={
                "processDefinitionIdIn": process_definition_id_in,
                "processDefinitionKeyIn": process_definition_key_in,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "compact": compact,
            },
        )

    def get_historic_activity_statistics(
        self,
        id: str,
        *,
        canceled: bool | None = None,
        finished: bool | None = None,
        complete_scope: bool | None = None,
        incidents: bool | None = None,
        started_before: str | None = None,
        started_after: str | None = None,
        finished_before: str | None = None,
        finished_after: str | None = None,
        process_instance_id_in: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
    ) -> Any:
        """Get Historic Activity Statistics.

        Retrieves historic statistics of a given process definition, grouped by
        activities.

        GET /history/process-definition/{id}/statistics
        """
        return self._call(
            "GET",
            "/history/process-definition/{id}/statistics",
            path={"id": id},
            params={
                "canceled": canceled,
                "finished": finished,
                "completeScope": complete_scope,
                "incidents": incidents,
                "startedBefore": started_before,
                "startedAfter": started_after,
                "finishedBefore": finished_before,
                "finishedAfter": finished_after,
                "processInstanceIdIn": process_instance_id_in,
                "sortBy": sort_by,
                "sortOrder": sort_order,
            },
        )
