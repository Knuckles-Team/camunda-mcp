"""Operaton / Camunda 7 engine REST: the Tenant operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7Tenant(ApiClientBase):
    """Tenant: 10 engine REST operation(s)."""

    def create_group_membership(
        self,
        id: str,
        group_id: str,
    ) -> Any:
        """Create Tenant Group Membership.

        Creates a membership between a tenant and a group.

        PUT /tenant/{id}/group-members/{groupId}
        """
        return self._call(
            "PUT",
            "/tenant/{id}/group-members/{groupId}",
            path={"id": id, "groupId": group_id},
        )

    def create_tenant(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Create Tenant.

        Create a new tenant. Request body: an object with id, name.

        POST /tenant/create
        """
        return self._call(
            "POST",
            "/tenant/create",
            body=body,
        )

    def create_user_membership(
        self,
        id: str,
        user_id: str,
    ) -> Any:
        """Create Tenant User Membership.

        Creates a membership between a tenant and an user.

        PUT /tenant/{id}/user-members/{userId}
        """
        return self._call(
            "PUT",
            "/tenant/{id}/user-members/{userId}",
            path={"id": id, "userId": user_id},
        )

    def delete_group_membership(
        self,
        id: str,
        group_id: str,
    ) -> Any:
        """Create Tenant Group Membership.

        Creates a membership between a tenant and a group.

        DELETE /tenant/{id}/group-members/{groupId}
        """
        return self._call(
            "DELETE",
            "/tenant/{id}/group-members/{groupId}",
            path={"id": id, "groupId": group_id},
        )

    def delete_tenant(
        self,
        id: str,
    ) -> Any:
        """Delete Tenant.

        Deletes a tenant by id.

        DELETE /tenant/{id}
        """
        return self._call(
            "DELETE",
            "/tenant/{id}",
            path={"id": id},
        )

    def delete_user_membership(
        self,
        id: str,
        user_id: str,
    ) -> Any:
        """Delete a Tenant User Membership.

        Deletes a membership between a tenant and an user.

        DELETE /tenant/{id}/user-members/{userId}
        """
        return self._call(
            "DELETE",
            "/tenant/{id}/user-members/{userId}",
            path={"id": id, "userId": user_id},
        )

    def get_tenant(
        self,
        id: str,
    ) -> Any:
        """Get Tenant.

        Retrieves a tenant.

        GET /tenant/{id}
        """
        return self._call(
            "GET",
            "/tenant/{id}",
            path={"id": id},
        )

    def get_tenant_count(
        self,
        *,
        id: str | None = None,
        name: str | None = None,
        name_like: str | None = None,
        user_member: str | None = None,
        group_member: str | None = None,
        including_groups_of_user: bool | None = None,
    ) -> Any:
        """Get Tenant Count.

        Query for tenants using a list of parameters and retrieves the count.

        GET /tenant/count
        """
        return self._call(
            "GET",
            "/tenant/count",
            params={
                "id": id,
                "name": name,
                "nameLike": name_like,
                "userMember": user_member,
                "groupMember": group_member,
                "includingGroupsOfUser": including_groups_of_user,
            },
        )

    def query_tenants(
        self,
        *,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
        id: str | None = None,
        name: str | None = None,
        name_like: str | None = None,
        user_member: str | None = None,
        group_member: str | None = None,
        including_groups_of_user: bool | None = None,
    ) -> Any:
        """Get Tenants.

        Query for a list of tenants using a list of parameters. The size of the
        result set can be retrieved by using the Get Tenant Count method.

        GET /tenant
        """
        return self._call(
            "GET",
            "/tenant",
            params={
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
                "id": id,
                "name": name,
                "nameLike": name_like,
                "userMember": user_member,
                "groupMember": group_member,
                "includingGroupsOfUser": including_groups_of_user,
            },
        )

    def update_tenant(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Update Tenant.

        Updates a given tenant. Request body: an object with id, name.

        PUT /tenant/{id}
        """
        return self._call(
            "PUT",
            "/tenant/{id}",
            path={"id": id},
            body=body,
        )
