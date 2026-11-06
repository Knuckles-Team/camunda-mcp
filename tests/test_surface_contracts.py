"""CONN-CAMUNDA-MCP-R005, R006: tool-use contracts, links, locations, roles and agent prompts."""

import asyncio
import inspect
import json
import re
from pathlib import Path

import pytest
from scion_sdk.connector import build_server

from camunda_mcp import connector_contracts as declared
from camunda_mcp.mcp.mcp_camunda import contracts_turtle

PACKAGE = Path(__file__).resolve().parents[1] / "camunda_mcp"
PROMPTS = {
    p.stem: json.loads(p.read_text()) for p in (PACKAGE / "prompts").glob("*.json")
}
SKILLS = {p.parent.name for p in (PACKAGE / "skills").glob("*/SKILL.md")}


@pytest.fixture(scope="module")
def tools():
    _, mcp = build_server("camunda_mcp", command_args=[])
    return {t.name: t for t in asyncio.run(mcp.list_tools())}


def test_every_tool_is_called_by_a_contract_and_named_by_a_link(tools):
    called = {s.tool for c in declared.CONTRACTS for s in c.steps}
    linked = {t for link in declared.LINKS for t in link.tools}
    assert set(tools) <= called
    assert set(tools) <= linked
    assert called <= set(tools) and linked <= set(tools)


def test_steps_pass_real_parameters_and_declare_refusals(tools):
    for contract in declared.CONTRACTS:
        assert any(s.refusals for s in contract.steps), contract.task
        for step in contract.steps:
            props = set(tools[step.tool].parameters.get("properties", {}))
            assert set(step.params) <= props, (step.tool, set(step.params) - props)
            assert step.result, step.tool


def test_links_name_packaged_prompts_and_skills():
    tasks = {c.task for c in declared.CONTRACTS}
    for link in declared.LINKS:
        assert link.task in tasks
        assert set(link.prompts) <= set(PROMPTS), link
        assert set(link.skills) <= SKILLS, link
    assert {p for link in declared.LINKS for p in link.prompts} == set(PROMPTS)
    assert {s for link in declared.LINKS for s in link.skills} == SKILLS


def test_prompts_are_complete_agent_definitions(tools):
    locations = {loc.name for loc in declared.LOCATIONS}
    roles = {r.name for r in declared.ROLES}
    kinds = set()
    for name, doc in PROMPTS.items():
        agent = doc["agent"]
        kinds.add(agent["kind"])
        directive = doc["instructions"]["core_directive"]
        for section in ("GOAL", "TOOLS AND SKILLS", "DATA", "GUARDRAILS", "OUTPUT"):
            assert section in directive, (name, section)
        assert set(agent["tools"]) <= set(tools), name
        assert set(agent["skills"]) <= SKILLS, name
        assert set(agent["data"]["reads"]) | set(agent["data"]["writes"]) <= locations
        assert agent["guardrails"]["never"] and agent["outputs"], name
        for tool in agent["tools"]:
            annotations = tools[tool].annotations
            if annotations and annotations.destructive_hint:
                assert tool in agent["guardrails"]["approval_required"], (name, tool)
        for tool in re.findall(r"\bcamunda[78]?_\w+", directive):
            assert tool in tools, (name, tool)
        if agent["kind"] == "business-role":
            assert agent["business_role"] in roles
    assert "operator" in kinds
    assert roles == {
        d["agent"]["business_role"]
        for d in PROMPTS.values()
        if d["agent"]["kind"] == "business-role"
    }


def test_locations_read_through_served_tools(tools):
    for loc in declared.LOCATIONS:
        assert loc.read_tool in tools
        assert loc.federation_key and loc.instance


def test_skills_name_only_served_tools(tools):
    for skill in (PACKAGE / "skills").rglob("*.md"):
        for tool in re.findall(
            r"\bcamunda[78]_\w+|\bcamunda_ingest_processes\b", skill.read_text()
        ):
            assert tool in tools, (skill.name, tool)


def test_contracts_render_as_turtle():
    text = contracts_turtle()
    assert "sc:ToolUseContract" in text and "sc:DataLocation" in text
    assert "owl:imports" not in text
    assert inspect.isfunction(contracts_turtle.__wrapped__)
