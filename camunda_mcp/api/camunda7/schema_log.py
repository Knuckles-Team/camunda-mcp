"""Operaton / Camunda 7 engine REST: the Schema Log operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7SchemaLog(ApiClientBase):
    """Schema Log: 2 engine REST operation(s)."""

    def get_schema_log(
        self,
        *,
        version: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
    ) -> Any:
        """Get List.

        Queries for schema log entries that fulfill given parameters.

        GET /schema/log
        """
        return self._call(
            "GET",
            "/schema/log",
            params={
                "version": version,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
            },
        )

    def query_schema_log(
        self,
        *,
        first_result: int | None = None,
        max_results: int | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Get List (POST).

        Queries for schema log entries that fulfill given parameters. Request body:
        an object with version, sorting.

        POST /schema/log
        """
        return self._call(
            "POST",
            "/schema/log",
            params={
                "firstResult": first_result,
                "maxResults": max_results,
            },
            body=body,
        )
