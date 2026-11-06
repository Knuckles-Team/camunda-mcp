"""Operaton / Camunda 7 engine REST: the Historic Batch operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7HistoricBatch(ApiClientBase):
    """Historic Batch: 7 engine REST operation(s)."""

    def delete_historic_batch(
        self,
        id: str,
    ) -> Any:
        """Delete Historic Batch.

        Deletes a historic batch by id, including related historic job logs.

        DELETE /history/batch/{id}
        """
        return self._call(
            "DELETE",
            "/history/batch/{id}",
            path={"id": id},
        )

    def get_cleanable_historic_batches_report(
        self,
        *,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
    ) -> Any:
        """Get Cleanable Batch Report.

        Retrieves a report about a historic batch operations relevant to history
        cleanup (see History cleanup ) so that you can tune the history time to
        live. These reports include the count of the finished batches, cleanable
        batches and type of the batch. The size of the result set can be retrieved
        by using the Get Cleanable Batch Report Count method.

        GET /history/batch/cleanable-batch-report
        """
        return self._call(
            "GET",
            "/history/batch/cleanable-batch-report",
            params={
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
            },
        )

    def get_cleanable_historic_batches_report_count(
        self,
    ) -> Any:
        """Get Cleanable Batch Report Count.

        Queries for the number of report results about a historic batch operations
        relevant to history cleanup (see History cleanup ). Takes the same
        parameters as the Get Cleanable Batch Report method.

        GET /history/batch/cleanable-batch-report/count
        """
        return self._call(
            "GET",
            "/history/batch/cleanable-batch-report/count",
        )

    def get_historic_batch(
        self,
        id: str,
    ) -> Any:
        """Get Historic Batch.

        Retrieves a historic batch by id, according to the `HistoricBatch` interface
        in the engine.

        GET /history/batch/{id}
        """
        return self._call(
            "GET",
            "/history/batch/{id}",
            path={"id": id},
        )

    def get_historic_batches(
        self,
        *,
        batch_id: str | None = None,
        type: str | None = None,
        completed: bool | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
    ) -> Any:
        """Get Historic Batches.

        Queries for historic batches that fulfill given parameters. Parameters may
        be the properties of batches, such as the id or type. The size of the result
        set can be retrieved by using the Get Historic Batch Count method.

        GET /history/batch
        """
        return self._call(
            "GET",
            "/history/batch",
            params={
                "batchId": batch_id,
                "type": type,
                "completed": completed,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
            },
        )

    def get_historic_batches_count(
        self,
        *,
        batch_id: str | None = None,
        type: str | None = None,
        completed: bool | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
    ) -> Any:
        """Get Historic Batch Count.

        Requests the number of historic batches that fulfill the query criteria.
        Takes the same filtering parameters as the Get Historic Batches method.

        GET /history/batch/count
        """
        return self._call(
            "GET",
            "/history/batch/count",
            params={
                "batchId": batch_id,
                "type": type,
                "completed": completed,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
            },
        )

    def set_removal_time_async_historic_batch(
        self,
        *,
        body: Any = None,
    ) -> Any:
        """Set Removal Time Async (POST).

        Sets the removal time to multiple historic batches asynchronously (batch).
        At least __historicBatchIds__ or __historicBatchQuery__ has to be provided.
        If both are provided, all instances matching query criterion and instances
        from the list will be updated with a removal time.

        POST /history/batch/set-removal-time
        """
        return self._call(
            "POST",
            "/history/batch/set-removal-time",
            body=body,
        )
