"""Operaton / Camunda 7 engine REST: the Version operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7Version(ApiClientBase):
    """Version: 1 engine REST operation(s)."""

    def get_rest_api_version(
        self,
    ) -> Any:
        """Get Rest API version.

        Retrieves the version of the Rest API.

        GET /version
        """
        return self._call(
            "GET",
            "/version",
        )
