"""Operaton / Camunda 7 engine REST: the Condition operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7Condition(ApiClientBase):
    """Condition: 1 engine REST operation(s)."""

    def evaluate_condition(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Evaluate.

        Triggers evaluation of conditions for conditional start event(s). Internally
        this maps to the engines condition evaluation builder method
        ConditionEvaluationBuilder#evaluateStartConditions(). For more information
        see the Conditional Start Events section of the BPMN 2.0 Implementation
        Reference. Request body: an object with variables, businessKey, tenantId,
        withoutTenantId, processDefinitionId.

        POST /condition
        """
        return self._call(
            "POST",
            "/condition",
            body=body,
        )
