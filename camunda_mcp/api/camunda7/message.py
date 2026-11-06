"""Operaton / Camunda 7 engine REST: the Message operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7Message(ApiClientBase):
    """Message: 1 engine REST operation(s)."""

    def deliver_message(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Correlate.

        Correlates a message to the process engine to either trigger a message start
        event or an intermediate message catching event. Internally this maps to the
        engine's message correlation builder methods
        `MessageCorrelationBuilder#correlateWithResult()` and
        `MessageCorrelationBuilder#correlateAllWithResult()`. Request body: an
        object with messageName, businessKey, tenantId, withoutTenantId,
        processInstanceId, correlationKeys, localCorrelationKeys, processVariables,
        processVariablesLocal, processVariablesToTriggeredScope, all, resultEnabled,
        variablesInResultEnabled.

        POST /message
        """
        return self._call(
            "POST",
            "/message",
            body=body,
        )
