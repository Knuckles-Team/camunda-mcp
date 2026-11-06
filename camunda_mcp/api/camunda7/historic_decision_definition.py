"""Operaton / Camunda 7 engine REST: the Historic Decision Definition operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7HistoricDecisionDefinition(ApiClientBase):
    """Historic Decision Definition: 2 engine REST operation(s)."""

    def get_cleanable_historic_decision_instance_report(
        self,
        *,
        decision_definition_id_in: str | None = None,
        decision_definition_key_in: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        compact: bool | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
    ) -> Any:
        """Get Cleanable Decision Instance Report.

        Retrieves a report about a decision definition and finished decision
        instances relevant to history cleanup (see History cleanup), so that you can
        tune the history time to live. These reports include the count of the
        finished historic decision instances, cleanable decision instances and basic
        decision definition data - id, key, name and version.

        GET /history/decision-definition/cleanable-decision-instance-report
        """
        return self._call(
            "GET",
            "/history/decision-definition/cleanable-decision-instance-report",
            params={
                "decisionDefinitionIdIn": decision_definition_id_in,
                "decisionDefinitionKeyIn": decision_definition_key_in,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "compact": compact,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
            },
        )

    def get_cleanable_historic_decision_instance_report_count(
        self,
        *,
        decision_definition_id_in: str | None = None,
        decision_definition_key_in: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        compact: bool | None = None,
    ) -> Any:
        """Get Cleanable Decision Instance Report Count.

        Queries for the number of report results about a decision definition and
        finished decision instances relevant to history cleanup (see History
        cleanup). Takes the same parameters as the Get Cleanable Decision Instance
        Report method.

        GET /history/decision-definition/cleanable-decision-instance-report/count
        """
        return self._call(
            "GET",
            "/history/decision-definition/cleanable-decision-instance-report/count",
            params={
                "decisionDefinitionIdIn": decision_definition_id_in,
                "decisionDefinitionKeyIn": decision_definition_key_in,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "compact": compact,
            },
        )
