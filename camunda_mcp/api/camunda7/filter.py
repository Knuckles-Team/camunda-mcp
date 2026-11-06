"""Operaton / Camunda 7 engine REST: the Filter operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7Filter(ApiClientBase):
    """Filter: 12 engine REST operation(s)."""

    def create_filter(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Create Filter.

        Creates a new filter. Request body: an object with resourceType, name,
        owner, query, properties.

        POST /filter/create
        """
        return self._call(
            "POST",
            "/filter/create",
            body=body,
        )

    def delete_filter(
        self,
        id: str,
    ) -> Any:
        """Delete Filter.

        Deletes a filter by id.

        DELETE /filter/{id}
        """
        return self._call(
            "DELETE",
            "/filter/{id}",
            path={"id": id},
        )

    def execute_filter_count(
        self,
        id: str,
    ) -> Any:
        """Execute Filter Count.

        Executes the saved query of the filter by id and returns the count.

        GET /filter/{id}/count
        """
        return self._call(
            "GET",
            "/filter/{id}/count",
            path={"id": id},
        )

    def execute_filter_list(
        self,
        id: str,
        *,
        first_result: int | None = None,
        max_results: int | None = None,
    ) -> Any:
        """Execute Filter List.

        Executes the saved query of the filter by id and returns the result list.

        GET /filter/{id}/list
        """
        return self._call(
            "GET",
            "/filter/{id}/list",
            path={"id": id},
            params={
                "firstResult": first_result,
                "maxResults": max_results,
            },
        )

    def execute_filter_single_result(
        self,
        id: str,
    ) -> Any:
        """Execute Filter Single Result.

        Executes the saved query of the filter by id and returns the single result.

        GET /filter/{id}/singleResult
        """
        return self._call(
            "GET",
            "/filter/{id}/singleResult",
            path={"id": id},
        )

    def get_filter_count(
        self,
        *,
        filter_id: str | None = None,
        resource_type: str | None = None,
        name: str | None = None,
        name_like: str | None = None,
        owner: str | None = None,
    ) -> Any:
        """Get Filter Count.

        Retrieves the number of filters that fulfill a provided query. Corresponds
        to the size of the result set when using the Get Filters method.

        GET /filter/count
        """
        return self._call(
            "GET",
            "/filter/count",
            params={
                "filterId": filter_id,
                "resourceType": resource_type,
                "name": name,
                "nameLike": name_like,
                "owner": owner,
            },
        )

    def get_filter_list(
        self,
        *,
        filter_id: str | None = None,
        resource_type: str | None = None,
        name: str | None = None,
        name_like: str | None = None,
        owner: str | None = None,
        item_count: bool | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
    ) -> Any:
        """Get Filters.

        Queries for a list of filters using a list of parameters. The size of the
        result set can be retrieved by using the Get Filter Count method.

        GET /filter
        """
        return self._call(
            "GET",
            "/filter",
            params={
                "filterId": filter_id,
                "resourceType": resource_type,
                "name": name,
                "nameLike": name_like,
                "owner": owner,
                "itemCount": item_count,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
            },
        )

    def get_single_filter(
        self,
        id: str,
        *,
        item_count: bool | None = None,
    ) -> Any:
        """Get Single Filter.

        Retrieves a single filter by id, according to the `Filter` interface in the
        engine.

        GET /filter/{id}
        """
        return self._call(
            "GET",
            "/filter/{id}",
            path={"id": id},
            params={
                "itemCount": item_count,
            },
        )

    def post_execute_filter_count(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Execute Filter Count (POST).

        Executes the saved query of the filter by id and returns the count. This
        method is slightly more powerful then the Get Execute Filter Count method
        because it allows to extend the saved query of the filter.

        POST /filter/{id}/count
        """
        return self._call(
            "POST",
            "/filter/{id}/count",
            path={"id": id},
            body=body,
        )

    def post_execute_filter_list(
        self,
        id: str,
        *,
        first_result: int | None = None,
        max_results: int | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Execute Filter List (POST).

        Executes the saved query of the filter by id and returns the result list.
        This method is slightly more powerful then the Get Execute FilterList method
        because it allows to extend the saved query of the filter.

        POST /filter/{id}/list
        """
        return self._call(
            "POST",
            "/filter/{id}/list",
            path={"id": id},
            params={
                "firstResult": first_result,
                "maxResults": max_results,
            },
            body=body,
        )

    def post_execute_filter_single_result(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Execute Filter Single Result (POST).

        Executes the saved query of the filter by id and returns the single result.
        This method is slightly more powerful then the Get Execute Filter Single
        Result method because it allows to extend the saved query of the filter.

        POST /filter/{id}/singleResult
        """
        return self._call(
            "POST",
            "/filter/{id}/singleResult",
            path={"id": id},
            body=body,
        )

    def update_filter(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Update Filter.

        Updates an existing filter. Request body: an object with resourceType, name,
        owner, query, properties.

        PUT /filter/{id}
        """
        return self._call(
            "PUT",
            "/filter/{id}",
            path={"id": id},
            body=body,
        )
