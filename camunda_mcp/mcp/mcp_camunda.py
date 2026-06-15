"""Thin MCP wrappers around the Camunda API clients.

Each tool is a thin shim: it parses params, picks the platform client
(``v7`` = Camunda 7 Engine REST, ``v8`` = Camunda 8 REST), calls the
corresponding method, and returns the result. All API surface lives in
``camunda_mcp.api`` — these tools add no business logic.
"""

import json
from typing import Any, cast

from fastmcp import FastMCP
from pydantic import Field

from camunda_mcp.auth import get_client


def _p(params_json: str) -> dict[str, Any]:
    return json.loads(params_json) if params_json else {}


def register_camunda_tools(mcp: FastMCP) -> None:
    """Register Camunda 7 and Camunda 8 process automation tools."""

    @mcp.tool(tags={"process"})
    async def camunda_process(
        action: str = Field(
            description=(
                "Process definition action. v7: 'list', 'get', 'xml', 'start', "
                "'statistics', 'suspend'. v8: 'list' (Operate search)."
            )
        ),
        platform: str = Field(
            default="7", description="Target platform: '7' or '8'."
        ),
        params_json: str = Field(
            default="{}",
            description=(
                "JSON args. v7 get/xml: {\"id\":..} or {\"key\":..}; "
                "start: {\"key\":..,\"body\":{\"variables\":{...}}}; "
                "list/statistics/suspend take filter/body fields. "
                "v8 list: an Operate search body."
            ),
        ),
    ) -> Any:
        """Work with process definitions on Camunda 7 or Camunda 8."""
        api = get_client()
        p = _p(params_json)
        if str(platform) in ("8", "c8"):
            c8 = api.v8
            if action == "list":
                return c8.search_process_definitions(p.get("body", p) or {})
            raise ValueError(f"Unknown v8 process action: {action!r}.")
        c7 = api.v7
        if action == "list":
            return c7.list_process_definitions(p or None)
        if action == "get":
            return c7.get_process_definition(p.get("id"), p.get("key"))
        if action == "xml":
            return c7.get_process_definition_xml(p.get("id"), p.get("key"))
        if action == "start":
            return c7.start_process_instance(
                p.get("id"), p.get("key"), p.get("body")
            )
        if action == "statistics":
            return c7.get_process_definition_statistics(p or None)
        if action == "suspend":
            return c7.suspend_process_definition(
                p.get("id"),
                p.get("key"),
                p.get("suspended", True),
                p.get("include_instances", True),
            )
        raise ValueError(f"Unknown v7 process action: {action!r}.")

    @mcp.tool(tags={"process"})
    async def camunda_instance(
        action: str = Field(
            description=(
                "Process instance action. v7: 'list', 'get', 'delete', "
                "'variables', 'set_variables', 'suspend'. v8: 'list', 'get', "
                "'statistics', 'cancel'."
            )
        ),
        platform: str = Field(
            default="7", description="Target platform: '7' or '8'."
        ),
        params_json: str = Field(
            default="{}",
            description=(
                "JSON args. v7: {\"instance_id\":..} plus body for "
                "set_variables; v8: {\"key\":..} or a search {\"body\":{...}}."
            ),
        ),
    ) -> Any:
        """Work with process instances on Camunda 7 or Camunda 8."""
        api = get_client()
        p = _p(params_json)
        if str(platform) in ("8", "c8"):
            c8 = api.v8
            if action == "list":
                return c8.search_process_instances(p.get("body", p) or {})
            if action == "get":
                return c8.get_process_instance(p["key"])
            if action == "statistics":
                return c8.get_process_instance_statistics(p["key"])
            if action == "cancel":
                return c8.cancel_process_instance(p["key"])
            raise ValueError(f"Unknown v8 instance action: {action!r}.")
        c7 = api.v7
        iid = cast(str, p.get("instance_id"))
        if action == "list":
            return c7.list_process_instances(p or None)
        if action == "get":
            return c7.get_process_instance(iid)
        if action == "delete":
            return c7.delete_process_instance(iid, p.get("params"))
        if action == "variables":
            return c7.get_process_instance_variables(iid)
        if action == "set_variables":
            return c7.modify_process_instance_variables(iid, p["body"])
        if action == "suspend":
            return c7.suspend_process_instance(iid, p.get("suspended", True))
        raise ValueError(f"Unknown v7 instance action: {action!r}.")

    @mcp.tool(tags={"task"})
    async def camunda_task(
        action: str = Field(
            description=(
                "User task action. v7: 'list', 'get', 'claim', 'unclaim', "
                "'assign', 'complete', 'variables', 'set_variables'. v8: "
                "'list', 'get', 'assign', 'unassign', 'complete', 'variables'."
            )
        ),
        platform: str = Field(
            default="7", description="Target platform: '7' or '8'."
        ),
        params_json: str = Field(
            default="{}",
            description=(
                "JSON args. v7: {\"task_id\":..,\"user_id\":..,"
                "\"variables\":{...}}; v8: {\"task_id\":..,\"assignee\":..,"
                "\"variables\":[{\"name\":..,\"value\":..}]} or a search body."
            ),
        ),
    ) -> Any:
        """Work with user tasks on Camunda 7 or Camunda 8 (Tasklist)."""
        api = get_client()
        p = _p(params_json)
        if str(platform) in ("8", "c8"):
            c8 = api.v8
            tid = cast(str, p.get("task_id"))
            if action == "list":
                return c8.search_tasks(p.get("body", {}))
            if action == "get":
                return c8.get_task(tid)
            if action == "assign":
                return c8.assign_task(tid, p.get("body") or {
                    k: v for k, v in p.items() if k != "task_id"
                })
            if action == "unassign":
                return c8.unassign_task(tid)
            if action == "complete":
                return c8.complete_task(tid, p.get("variables"))
            if action == "variables":
                return c8.get_task_variables(tid, p.get("body"))
            raise ValueError(f"Unknown v8 task action: {action!r}.")
        c7 = api.v7
        tid = cast(str, p.get("task_id"))
        if action == "list":
            return c7.list_tasks(p or None)
        if action == "get":
            return c7.get_task(tid)
        if action == "claim":
            return c7.claim_task(tid, p["user_id"])
        if action == "unclaim":
            return c7.unclaim_task(tid)
        if action == "assign":
            return c7.set_task_assignee(tid, p["user_id"])
        if action == "complete":
            return c7.complete_task(tid, p.get("variables"))
        if action == "variables":
            return c7.get_task_variables(tid)
        if action == "set_variables":
            return c7.set_task_variables(tid, p["body"])
        raise ValueError(f"Unknown v7 task action: {action!r}.")

    @mcp.tool(tags={"deployment"})
    async def camunda_deploy(
        platform: str = Field(
            default="7", description="Target platform: '7' or '8'."
        ),
        resource_name: str = Field(
            default="process.bpmn",
            description="File name of the resource to deploy.",
        ),
        resource_content: str = Field(
            default="",
            description="Resource content (BPMN/DMN XML or form JSON).",
        ),
        params_json: str = Field(
            default="{}",
            description=(
                "JSON args. v7: {\"deployment_name\":..,\"data\":{...}}. "
                "v8 ignores extra args."
            ),
        ),
    ) -> Any:
        """Deploy a BPMN/DMN/form resource to Camunda 7 or Camunda 8."""
        api = get_client()
        p = _p(params_json)
        content = resource_content.encode("utf-8")
        if str(platform) in ("8", "c8"):
            files = {"resources": (resource_name, content, "text/xml")}
            return api.v8.deploy_resources(files)
        files = {resource_name: (resource_name, content, "text/xml")}
        return api.v7.create_deployment(
            files,
            deployment_name=p.get("deployment_name", "deployment"),
            data=p.get("data"),
        )

    @mcp.tool(tags={"messaging"})
    async def camunda_message(
        action: str = Field(
            description=(
                "Messaging action. v7: 'correlate', 'signal'. v8: 'publish', "
                "'signal'."
            )
        ),
        platform: str = Field(
            default="7", description="Target platform: '7' or '8'."
        ),
        params_json: str = Field(
            default="{}",
            description=(
                "JSON body for the message/signal. v7 correlate: "
                "{\"messageName\":..,\"businessKey\":..}; v8 publish: "
                "{\"name\":..,\"correlationKey\":..}; v8 signal: "
                "{\"signalName\":..}."
            ),
        ),
    ) -> Any:
        """Correlate/publish a message or broadcast a signal."""
        api = get_client()
        body = _p(params_json)
        if str(platform) in ("8", "c8"):
            c8 = api.v8
            if action == "publish":
                return c8.publish_message(body)
            if action == "signal":
                return c8.broadcast_signal(body)
            raise ValueError(f"Unknown v8 message action: {action!r}.")
        c7 = api.v7
        if action == "correlate":
            return c7.correlate_message(body)
        if action == "signal":
            return c7.throw_signal(body)
        raise ValueError(f"Unknown v7 message action: {action!r}.")

    @mcp.tool(tags={"external-task"})
    async def camunda_external_task(
        action: str = Field(
            description=(
                "Camunda 7 external task action: 'fetch_and_lock', 'complete', "
                "'failure', 'bpmn_error'."
            )
        ),
        params_json: str = Field(
            default="{}",
            description=(
                "JSON args. fetch_and_lock: a full request body; others: "
                "{\"task_id\":..,\"body\":{...}}."
            ),
        ),
    ) -> Any:
        """Camunda 7 external task worker operations."""
        c7 = get_client().v7
        p = _p(params_json)
        if action == "fetch_and_lock":
            return c7.fetch_and_lock(p.get("body", p))
        tid = p["task_id"]
        body = p.get("body", {})
        if action == "complete":
            return c7.complete_external_task(tid, body)
        if action == "failure":
            return c7.handle_external_task_failure(tid, body)
        if action == "bpmn_error":
            return c7.handle_external_task_bpmn_error(tid, body)
        raise ValueError(f"Unknown external task action: {action!r}.")

    @mcp.tool(tags={"jobs"})
    async def camunda_job(
        action: str = Field(
            description=(
                "Job/incident action. v7: 'list_jobs', 'execute_job', "
                "'set_retries', 'list_incidents', 'get_incident', "
                "'resolve_incident'. v8: 'activate', 'complete', 'fail', "
                "'update', 'resolve_incident'."
            )
        ),
        platform: str = Field(
            default="7", description="Target platform: '7' or '8'."
        ),
        params_json: str = Field(
            default="{}",
            description=(
                "JSON args. v7: {\"job_id\":..,\"retries\":..} / "
                "{\"incident_id\":..} / filter body. v8: "
                "{\"job_key\":..,\"body\":{...}} or {\"incident_key\":..}."
            ),
        ),
    ) -> Any:
        """Manage jobs and incidents on Camunda 7 or Camunda 8."""
        api = get_client()
        p = _p(params_json)
        if str(platform) in ("8", "c8"):
            c8 = api.v8
            if action == "activate":
                return c8.activate_jobs(p.get("body", p))
            if action == "complete":
                return c8.complete_job(p["job_key"], p.get("variables"))
            if action == "fail":
                return c8.fail_job(p["job_key"], p.get("body", {}))
            if action == "update":
                return c8.update_job(p["job_key"], p.get("body", {}))
            if action == "resolve_incident":
                return c8.resolve_incident(p["incident_key"])
            raise ValueError(f"Unknown v8 job action: {action!r}.")
        c7 = api.v7
        if action == "list_jobs":
            return c7.list_jobs(p or None)
        if action == "execute_job":
            return c7.execute_job(p["job_id"])
        if action == "set_retries":
            return c7.set_job_retries(p["job_id"], p["retries"])
        if action == "list_incidents":
            return c7.list_incidents(p or None)
        if action == "get_incident":
            return c7.get_incident(p["incident_id"])
        if action == "resolve_incident":
            return c7.resolve_incident(p["incident_id"])
        raise ValueError(f"Unknown v7 job action: {action!r}.")

    @mcp.tool(tags={"history"})
    async def camunda_history(
        action: str = Field(
            description=(
                "Camunda 7 history action: 'process_instances', "
                "'activity_instances', 'variables'."
            )
        ),
        params_json: str = Field(
            default="{}", description="JSON query filters for the history query."
        ),
    ) -> Any:
        """Query Camunda 7 historic data."""
        c7 = get_client().v7
        p = _p(params_json) or None
        if action == "process_instances":
            return c7.list_historic_process_instances(p)
        if action == "activity_instances":
            return c7.list_historic_activity_instances(p)
        if action == "variables":
            return c7.list_historic_variables(p)
        raise ValueError(f"Unknown history action: {action!r}.")

    @mcp.tool(tags={"deployment"})
    async def camunda_deployment(
        action: str = Field(
            description="Camunda 7 deployment action: 'list', 'get', 'delete'."
        ),
        params_json: str = Field(
            default="{}",
            description=(
                "JSON args. list: filter body; get/delete: "
                "{\"deployment_id\":..,\"params\":{...}}."
            ),
        ),
    ) -> Any:
        """Manage Camunda 7 deployments (list/get/delete)."""
        c7 = get_client().v7
        p = _p(params_json)
        if action == "list":
            return c7.list_deployments(p or None)
        if action == "get":
            return c7.get_deployment(p["deployment_id"])
        if action == "delete":
            return c7.delete_deployment(p["deployment_id"], p.get("params"))
        raise ValueError(f"Unknown deployment action: {action!r}.")

    @mcp.tool(tags={"operate"})
    async def camunda_ops(
        action: str = Field(
            description=(
                "Camunda 8 Operate/Tasklist search. One of: "
                "'process_definitions', 'process_instances', "
                "'flownode_instances', 'variables', 'incidents', 'tasks'."
            )
        ),
        params_json: str = Field(
            default="{}", description="JSON search body for the chosen surface."
        ),
    ) -> Any:
        """Search Camunda 8 Operate / Tasklist surfaces."""
        c8 = get_client().v8
        body = _p(params_json)
        if action == "process_definitions":
            return c8.search_process_definitions(body)
        if action == "process_instances":
            return c8.search_process_instances(body)
        if action == "flownode_instances":
            return c8.search_flownode_instances(body)
        if action == "variables":
            return c8.search_variables(body)
        if action == "incidents":
            return c8.search_incidents(body)
        if action == "tasks":
            return c8.search_tasks(body)
        raise ValueError(f"Unknown ops action: {action!r}.")
