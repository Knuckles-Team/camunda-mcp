import asyncio

from camunda_mcp.mcp_server import get_mcp_instance


def _tools() -> dict:
    mcp, _args, _mw = get_mcp_instance()
    return {t.name: t for t in asyncio.run(mcp.list_tools())}


def test_surface_is_one_tool_per_operation_plus_two():
    names = set(_tools())
    v7 = {n for n in names if n.startswith("camunda7_")}
    v8 = {n for n in names if n.startswith("camunda8_")}
    assert len(v7) == 39
    assert len(v8) == 24
    assert names - v7 - v8 == {"camunda_deploy", "camunda_ingest_processes"}
    assert len(names) == 65


def test_no_split_action_facade_tools():
    for name, tool in _tools().items():
        assert "split-action" not in tool.tags, name
