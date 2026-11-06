"""Operaton / Camunda 7 engine REST: the Historic Job Log operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7HistoricJobLog(ApiClientBase):
    """Historic Job Log: 6 engine REST operation(s)."""

    def get_historic_job_log(
        self,
        id: str,
    ) -> Any:
        """Get Job Log.

        Retrieves a historic job log by id.

        GET /history/job-log/{id}
        """
        return self._call(
            "GET",
            "/history/job-log/{id}",
            path={"id": id},
        )

    def get_historic_job_logs(
        self,
        *,
        log_id: str | None = None,
        job_id: str | None = None,
        job_exception_message: str | None = None,
        job_definition_id: str | None = None,
        job_definition_type: str | None = None,
        job_definition_configuration: str | None = None,
        activity_id_in: str | None = None,
        failed_activity_id_in: str | None = None,
        execution_id_in: str | None = None,
        process_instance_id: str | None = None,
        process_definition_id: str | None = None,
        process_definition_key: str | None = None,
        deployment_id: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        hostname: str | None = None,
        job_priority_lower_than_or_equals: int | None = None,
        job_priority_higher_than_or_equals: int | None = None,
        creation_log: bool | None = None,
        failure_log: bool | None = None,
        success_log: bool | None = None,
        deletion_log: bool | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
    ) -> Any:
        """Get Job Logs.

        Queries for historic job logs that fulfill the given parameters. The size of
        the result set can be retrieved by using the Get Job Log Count method.

        GET /history/job-log
        """
        return self._call(
            "GET",
            "/history/job-log",
            params={
                "logId": log_id,
                "jobId": job_id,
                "jobExceptionMessage": job_exception_message,
                "jobDefinitionId": job_definition_id,
                "jobDefinitionType": job_definition_type,
                "jobDefinitionConfiguration": job_definition_configuration,
                "activityIdIn": activity_id_in,
                "failedActivityIdIn": failed_activity_id_in,
                "executionIdIn": execution_id_in,
                "processInstanceId": process_instance_id,
                "processDefinitionId": process_definition_id,
                "processDefinitionKey": process_definition_key,
                "deploymentId": deployment_id,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "hostname": hostname,
                "jobPriorityLowerThanOrEquals": job_priority_lower_than_or_equals,
                "jobPriorityHigherThanOrEquals": job_priority_higher_than_or_equals,
                "creationLog": creation_log,
                "failureLog": failure_log,
                "successLog": success_log,
                "deletionLog": deletion_log,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
            },
        )

    def get_historic_job_logs_count(
        self,
        *,
        log_id: str | None = None,
        job_id: str | None = None,
        job_exception_message: str | None = None,
        job_definition_id: str | None = None,
        job_definition_type: str | None = None,
        job_definition_configuration: str | None = None,
        activity_id_in: str | None = None,
        failed_activity_id_in: str | None = None,
        execution_id_in: str | None = None,
        process_instance_id: str | None = None,
        process_definition_id: str | None = None,
        process_definition_key: str | None = None,
        deployment_id: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        hostname: str | None = None,
        job_priority_lower_than_or_equals: int | None = None,
        job_priority_higher_than_or_equals: int | None = None,
        creation_log: bool | None = None,
        failure_log: bool | None = None,
        success_log: bool | None = None,
        deletion_log: bool | None = None,
    ) -> Any:
        """Get Job Log Count.

        Queries for the number of historic job logs that fulfill the given
        parameters. Takes the same parameters as the Get Job Logs method.

        GET /history/job-log/count
        """
        return self._call(
            "GET",
            "/history/job-log/count",
            params={
                "logId": log_id,
                "jobId": job_id,
                "jobExceptionMessage": job_exception_message,
                "jobDefinitionId": job_definition_id,
                "jobDefinitionType": job_definition_type,
                "jobDefinitionConfiguration": job_definition_configuration,
                "activityIdIn": activity_id_in,
                "failedActivityIdIn": failed_activity_id_in,
                "executionIdIn": execution_id_in,
                "processInstanceId": process_instance_id,
                "processDefinitionId": process_definition_id,
                "processDefinitionKey": process_definition_key,
                "deploymentId": deployment_id,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "hostname": hostname,
                "jobPriorityLowerThanOrEquals": job_priority_lower_than_or_equals,
                "jobPriorityHigherThanOrEquals": job_priority_higher_than_or_equals,
                "creationLog": creation_log,
                "failureLog": failure_log,
                "successLog": success_log,
                "deletionLog": deletion_log,
            },
        )

    def get_stacktrace_historic_job_log(
        self,
        id: str,
    ) -> Any:
        """Get Job Log Exception Stacktrace.

        Retrieves the corresponding exception stacktrace to the passed historic job
        log by id.

        GET /history/job-log/{id}/stacktrace
        """
        return self._call(
            "GET",
            "/history/job-log/{id}/stacktrace",
            path={"id": id},
        )

    def query_historic_job_logs(
        self,
        *,
        first_result: int | None = None,
        max_results: int | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Get Job Logs (POST).

        Queries for historic job logs that fulfill the given parameters. This method
        is slightly more powerful than the Get Job Logs method because it allows
        filtering by historic job logs values of the different types `String`,
        `Number` or `Boolean`. Request body: an object with logId, jobId,
        jobExceptionMessage, jobDefinitionId, jobDefinitionType,
        jobDefinitionConfiguration, activityIdIn, failedActivityIdIn, executionIdIn,
        processInstanceId, processDefinitionId, processDefinitionKey, deploymentId,
        tenantIdIn, withoutTenantId, hostname, jobPriorityLowerThanOrEquals,
        jobPriorityHigherThanOrEquals, creationLog, failureLog, successLog,
        deletionLog, sorting.

        POST /history/job-log
        """
        return self._call(
            "POST",
            "/history/job-log",
            params={
                "firstResult": first_result,
                "maxResults": max_results,
            },
            body=body,
        )

    def query_historic_job_logs_count(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Get Job Log Count (POST).

        Queries for the number of historic job logs that fulfill the given
        parameters. This method takes the same message body as the Get Job Logs
        (POST) method and therefore it is slightly more powerful than the Get Job
        Log Count method. Request body: an object with logId, jobId,
        jobExceptionMessage, jobDefinitionId, jobDefinitionType,
        jobDefinitionConfiguration, activityIdIn, failedActivityIdIn, executionIdIn,
        processInstanceId, processDefinitionId, processDefinitionKey, deploymentId,
        tenantIdIn, withoutTenantId, hostname, jobPriorityLowerThanOrEquals,
        jobPriorityHigherThanOrEquals, creationLog, failureLog, successLog,
        deletionLog, sorting.

        POST /history/job-log/count
        """
        return self._call(
            "POST",
            "/history/job-log/count",
            body=body,
        )
