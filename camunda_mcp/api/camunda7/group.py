"""Operaton / Camunda 7 engine REST: the Group operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7Group(ApiClientBase):
    """Group: 10 engine REST operation(s)."""

    def create_group(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Create Group.

        Creates a new group. Request body: an object with id, name, type.

        POST /group/create
        """
        return self._call(
            "POST",
            "/group/create",
            body=body,
        )

    def create_group_member(
        self,
        id: str,
        user_id: str,
    ) -> Any:
        """Create Group Member.

        Adds a member to a group.

        PUT /group/{id}/members/{userId}
        """
        return self._call(
            "PUT",
            "/group/{id}/members/{userId}",
            path={"id": id, "userId": user_id},
        )

    def delete_group(
        self,
        id: str,
    ) -> Any:
        """Delete Group.

        Deletes a group by id.

        DELETE /group/{id}
        """
        return self._call(
            "DELETE",
            "/group/{id}",
            path={"id": id},
        )

    def delete_group_member(
        self,
        id: str,
        user_id: str,
    ) -> Any:
        """Delete a Group Member.

        Removes a member from a group.

        DELETE /group/{id}/members/{userId}
        """
        return self._call(
            "DELETE",
            "/group/{id}/members/{userId}",
            path={"id": id, "userId": user_id},
        )

    def get_group(
        self,
        id: str,
    ) -> Any:
        """Get Group.

        Retrieves a group by id.

        GET /group/{id}
        """
        return self._call(
            "GET",
            "/group/{id}",
            path={"id": id},
        )

    def get_group_count(
        self,
        *,
        id: str | None = None,
        id_in: str | None = None,
        name: str | None = None,
        name_like: str | None = None,
        type: str | None = None,
        member: str | None = None,
        member_of_tenant: str | None = None,
    ) -> Any:
        """Get List Count.

        Queries for groups using a list of parameters and retrieves the count.

        GET /group/count
        """
        return self._call(
            "GET",
            "/group/count",
            params={
                "id": id,
                "idIn": id_in,
                "name": name,
                "nameLike": name_like,
                "type": type,
                "member": member,
                "memberOfTenant": member_of_tenant,
            },
        )

    def get_query_groups(
        self,
        *,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
        id: str | None = None,
        id_in: str | None = None,
        name: str | None = None,
        name_like: str | None = None,
        type: str | None = None,
        member: str | None = None,
        member_of_tenant: str | None = None,
    ) -> Any:
        """Get List.

        Queries for a list of groups using a list of parameters. The size of the
        result set can be retrieved by using the Get Group Count method.

        GET /group
        """
        return self._call(
            "GET",
            "/group",
            params={
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
                "id": id,
                "idIn": id_in,
                "name": name,
                "nameLike": name_like,
                "type": type,
                "member": member,
                "memberOfTenant": member_of_tenant,
            },
        )

    def post_query_groups(
        self,
        *,
        first_result: int | None = None,
        max_results: int | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Get List (POST).

        Queries for a list of groups using a list of parameters. The size of the
        result set can be retrieved by using the Get Group Count (POST) method.
        Request body: an object with id, idIn, name, nameLike, type, member,
        memberOfTenant, sorting.

        POST /group
        """
        return self._call(
            "POST",
            "/group",
            params={
                "firstResult": first_result,
                "maxResults": max_results,
            },
            body=body,
        )

    def query_group_count(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Get List Count (POST).

        Queries for groups using a list of parameters and retrieves the count.
        Request body: an object with id, idIn, name, nameLike, type, member,
        memberOfTenant, sorting.

        POST /group/count
        """
        return self._call(
            "POST",
            "/group/count",
            body=body,
        )

    def update_group(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Update Group.

        Updates a given group by id. Request body: an object with id, name, type.

        PUT /group/{id}
        """
        return self._call(
            "PUT",
            "/group/{id}",
            path={"id": id},
            body=body,
        )
