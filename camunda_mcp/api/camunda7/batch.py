"""Operaton / Camunda 7 engine REST: the Batch operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7Batch(ApiClientBase):
    """Batch: 7 engine REST operation(s)."""

    def delete_batch(
        self,
        id: str,
        *,
        cascade: bool | None = None,
    ) -> Any:
        """Delete.

        Deletes a batch by id, including all related jobs and job definitions.
        Optionally also deletes the batch history.

        DELETE /batch/{id}
        """
        return self._call(
            "DELETE",
            "/batch/{id}",
            path={"id": id},
            params={
                "cascade": cascade,
            },
        )

    def get_batch(
        self,
        id: str,
    ) -> Any:
        """Get.

        Retrieves a batch by id, according to the Batch interface in the engine.

        GET /batch/{id}
        """
        return self._call(
            "GET",
            "/batch/{id}",
            path={"id": id},
        )

    def get_batch_statistics(
        self,
        *,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
        batch_id: str | None = None,
        type: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        suspended: bool | None = None,
        created_by: str | None = None,
        started_before: str | None = None,
        started_after: str | None = None,
        with_failures: bool | None = None,
        without_failures: bool | None = None,
    ) -> Any:
        """Get Statistics.

        Queries for batch statistics that fulfill given parameters. Parameters may
        be the properties of batches, such as the id or type. The size of the result
        set can be retrieved by using the Get Batch Statistics Count method.

        GET /batch/statistics
        """
        return self._call(
            "GET",
            "/batch/statistics",
            params={
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
                "batchId": batch_id,
                "type": type,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "suspended": suspended,
                "createdBy": created_by,
                "startedBefore": started_before,
                "startedAfter": started_after,
                "withFailures": with_failures,
                "withoutFailures": without_failures,
            },
        )

    def get_batch_statistics_count(
        self,
        *,
        batch_id: str | None = None,
        type: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        suspended: bool | None = None,
        created_by: str | None = None,
        started_before: str | None = None,
        started_after: str | None = None,
        with_failures: bool | None = None,
        without_failures: bool | None = None,
    ) -> Any:
        """Get Statistics Count.

        Requests the number of batch statistics that fulfill the query criteria.
        Takes the same filtering parameters as the Get Batch Statistics method.

        GET /batch/statistics/count
        """
        return self._call(
            "GET",
            "/batch/statistics/count",
            params={
                "batchId": batch_id,
                "type": type,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "suspended": suspended,
                "createdBy": created_by,
                "startedBefore": started_before,
                "startedAfter": started_after,
                "withFailures": with_failures,
                "withoutFailures": without_failures,
            },
        )

    def get_batches(
        self,
        *,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
        batch_id: str | None = None,
        type: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        suspended: bool | None = None,
        created_by: str | None = None,
        started_before: str | None = None,
        started_after: str | None = None,
        with_failures: bool | None = None,
        without_failures: bool | None = None,
    ) -> Any:
        """Get List.

        Queries for batches that fulfill given parameters. Parameters may be the
        properties of batches, such as the id or type. The size of the result set
        can be retrieved by using the Get Batch Count method.

        GET /batch
        """
        return self._call(
            "GET",
            "/batch",
            params={
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
                "batchId": batch_id,
                "type": type,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "suspended": suspended,
                "createdBy": created_by,
                "startedBefore": started_before,
                "startedAfter": started_after,
                "withFailures": with_failures,
                "withoutFailures": without_failures,
            },
        )

    def get_batches_count(
        self,
        *,
        batch_id: str | None = None,
        type: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        suspended: bool | None = None,
        created_by: str | None = None,
        started_before: str | None = None,
        started_after: str | None = None,
        with_failures: bool | None = None,
        without_failures: bool | None = None,
    ) -> Any:
        """Get List Count.

        Requests the number of batches that fulfill the query criteria. Takes the
        same filtering parameters as the Get Batches method.

        GET /batch/count
        """
        return self._call(
            "GET",
            "/batch/count",
            params={
                "batchId": batch_id,
                "type": type,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "suspended": suspended,
                "createdBy": created_by,
                "startedBefore": started_before,
                "startedAfter": started_after,
                "withFailures": with_failures,
                "withoutFailures": without_failures,
            },
        )

    def update_batch_suspension_state(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Activate/Suspend.

        Activates or suspends a batch by id. Request body: an object with suspended.

        PUT /batch/{id}/suspended
        """
        return self._call(
            "PUT",
            "/batch/{id}/suspended",
            path={"id": id},
            body=body,
        )
