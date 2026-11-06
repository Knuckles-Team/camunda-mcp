"""Operaton / Camunda 7 engine REST: the Task Attachment operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase, upload_part


class Camunda7TaskAttachment(ApiClientBase):
    """Task Attachment: 5 engine REST operation(s)."""

    def add_attachment(
        self,
        id: str,
        *,
        attachment_name: str | None = None,
        attachment_description: str | None = None,
        attachment_type: str | None = None,
        url: str | None = None,
        content: str | None = None,
        filename: str | None = None,
    ) -> Any:
        """Create.

        Creates an attachment for a task.

        POST /task/{id}/attachment/create
        """
        return self._call(
            "POST",
            "/task/{id}/attachment/create",
            path={"id": id},
            form={
                "attachment-name": attachment_name,
                "attachment-description": attachment_description,
                "attachment-type": attachment_type,
                "url": url,
            },
            files=upload_part("content", content, filename),
        )

    def delete_attachment(
        self,
        id: str,
        attachment_id: str,
    ) -> Any:
        """Delete.

        Removes an attachment from a task by id.

        DELETE /task/{id}/attachment/{attachmentId}
        """
        return self._call(
            "DELETE",
            "/task/{id}/attachment/{attachmentId}",
            path={"id": id, "attachmentId": attachment_id},
        )

    def get_attachment(
        self,
        id: str,
        attachment_id: str,
    ) -> Any:
        """Get.

        Retrieves a task attachment by task id and attachment id.

        GET /task/{id}/attachment/{attachmentId}
        """
        return self._call(
            "GET",
            "/task/{id}/attachment/{attachmentId}",
            path={"id": id, "attachmentId": attachment_id},
        )

    def get_attachment_data(
        self,
        id: str,
        attachment_id: str,
    ) -> Any:
        """Get (Binary).

        Retrieves the binary content of a task attachment by task id and attachment
        id.

        GET /task/{id}/attachment/{attachmentId}/data
        """
        return self._call(
            "GET",
            "/task/{id}/attachment/{attachmentId}/data",
            path={"id": id, "attachmentId": attachment_id},
        )

    def get_attachments(
        self,
        id: str,
    ) -> Any:
        """Get List.

        Gets the attachments for a task.

        GET /task/{id}/attachment
        """
        return self._call(
            "GET",
            "/task/{id}/attachment",
            path={"id": id},
        )
