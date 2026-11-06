"""Operaton / Camunda 7 engine REST: the Historic Identity Link Log operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7HistoricIdentityLinkLog(ApiClientBase):
    """Historic Identity Link Log: 2 engine REST operation(s)."""

    def get_historic_identity_links(
        self,
        *,
        type: str | None = None,
        user_id: str | None = None,
        group_id: str | None = None,
        date_before: str | None = None,
        date_after: str | None = None,
        task_id: str | None = None,
        process_definition_id: str | None = None,
        process_definition_key: str | None = None,
        operation_type: str | None = None,
        assigner_id: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
    ) -> Any:
        """Get Identity Link Logs.

        Queries for historic identity link logs that fulfill given parameters. The
        size of the result set can be retrieved by using the Get Identity-Link-Log
        Count method.

        GET /history/identity-link-log
        """
        return self._call(
            "GET",
            "/history/identity-link-log",
            params={
                "type": type,
                "userId": user_id,
                "groupId": group_id,
                "dateBefore": date_before,
                "dateAfter": date_after,
                "taskId": task_id,
                "processDefinitionId": process_definition_id,
                "processDefinitionKey": process_definition_key,
                "operationType": operation_type,
                "assignerId": assigner_id,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
            },
        )

    def get_historic_identity_links_count(
        self,
        *,
        type: str | None = None,
        user_id: str | None = None,
        group_id: str | None = None,
        date_before: str | None = None,
        date_after: str | None = None,
        task_id: str | None = None,
        process_definition_id: str | None = None,
        process_definition_key: str | None = None,
        operation_type: str | None = None,
        assigner_id: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
    ) -> Any:
        """Get Identity Link Log Count.

        Queries for the number of historic identity link logs that fulfill the given
        parameters. Takes the same parameters as the Get Identity-Link-Logs method.

        GET /history/identity-link-log/count
        """
        return self._call(
            "GET",
            "/history/identity-link-log/count",
            params={
                "type": type,
                "userId": user_id,
                "groupId": group_id,
                "dateBefore": date_before,
                "dateAfter": date_after,
                "taskId": task_id,
                "processDefinitionId": process_definition_id,
                "processDefinitionKey": process_definition_key,
                "operationType": operation_type,
                "assignerId": assigner_id,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
            },
        )
