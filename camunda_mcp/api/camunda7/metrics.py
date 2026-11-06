"""Operaton / Camunda 7 engine REST: the Metrics operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7Metrics(ApiClientBase):
    """Metrics: 3 engine REST operation(s)."""

    def delete_task_metrics(
        self,
        *,
        date: str | None = None,
    ) -> Any:
        """Delete Task Worker Metrics.

        Deletes all task worker metrics prior to the given date or all if no date is
        provided.

        DELETE /metrics/task-worker
        """
        return self._call(
            "DELETE",
            "/metrics/task-worker",
            params={
                "date": date,
            },
        )

    def get_metrics(
        self,
        metrics_name: str,
        *,
        start_date: str | None = None,
        end_date: str | None = None,
    ) -> Any:
        """Get Sum.

        Retrieves the `sum` (count) for a given metric.

        GET /metrics/{metrics-name}/sum
        """
        return self._call(
            "GET",
            "/metrics/{metrics-name}/sum",
            path={"metrics-name": metrics_name},
            params={
                "startDate": start_date,
                "endDate": end_date,
            },
        )

    def interval(
        self,
        *,
        name: str | None = None,
        reporter: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
        interval: int | None = None,
        aggregate_by_reporter: str | None = None,
    ) -> Any:
        """Get Metrics in Interval.

        Retrieves a list of metrics, aggregated for a given interval.

        GET /metrics
        """
        return self._call(
            "GET",
            "/metrics",
            params={
                "name": name,
                "reporter": reporter,
                "startDate": start_date,
                "endDate": end_date,
                "firstResult": first_result,
                "maxResults": max_results,
                "interval": interval,
                "aggregateByReporter": aggregate_by_reporter,
            },
        )
