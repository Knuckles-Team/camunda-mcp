"""The one Camunda tool that is not an API-operation wrapper: KG ingest.

Every engine operation is its own typed tool (``camunda7_*``, ``camunda8_*``),
served by the SDK from the clients in ``camunda_mcp.api``. Deploying a BPMN or
DMN resource is ``camunda7_create_deployment`` / ``camunda8_deploy_resources``.
"""

import json
import re
from functools import cache
from importlib import resources
from typing import Any

from fastmcp import FastMCP
from pydantic import Field

from camunda_mcp.auth import get_client


def _snake(name: str) -> str:
    s = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s).lower()


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


@cache
def contracts_turtle() -> str:
    """The surface declarations of ``camunda_mcp.connector_contracts`` as Turtle."""
    from camunda_mcp import connector_contracts as declared
    from camunda_mcp._surface import render_surface_turtle

    prompts: dict[str, dict[str, Any]] = {}
    for path in sorted((resources.files("camunda_mcp") / "prompts").iterdir()):
        if path.name.endswith(".json"):
            document = json.loads(path.read_text(encoding="utf-8"))
            prompts[path.name[: -len(".json")]] = document.get("agent") or {}
    return render_surface_turtle(
        "camunda-mcp",
        declared.CONTRACTS,
        declared.LINKS,
        declared.LOCATIONS,
        declared.ROLES,
        prompts,
    )


def register_camunda_tools(mcp: FastMCP) -> None:
    """Register the Camunda KG ingest tool and the surface-contract resource."""

    @mcp.resource(
        "ontology://camunda-mcp/contracts.ttl",
        name="camunda-mcp-contracts",
        description=(
            "Tool-use contracts, prompt/skill/tool links, data locations and "
            "business roles of camunda-mcp, as surface-contract Turtle."
        ),
        mime_type="text/turtle",
    )
    def camunda_contracts() -> str:
        return contracts_turtle()

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
        """Natively ingest Camunda processes into medulla as typed nodes.

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
            filters = {_snake(k): v for k, v in p.items()}
            defs = _as_records(api.v7.get_process_definitions(**filters))
            insts = (
                _as_records(api.v7.get_process_instances()) if include_instances else []
            )
        return {
            "listed_definitions": len(defs),
            "listed_instances": len(insts),
            "ingested_definitions": await kg_ingest.ingest_process_definitions(defs),
            "ingested_instances": (
                await kg_ingest.ingest_process_instances(insts) if insts else None
            ),
        }
