"""Operaton / Camunda 7 engine REST: the Authorization operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7Authorization(ApiClientBase):
    """Authorization: 7 engine REST operation(s)."""

    def create_authorization(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Create a New Authorization.

        Creates a new authorization. Request body: an object with type, permissions,
        userId, groupId, resourceType, resourceId.

        POST /authorization/create
        """
        return self._call(
            "POST",
            "/authorization/create",
            body=body,
        )

    def delete_authorization(
        self,
        id: str,
    ) -> Any:
        """Delete Authorization.

        Deletes an authorization by id.

        DELETE /authorization/{id}
        """
        return self._call(
            "DELETE",
            "/authorization/{id}",
            path={"id": id},
        )

    def get_authorization(
        self,
        id: str,
    ) -> Any:
        """Get Authorization.

        Retrieves an authorization by id.

        GET /authorization/{id}
        """
        return self._call(
            "GET",
            "/authorization/{id}",
            path={"id": id},
        )

    def get_authorization_count(
        self,
        *,
        id: str | None = None,
        type: int | None = None,
        user_id_in: str | None = None,
        group_id_in: str | None = None,
        resource_type: int | None = None,
        resource_id: str | None = None,
    ) -> Any:
        """Get Authorization Count.

        Queries for authorizations using a list of parameters and retrieves the
        count.

        GET /authorization/count
        """
        return self._call(
            "GET",
            "/authorization/count",
            params={
                "id": id,
                "type": type,
                "userIdIn": user_id_in,
                "groupIdIn": group_id_in,
                "resourceType": resource_type,
                "resourceId": resource_id,
            },
        )

    def is_user_authorized(
        self,
        *,
        permission_name: str,
        resource_name: str,
        resource_type: int,
        resource_id: str | None = None,
        user_id: str | None = None,
    ) -> Any:
        """Perform an Authorization Check.

        Performs an authorization check for the currently authenticated user.

        GET /authorization/check
        """
        return self._call(
            "GET",
            "/authorization/check",
            params={
                "permissionName": permission_name,
                "resourceName": resource_name,
                "resourceType": resource_type,
                "resourceId": resource_id,
                "userId": user_id,
            },
        )

    def query_authorizations(
        self,
        *,
        id: str | None = None,
        type: int | None = None,
        user_id_in: str | None = None,
        group_id_in: str | None = None,
        resource_type: int | None = None,
        resource_id: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
    ) -> Any:
        """Get Authorizations.

        Queries for a list of authorizations using a list of parameters. The size of
        the result set can be retrieved by using the Get Authorization Count method.

        GET /authorization
        """
        return self._call(
            "GET",
            "/authorization",
            params={
                "id": id,
                "type": type,
                "userIdIn": user_id_in,
                "groupIdIn": group_id_in,
                "resourceType": resource_type,
                "resourceId": resource_id,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
            },
        )

    def update_authorization(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Update an Authorization.

        Updates an authorization by id. Request body: an object with permissions,
        userId, groupId, resourceType, resourceId.

        PUT /authorization/{id}
        """
        return self._call(
            "PUT",
            "/authorization/{id}",
            path={"id": id},
            body=body,
        )
