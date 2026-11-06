"""Operaton / Camunda 7 engine REST: the History Cleanup operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7HistoryCleanup(ApiClientBase):
    """History Cleanup: 4 engine REST operation(s)."""

    def cleanup_async(
        self,
        *,
        immediately_due: bool | None = None,
    ) -> Any:
        """Clean up history (POST).

        Schedules asynchronous history cleanup (See History cleanup). **Note:** This
        endpoint will return at most a single history cleanup job. Since version
        `7.9.0` it is possible to configure multiple parallel history cleanup jobs.
        Use `GET /history/cleanup/jobs` to find all the available history cleanup
        jobs.

        POST /history/cleanup
        """
        return self._call(
            "POST",
            "/history/cleanup",
            params={
                "immediatelyDue": immediately_due,
            },
        )

    def find_cleanup_job(
        self,
    ) -> Any:
        """Find clean up history job (GET).

        **Deprecated!** Use `GET /history/cleanup/jobs` instead. Finds history
        cleanup job (See History cleanup).

        GET /history/cleanup/job
        """
        return self._call(
            "GET",
            "/history/cleanup/job",
        )

    def find_cleanup_jobs(
        self,
    ) -> Any:
        """Find clean up history jobs (GET).

        Finds history cleanup jobs (See History cleanup).

        GET /history/cleanup/jobs
        """
        return self._call(
            "GET",
            "/history/cleanup/jobs",
        )

    def get_history_cleanup_configuration(
        self,
    ) -> Any:
        """Get History Cleanup Configuration.

        Retrieves history cleanup batch window configuration (See History cleanup).

        GET /history/cleanup/configuration
        """
        return self._call(
            "GET",
            "/history/cleanup/configuration",
        )
