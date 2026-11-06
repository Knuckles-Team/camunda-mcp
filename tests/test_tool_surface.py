import asyncio

import pytest
from scion_sdk.connector import build_server
from scion_sdk.mcp.method_tools import UNTYPED_TOOLS_ATTRIBUTE


@pytest.fixture(scope="module")
def served():
    _, mcp = build_server("camunda_mcp", command_args=[])
    return mcp, {t.name: t for t in asyncio.run(mcp.list_tools())}


def test_surface_is_one_tool_per_engine_operation(served):
    """CONN-CAMUNDA-MCP-R002: every Operaton engine REST operation is one tool."""
    _, tools = served
    names = set(tools)
    v7 = {n for n in names if n.startswith("camunda7_")}
    v8 = {n for n in names if n.startswith("camunda8_")}
    assert len(v7) == 386
    assert len(v8) == 24
    assert names - v7 - v8 == {"camunda_ingest_processes"}


def test_no_action_routed_or_untyped_tools(served):
    mcp, tools = served
    for name, tool in tools.items():
        assert "split-action" not in tool.tags, name
        assert "action" not in tool.parameters.get("properties", {}), name
    assert not getattr(mcp, UNTYPED_TOOLS_ATTRIBUTE, set())
    for retired in (
        "camunda_process",
        "camunda_instance",
        "camunda_task",
        "camunda_deploy",
    ):
        assert retired not in tools


def test_query_parameters_are_typed(served):
    _, tools = served
    props = tools["camunda7_get_process_definitions"].parameters["properties"]
    assert {"type": "boolean"} in props["latest_version"]["anyOf"]
    assert {"type": "integer"} in props["max_results"]["anyOf"]
    delete = tools["camunda7_delete_deployment"]
    assert delete.annotations.destructive_hint is True
    assert "cascade" in delete.parameters["properties"]
    assert set(tools["camunda7_create_deployment"].parameters["properties"]) >= {
        "deployment_name",
        "resources",
        "enable_duplicate_filtering",
    }
