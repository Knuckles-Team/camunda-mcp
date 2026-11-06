"""Operaton / Camunda 7 engine REST: the Engine operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7Engine(ApiClientBase):
    """Engine: 1 engine REST operation(s)."""

    def get_process_engine_names(
        self,
    ) -> Any:
        """Get List.

        Retrieves the names of all process engines available on your platform.
        **Note**: You cannot prepend `/engine/{name}` to this method.

        GET /engine
        """
        return self._call(
            "GET",
            "/engine",
        )
