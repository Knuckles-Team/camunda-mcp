"""Operaton / Camunda 7 engine REST: the Signal operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7Signal(ApiClientBase):
    """Signal: 1 engine REST operation(s)."""

    def throw_signal(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Event.

        A signal is an event of global scope (broadcast semantics) and is delivered
        to all active handlers. Internally this maps to the engine's signal event
        received builder method `RuntimeService#createSignalEvent()`. For more
        information about the signal behavior, see the Signal Events section of the
        BPMN 2.0 Implementation Reference. Request body: an object with name,
        executionId, variables, tenantId, withoutTenantId.

        POST /signal
        """
        return self._call(
            "POST",
            "/signal",
            body=body,
        )
