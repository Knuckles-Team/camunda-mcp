"""Operaton / Camunda 7 engine REST: the Task Identity Link operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7TaskIdentityLink(ApiClientBase):
    """Task Identity Link: 3 engine REST operation(s)."""

    def add_identity_link(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Add.

        Adds an identity link to a task by id. Can be used to link any user or group
        to a task and specify a relation. Request body: an object with userId,
        groupId, type.

        POST /task/{id}/identity-links
        """
        return self._call(
            "POST",
            "/task/{id}/identity-links",
            path={"id": id},
            body=body,
        )

    def delete_identity_link(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Delete.

        Removes an identity link from a task by id Request body: an object with
        userId, groupId, type.

        POST /task/{id}/identity-links/delete
        """
        return self._call(
            "POST",
            "/task/{id}/identity-links/delete",
            path={"id": id},
            body=body,
        )

    def get_identity_links(
        self,
        id: str,
        *,
        type: str | None = None,
    ) -> Any:
        """Get List.

        Gets the identity links for a task by id, which are the users and groups
        that are in *some* relation to it (including assignee and owner).

        GET /task/{id}/identity-links
        """
        return self._call(
            "GET",
            "/task/{id}/identity-links",
            path={"id": id},
            params={
                "type": type,
            },
        )
