"""Operaton / Camunda 7 engine REST: the Process Instance Comment operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7ProcessInstanceComment(ApiClientBase):
    """Process Instance Comment: 4 engine REST operation(s)."""

    def delete_process_instance_comment(
        self,
        id: str,
        comment_id: str,
    ) -> Any:
        """Delete.

        Removes a comment from a process instance by id.

        DELETE /process-instance/{id}/comment/{commentId}
        """
        return self._call(
            "DELETE",
            "/process-instance/{id}/comment/{commentId}",
            path={"id": id, "commentId": comment_id},
        )

    def delete_process_instance_comments(
        self,
        id: str,
    ) -> Any:
        """Delete ProcessInstance Comments.

        Deletes all comments of a process instance by id.

        DELETE /process-instance/{id}/comment
        """
        return self._call(
            "DELETE",
            "/process-instance/{id}/comment",
            path={"id": id},
        )

    def get_process_instance_comments(
        self,
        id: str,
    ) -> Any:
        """Get Process Instance Comments.

        Gets the comments for a process instance by id.

        GET /process-instance/{id}/comment
        """
        return self._call(
            "GET",
            "/process-instance/{id}/comment",
            path={"id": id},
        )

    def update_process_instance_comment(
        self,
        id: str,
        *,
        body: Any = None,
    ) -> Any:
        """Update.

        Updates a Comment.

        PUT /process-instance/{id}/comment
        """
        return self._call(
            "PUT",
            "/process-instance/{id}/comment",
            path={"id": id},
            body=body,
        )
