"""Every packaged prompt is named by a surface link (CONN-CAMUNDA-MCP-R002)."""

from pathlib import Path

from camunda_mcp.connector_contracts import LINKS

PROMPTS = Path(__file__).resolve().parents[1] / "camunda_mcp" / "prompts"


def test_every_prompt_is_linked_to_a_task():
    linked = {name for link in LINKS for name in link.prompts}
    assert {p.stem for p in PROMPTS.glob("*.json")} <= linked
