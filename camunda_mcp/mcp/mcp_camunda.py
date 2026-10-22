"""Camunda tools that are not API-operation wrappers: deploy and KG ingest.

The per-operation tools (``camunda7_*``, ``camunda8_*``) come from the SDK. Each tool here is a thin shim: it parses params,
picks the platform client
(``v7`` = Camunda 7 Engine REST, ``v8`` = Camunda 8 REST), calls the
corresponding method, and returns the result. All API surface lives in
``camunda_mcp.api`` — these tools add no business logic.
"""

import json
from typing import Any

from fastmcp import FastMCP
from pydantic import Field

from camunda_mcp.auth import get_client


def _p(params_json: str) -> dict[str, Any]:
    return json.loads(params_json) if params_json else {}


def _dict_records(items: list) -> list[dict[str, Any]]:
    return [r for r in items if isinstance(r, dict)]


def _nested_list_field(result: dict) -> list | None:
    for key in ("items", "results", "data"):
        val = result.get(key)
        if isinstance(val, list):
            return val
    return None


def _as_records(result: Any) -> list[dict[str, Any]]:
    """Coerce a Camunda list response into a list of record dicts."""
    if isinstance(result, list):
        return _dict_records(result)
    if isinstance(result, dict):
        nested = _nested_list_field(result)
        if nested is not None:
            return _dict_records(nested)
    return []


def register_camunda_tools(mcp: FastMCP) -> None:
    """Register Camunda 7 and Camunda 8 process automation tools."""

    @mcp.tool(tags={"deployment"})
    async def camunda_deploy(
        platform: str = Field(default="7", description="Target platform: '7' or '8'."),
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
                'JSON args. v7: {"deployment_name":..,"data":{...}}. '
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

    @mcp.tool(tags={"kg"})
    async def camunda_ingest_processes(
        platform: str = Field(default="7", description="Target platform: '7' or '8'."),
        params_json: str = Field(
            default="{}",
            description=(
                "JSON filter/search body for listing process definitions "
                "(v7 query params; v8 Operate search body)."
            ),
        ),
        include_instances: bool = Field(
            default=True,
            description="Also list running instances and ingest them (+:instanceOf).",
        ),
    ) -> Any:
        """Natively ingest Camunda processes into epistemic-graph as typed nodes.

        Lists process definitions (and optionally running instances) via the real
        client and pushes them as ``:BusinessProcess`` / ``:ProcessInstance`` nodes
        (+ ``:deployedIn`` / ``:instanceOf`` links) through the fast engine client.
        Best-effort: ``ingested`` is ``None`` when no engine is reachable.
        CONCEPT:AU-KG.ingest.enterprise-source-extractor.
        """
        from camunda_mcp import kg_ingest

        api = get_client()
        p = _p(params_json)
        if str(platform) in ("8", "c8"):
            defs = _as_records(
                api.v8.search_process_definitions(p.get("body", p) or {})
            )
            insts = (
                _as_records(api.v8.search_process_instances(p.get("body", p) or {}))
                if include_instances
                else []
            )
        else:
            defs = _as_records(api.v7.list_process_definitions(p or None))
            insts = (
                _as_records(api.v7.list_process_instances(p or None))
                if include_instances
                else []
            )
        return {
            "listed_definitions": len(defs),
            "listed_instances": len(insts),
            "ingested_definitions": await kg_ingest.ingest_process_definitions(defs),
            "ingested_instances": (
                await kg_ingest.ingest_process_instances(insts) if insts else None
            ),
        }
