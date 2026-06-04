"""Camunda 7 Engine REST API wrapper.

Comprehensive client for the Camunda Platform 7 Engine REST API (default base
path ``/engine-rest``). Covers process definitions, process instances, user
tasks, deployments, history, external tasks, messaging, incidents and jobs.
"""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7Api(ApiClientBase):
    """Full client for a Camunda 7 Engine REST API."""

    # ------------------------------------------------------------------ #
    # Process definitions
    # ------------------------------------------------------------------ #
    def list_process_definitions(self, params: dict[str, Any] | None = None) -> Any:
        """List process definitions, optionally filtered (e.g. key, latestVersion)."""
        return self.request(
            "GET", "process-definition", params=params, accept="application/json"
        )

    def get_process_definition(
        self, id: str | None = None, key: str | None = None
    ) -> Any:
        """Get a process definition by id, or the latest version by key."""
        endpoint = (
            f"process-definition/{id}"
            if id
            else f"process-definition/key/{key}"
        )
        return self.request("GET", endpoint, accept="application/json")

    def get_process_definition_xml(
        self, id: str | None = None, key: str | None = None
    ) -> Any:
        """Get the BPMN 2.0 XML for a process definition (by id or key)."""
        endpoint = (
            f"process-definition/{id}/xml"
            if id
            else f"process-definition/key/{key}/xml"
        )
        return self.request("GET", endpoint, accept="application/json")

    def start_process_instance(
        self,
        id: str | None = None,
        key: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Start a process instance by definition id or key.

        ``body`` may contain ``variables``, ``businessKey``, etc.
        """
        endpoint = (
            f"process-definition/{id}/start"
            if id
            else f"process-definition/key/{key}/start"
        )
        return self.request(
            "POST", endpoint, json=body or {}, content_type="application/json"
        )

    def get_process_definition_statistics(
        self, params: dict[str, Any] | None = None
    ) -> Any:
        """Get instance statistics aggregated by process definition."""
        return self.request(
            "GET",
            "process-definition/statistics",
            params=params,
            accept="application/json",
        )

    def suspend_process_definition(
        self,
        id: str | None = None,
        key: str | None = None,
        suspended: bool = True,
        include_instances: bool = True,
    ) -> Any:
        """Suspend or activate a process definition (and optionally its instances)."""
        body = {"suspended": suspended, "includeProcessInstances": include_instances}
        endpoint = (
            f"process-definition/{id}/suspended"
            if id
            else f"process-definition/key/{key}/suspended"
        )
        return self.request(
            "PUT", endpoint, json=body, content_type="application/json"
        )

    # ------------------------------------------------------------------ #
    # Process instances
    # ------------------------------------------------------------------ #
    def list_process_instances(self, params: dict[str, Any] | None = None) -> Any:
        """List running process instances, optionally filtered."""
        return self.request(
            "GET", "process-instance", params=params, accept="application/json"
        )

    def get_process_instance(self, instance_id: str) -> Any:
        """Get a running process instance by id."""
        return self.request(
            "GET", f"process-instance/{instance_id}", accept="application/json"
        )

    def delete_process_instance(
        self, instance_id: str, params: dict[str, Any] | None = None
    ) -> Any:
        """Delete (cancel) a running process instance."""
        return self.request(
            "DELETE", f"process-instance/{instance_id}", params=params
        )

    def get_process_instance_variables(self, instance_id: str) -> Any:
        """Get all variables of a process instance."""
        return self.request(
            "GET",
            f"process-instance/{instance_id}/variables",
            accept="application/json",
        )

    def modify_process_instance_variables(
        self, instance_id: str, body: dict[str, Any]
    ) -> Any:
        """Modify (add/update/delete) variables of a process instance.

        ``body`` is ``{"modifications": {...}, "deletions": [...]}``.
        """
        return self.request(
            "POST",
            f"process-instance/{instance_id}/variables",
            json=body,
            content_type="application/json",
        )

    def suspend_process_instance(
        self, instance_id: str, suspended: bool = True
    ) -> Any:
        """Suspend or activate a single process instance."""
        return self.request(
            "PUT",
            f"process-instance/{instance_id}/suspended",
            json={"suspended": suspended},
            content_type="application/json",
        )

    # ------------------------------------------------------------------ #
    # User tasks
    # ------------------------------------------------------------------ #
    def list_tasks(self, params: dict[str, Any] | None = None) -> Any:
        """List user tasks, optionally filtered (assignee, processInstanceId, ...)."""
        return self.request("GET", "task", params=params, accept="application/json")

    def get_task(self, task_id: str) -> Any:
        """Get a single user task by id."""
        return self.request("GET", f"task/{task_id}", accept="application/json")

    def claim_task(self, task_id: str, user_id: str) -> Any:
        """Claim a task for a user."""
        return self.request(
            "POST",
            f"task/{task_id}/claim",
            json={"userId": user_id},
            content_type="application/json",
        )

    def unclaim_task(self, task_id: str) -> Any:
        """Reset a task's assignee (unclaim)."""
        return self.request("POST", f"task/{task_id}/unclaim")

    def set_task_assignee(self, task_id: str, user_id: str) -> Any:
        """Set the assignee of a task."""
        return self.request(
            "POST",
            f"task/{task_id}/assignee",
            json={"userId": user_id},
            content_type="application/json",
        )

    def complete_task(
        self, task_id: str, variables: dict[str, Any] | None = None
    ) -> Any:
        """Complete a user task, optionally passing variables."""
        return self.request(
            "POST",
            f"task/{task_id}/complete",
            json={"variables": variables or {}},
            content_type="application/json",
        )

    def get_task_variables(self, task_id: str) -> Any:
        """Get all variables visible from a task."""
        return self.request(
            "GET", f"task/{task_id}/variables", accept="application/json"
        )

    def set_task_variables(self, task_id: str, body: dict[str, Any]) -> Any:
        """Update or delete task variables (``modifications``/``deletions``)."""
        return self.request(
            "POST",
            f"task/{task_id}/variables",
            json=body,
            content_type="application/json",
        )

    # ------------------------------------------------------------------ #
    # Deployments
    # ------------------------------------------------------------------ #
    def create_deployment(
        self,
        files: dict[str, Any],
        deployment_name: str = "deployment",
        data: dict[str, Any] | None = None,
    ) -> Any:
        """Create a deployment via multipart upload.

        ``files`` is a requests-style files dict, e.g.
        ``{"process.bpmn": ("process.bpmn", b"<xml>", "text/xml")}``.
        ``data`` holds extra form fields (e.g. ``enable-duplicate-filtering``).
        """
        form: dict[str, Any] = {"deployment-name": deployment_name}
        if data:
            form.update(data)
        return self.request("POST", "deployment/create", data=form, files=files)

    def list_deployments(self, params: dict[str, Any] | None = None) -> Any:
        """List deployments."""
        return self.request(
            "GET", "deployment", params=params, accept="application/json"
        )

    def get_deployment(self, deployment_id: str) -> Any:
        """Get a deployment by id."""
        return self.request(
            "GET", f"deployment/{deployment_id}", accept="application/json"
        )

    def delete_deployment(
        self, deployment_id: str, params: dict[str, Any] | None = None
    ) -> Any:
        """Delete a deployment (``cascade``, ``skipCustomListeners`` via params)."""
        return self.request("DELETE", f"deployment/{deployment_id}", params=params)

    # ------------------------------------------------------------------ #
    # History
    # ------------------------------------------------------------------ #
    def list_historic_process_instances(
        self, params: dict[str, Any] | None = None
    ) -> Any:
        """Query historic process instances."""
        return self.request(
            "GET",
            "history/process-instance",
            params=params,
            accept="application/json",
        )

    def list_historic_activity_instances(
        self, params: dict[str, Any] | None = None
    ) -> Any:
        """Query historic activity instances."""
        return self.request(
            "GET",
            "history/activity-instance",
            params=params,
            accept="application/json",
        )

    def list_historic_variables(self, params: dict[str, Any] | None = None) -> Any:
        """Query historic variable instances."""
        return self.request(
            "GET",
            "history/variable-instance",
            params=params,
            accept="application/json",
        )

    # ------------------------------------------------------------------ #
    # External tasks
    # ------------------------------------------------------------------ #
    def fetch_and_lock(self, body: dict[str, Any]) -> Any:
        """Fetch and lock external tasks for a worker.

        ``body`` is ``{"workerId": ..., "maxTasks": ..., "topics": [...]}``.
        """
        return self.request(
            "POST",
            "external-task/fetchAndLock",
            json=body,
            content_type="application/json",
        )

    def complete_external_task(self, task_id: str, body: dict[str, Any]) -> Any:
        """Complete an external task (``workerId``, ``variables``)."""
        return self.request(
            "POST",
            f"external-task/{task_id}/complete",
            json=body,
            content_type="application/json",
        )

    def handle_external_task_failure(
        self, task_id: str, body: dict[str, Any]
    ) -> Any:
        """Report a failure for an external task (``workerId``, ``errorMessage``)."""
        return self.request(
            "POST",
            f"external-task/{task_id}/failure",
            json=body,
            content_type="application/json",
        )

    def handle_external_task_bpmn_error(
        self, task_id: str, body: dict[str, Any]
    ) -> Any:
        """Raise a BPMN error from an external task (``workerId``, ``errorCode``)."""
        return self.request(
            "POST",
            f"external-task/{task_id}/bpmnError",
            json=body,
            content_type="application/json",
        )

    # ------------------------------------------------------------------ #
    # Messaging
    # ------------------------------------------------------------------ #
    def correlate_message(self, body: dict[str, Any]) -> Any:
        """Correlate a message to one or more process instances.

        ``body`` is ``{"messageName": ..., "businessKey": ..., "processVariables": ...}``.
        """
        return self.request(
            "POST", "message", json=body, content_type="application/json"
        )

    def throw_signal(self, body: dict[str, Any]) -> Any:
        """Throw a signal (``{"name": ..., "variables": ...}``)."""
        return self.request(
            "POST", "signal", json=body, content_type="application/json"
        )

    # ------------------------------------------------------------------ #
    # Incidents
    # ------------------------------------------------------------------ #
    def list_incidents(self, params: dict[str, Any] | None = None) -> Any:
        """List incidents, optionally filtered."""
        return self.request(
            "GET", "incident", params=params, accept="application/json"
        )

    def get_incident(self, incident_id: str) -> Any:
        """Get a single incident by id."""
        return self.request(
            "GET", f"incident/{incident_id}", accept="application/json"
        )

    def resolve_incident(self, incident_id: str) -> Any:
        """Resolve (delete) an incident."""
        return self.request("DELETE", f"incident/{incident_id}")

    # ------------------------------------------------------------------ #
    # Jobs
    # ------------------------------------------------------------------ #
    def list_jobs(self, params: dict[str, Any] | None = None) -> Any:
        """List jobs, optionally filtered."""
        return self.request("GET", "job", params=params, accept="application/json")

    def execute_job(self, job_id: str) -> Any:
        """Execute a job synchronously."""
        return self.request("POST", f"job/{job_id}/execute")

    def set_job_retries(self, job_id: str, retries: int) -> Any:
        """Set the number of retries for a job."""
        return self.request(
            "PUT",
            f"job/{job_id}/retries",
            json={"retries": retries},
            content_type="application/json",
        )
