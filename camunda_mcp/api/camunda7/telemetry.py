"""Operaton / Camunda 7 engine REST: the Telemetry operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7Telemetry(ApiClientBase):
    """Telemetry: 3 engine REST operation(s)."""

    def configure_telemetry(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Configure Telemetry.

        Deprecated: The sending telemetry feature is removed. Please remove the
        endpoint usages as they are no longer needed. Request body: an object with
        enableTelemetry.

        POST /telemetry/configuration
        """
        return self._call(
            "POST",
            "/telemetry/configuration",
            body=body,
        )

    def get_telemetry_configuration(
        self,
    ) -> Any:
        """Fetch Telemetry Configuration.

        Fetches Telemetry Configuration.

        GET /telemetry/configuration
        """
        return self._call(
            "GET",
            "/telemetry/configuration",
        )

    def get_telemetry_data(
        self,
    ) -> Any:
        """Fetch Telemetry Data.

        Deprecated: Always returns false. The sending telemetry feature is removed.
        Please remove the endpoint usages as they are no longer needed.

        GET /telemetry/data
        """
        return self._call(
            "GET",
            "/telemetry/data",
        )
