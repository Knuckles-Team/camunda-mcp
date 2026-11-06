"""Operaton / Camunda 7 engine REST: the Task Comment operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7TaskComment(ApiClientBase):
    """Task Comment: 6 engine REST operation(s)."""

    def create_comment(
        self,
        id: str,
        *,
        body: Any = None,
    ) -> Any:
        """Create.

        Creates a comment for a task by id.

        POST /task/{id}/comment/create
        """
        return self._call(
            "POST",
            "/task/{id}/comment/create",
            path={"id": id},
            body=body,
        )

    def delete_task_comment(
        self,
        id: str,
        comment_id: str,
    ) -> Any:
        """Delete.

        Removes a comment from a task by id.

        DELETE /task/{id}/comment/{commentId}
        """
        return self._call(
            "DELETE",
            "/task/{id}/comment/{commentId}",
            path={"id": id, "commentId": comment_id},
        )

    def delete_task_comments(
        self,
        id: str,
    ) -> Any:
        """Delete Task Comments.

        Deletes all comments of a task by task id.

        DELETE /task/{id}/comment
        """
        return self._call(
            "DELETE",
            "/task/{id}/comment",
            path={"id": id},
        )

    def get_comment(
        self,
        id: str,
        comment_id: str,
    ) -> Any:
        """Get.

        Retrieves a task comment by task id and comment id.

        GET /task/{id}/comment/{commentId}
        """
        return self._call(
            "GET",
            "/task/{id}/comment/{commentId}",
            path={"id": id, "commentId": comment_id},
        )

    def get_comments(
        self,
        id: str,
    ) -> Any:
        """Get List.

        Gets the comments for a task by id.

        GET /task/{id}/comment
        """
        return self._call(
            "GET",
            "/task/{id}/comment",
            path={"id": id},
        )

    def update_task_comment(
        self,
        id: str,
        *,
        body: Any = None,
    ) -> Any:
        """Update.

        Updates a Comment.

        PUT /task/{id}/comment
        """
        return self._call(
            "PUT",
            "/task/{id}/comment",
            path={"id": id},
            body=body,
        )
