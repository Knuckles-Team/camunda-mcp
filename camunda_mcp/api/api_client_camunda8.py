"""Camunda 8 REST API wrapper.

Wraps the three Camunda 8 REST surfaces:

* **Zeebe REST API** (C8.5+, base ``/v2``) — deploy resources, create process
  instances (with/without result), publish messages, broadcast signals, activate
  jobs, complete/fail jobs, update retries/timeout, resolve incidents, cancel
  process instances.
* **Operate REST API** — search process definitions/instances, instance
  statistics, flow node instances, variables, incidents.
* **Tasklist REST API** — search tasks, get task, assign/unassign, complete
  task, get task variables.

OAuth: if ``CAMUNDA8_CLIENT_ID``/``CAMUNDA8_CLIENT_SECRET``/``CAMUNDA8_OAUTH_URL``
are configured, a ``client_credentials`` token is fetched and cached, then
applied to every request. Otherwise no auth header is sent (self-managed
without authentication).
"""

import time
from typing import Any

import requests

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda8Api(ApiClientBase):
    """Full client for the Camunda 8 REST surfaces (Zeebe, Operate, Tasklist)."""

    def __init__(
        self,
        zeebe_url: str,
        operate_url: str | None = None,
        tasklist_url: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        oauth_url: str | None = None,
        audience: str = "zeebe.camunda.io",
        verify: bool = True,
    ):
        # base_url tracks the Zeebe REST endpoint; the other surfaces are
        # addressed via absolute URLs built from their own base.
        super().__init__(base_url=zeebe_url, verify=verify)
        self.zeebe_url = zeebe_url.rstrip("/")
        self.operate_url = (operate_url or "").rstrip("/")
        self.tasklist_url = (tasklist_url or "").rstrip("/")
        self.client_id = client_id
        self.client_secret = client_secret
        self.oauth_url = oauth_url
        self.audience = audience
        self._token: str | None = None
        self._token_expiry: float = 0.0

    # ------------------------------------------------------------------ #
    # OAuth
    # ------------------------------------------------------------------ #
    def _get_token(self) -> str | None:
        """Return a cached bearer token, fetching a new one if needed.

        Returns ``None`` when OAuth is not configured (no-auth deployment).
        """
        if not (self.client_id and self.client_secret and self.oauth_url):
            return None
        if self._token and time.time() < self._token_expiry - 30:
            return self._token

        resp = requests.post(
            self.oauth_url,
            data={
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "audience": self.audience,
            },
            verify=self._session.verify,
        )
        if resp.status_code >= 400:
            raise Exception(
                f"OAuth error: {resp.status_code} - {resp.text}"
            )
        payload = resp.json()
        self._token = payload["access_token"]
        self._token_expiry = time.time() + int(payload.get("expires_in", 300))
        return self._token

    def _auth_headers(
        self, headers: dict[str, str] | None = None
    ) -> dict[str, str] | None:
        token = self._get_token()
        merged = dict(headers or {})
        if token:
            merged["Authorization"] = f"Bearer {token}"
        return merged or None

    def _call(
        self,
        method: str,
        url: str,
        json: Any | None = None,
        params: dict[str, Any] | None = None,
    ) -> Any:
        """Authenticated JSON call to an absolute URL."""
        return self.request(
            method,
            url,
            params=params,
            json=json,
            accept="application/json",
            content_type="application/json" if json is not None else None,
            headers=self._auth_headers(),
        )

    # ------------------------------------------------------------------ #
    # Zeebe REST API (/v2)
    # ------------------------------------------------------------------ #
    def deploy_resources(self, files: dict[str, Any]) -> Any:
        """Deploy BPMN/DMN/form resources via multipart upload.

        ``files`` is a requests-style files dict, e.g.
        ``{"resources": ("process.bpmn", b"<xml>", "text/xml")}``.
        """
        return self.request(
            "POST",
            f"{self.zeebe_url}/v2/deployments",
            files=files,
            accept="application/json",
            headers=self._auth_headers(),
        )

    def create_process_instance(self, body: dict[str, Any]) -> Any:
        """Create a process instance.

        ``body`` is ``{"processDefinitionKey": ..., "variables": {...}}`` or
        ``{"processDefinitionId": <bpmnProcessId>, "variables": {...}}``.
        """
        return self._call(
            "POST", f"{self.zeebe_url}/v2/process-instances", json=body
        )

    def create_process_instance_with_result(self, body: dict[str, Any]) -> Any:
        """Create a process instance and await its result."""
        payload = dict(body)
        payload.setdefault("awaitCompletion", True)
        return self._call(
            "POST", f"{self.zeebe_url}/v2/process-instances", json=payload
        )

    def cancel_process_instance(self, process_instance_key: str) -> Any:
        """Cancel a running process instance."""
        return self._call(
            "POST",
            f"{self.zeebe_url}/v2/process-instances/"
            f"{process_instance_key}/cancellation",
            json={},
        )

    def publish_message(self, body: dict[str, Any]) -> Any:
        """Publish (correlate) a message.

        ``body`` is ``{"name": ..., "correlationKey": ..., "variables": {...}}``.
        """
        return self._call(
            "POST", f"{self.zeebe_url}/v2/messages/publication", json=body
        )

    def broadcast_signal(self, body: dict[str, Any]) -> Any:
        """Broadcast a signal (``{"signalName": ..., "variables": {...}}``)."""
        return self._call(
            "POST", f"{self.zeebe_url}/v2/signals/broadcast", json=body
        )

    def activate_jobs(self, body: dict[str, Any]) -> Any:
        """Activate jobs for a worker.

        ``body`` is ``{"type": ..., "worker": ..., "maxJobsToActivate": ...}``.
        """
        return self._call("POST", f"{self.zeebe_url}/v2/jobs/activation", json=body)

    def complete_job(
        self, job_key: str, variables: dict[str, Any] | None = None
    ) -> Any:
        """Complete a job, optionally returning variables."""
        return self._call(
            "POST",
            f"{self.zeebe_url}/v2/jobs/{job_key}/completion",
            json={"variables": variables or {}},
        )

    def fail_job(self, job_key: str, body: dict[str, Any]) -> Any:
        """Fail a job (``{"retries": ..., "errorMessage": ...}``)."""
        return self._call(
            "POST", f"{self.zeebe_url}/v2/jobs/{job_key}/failure", json=body
        )

    def update_job(self, job_key: str, body: dict[str, Any]) -> Any:
        """Update a job's retries and/or timeout.

        ``body`` is ``{"changeset": {"retries": ..., "timeout": ...}}``.
        """
        return self._call(
            "PATCH", f"{self.zeebe_url}/v2/jobs/{job_key}", json=body
        )

    def resolve_incident(self, incident_key: str) -> Any:
        """Resolve an incident (Zeebe REST)."""
        return self._call(
            "POST",
            f"{self.zeebe_url}/v2/incidents/{incident_key}/resolution",
            json={},
        )

    # ------------------------------------------------------------------ #
    # Operate REST API
    # ------------------------------------------------------------------ #
    def search_process_definitions(self, body: dict[str, Any] | None = None) -> Any:
        """Search process definitions (Operate)."""
        return self._call(
            "POST",
            f"{self.operate_url}/v1/process-definitions/search",
            json=body or {},
        )

    def search_process_instances(self, body: dict[str, Any] | None = None) -> Any:
        """Search process instances (Operate)."""
        return self._call(
            "POST",
            f"{self.operate_url}/v1/process-instances/search",
            json=body or {},
        )

    def get_process_instance(self, key: str) -> Any:
        """Get a single process instance by key (Operate)."""
        return self._call(
            "GET", f"{self.operate_url}/v1/process-instances/{key}"
        )

    def get_process_instance_statistics(self, key: str) -> Any:
        """Get flow-node statistics for a process instance (Operate)."""
        return self._call(
            "GET", f"{self.operate_url}/v1/process-instances/{key}/statistics"
        )

    def search_flownode_instances(self, body: dict[str, Any] | None = None) -> Any:
        """Search flow node instances (Operate)."""
        return self._call(
            "POST",
            f"{self.operate_url}/v1/flownode-instances/search",
            json=body or {},
        )

    def search_variables(self, body: dict[str, Any] | None = None) -> Any:
        """Search variables (Operate)."""
        return self._call(
            "POST", f"{self.operate_url}/v1/variables/search", json=body or {}
        )

    def search_incidents(self, body: dict[str, Any] | None = None) -> Any:
        """Search incidents (Operate)."""
        return self._call(
            "POST", f"{self.operate_url}/v1/incidents/search", json=body or {}
        )

    # ------------------------------------------------------------------ #
    # Tasklist REST API
    # ------------------------------------------------------------------ #
    def search_tasks(self, body: dict[str, Any] | None = None) -> Any:
        """Search user tasks (Tasklist)."""
        return self._call(
            "POST", f"{self.tasklist_url}/v1/tasks/search", json=body or {}
        )

    def get_task(self, task_id: str) -> Any:
        """Get a single user task by id (Tasklist)."""
        return self._call("GET", f"{self.tasklist_url}/v1/tasks/{task_id}")

    def assign_task(self, task_id: str, body: dict[str, Any] | None = None) -> Any:
        """Assign a task (``{"assignee": ..., "allowOverrideAssignment": ...}``)."""
        return self._call(
            "PATCH",
            f"{self.tasklist_url}/v1/tasks/{task_id}/assignment",
            json=body or {},
        )

    def unassign_task(self, task_id: str) -> Any:
        """Unassign a task (Tasklist)."""
        return self._call(
            "PATCH",
            f"{self.tasklist_url}/v1/tasks/{task_id}/unassignment",
            json={},
        )

    def complete_task(
        self, task_id: str, variables: list[dict[str, Any]] | None = None
    ) -> Any:
        """Complete a user task (Tasklist).

        ``variables`` is a list of ``{"name": ..., "value": ...}`` entries.
        """
        return self._call(
            "PATCH",
            f"{self.tasklist_url}/v1/tasks/{task_id}/completion",
            json={"variables": variables or []},
        )

    def get_task_variables(self, task_id: str, body: dict[str, Any] | None = None) -> Any:
        """Search the variables of a task (Tasklist)."""
        return self._call(
            "POST",
            f"{self.tasklist_url}/v1/tasks/{task_id}/variables/search",
            json=body or {},
        )
