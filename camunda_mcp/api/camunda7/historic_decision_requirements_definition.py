"""Operaton / Camunda 7 engine REST: the Historic Decision Requirements Definition operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7HistoricDecisionRequirementsDefinition(ApiClientBase):
    """Historic Decision Requirements Definition: 1 engine REST operation(s)."""

    def get_decision_statistics(
        self,
        id: str,
        *,
        decision_instance_id: str | None = None,
    ) -> Any:
        """Get DRD Statistics.

        Retrieves evaluation statistics of a given decision requirements definition.

        GET /history/decision-requirements-definition/{id}/statistics
        """
        return self._call(
            "GET",
            "/history/decision-requirements-definition/{id}/statistics",
            path={"id": id},
            params={
                "decisionInstanceId": decision_instance_id,
            },
        )
