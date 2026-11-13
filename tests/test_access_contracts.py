"""CONN-CAMUNDA-MCP-CONNECTOR-CONTENT-R002: the competency reads are declared
as access contracts and each recorded response satisfies its contract."""

import asyncio
import json
from importlib import resources
from pathlib import Path

import pytest
import requests
from fastmcp import Client
from scion_sdk.access_contract import parse_access_contracts
from scion_sdk.connector import build_server

ID = "CONN-CAMUNDA-MCP-CONNECTOR-CONTENT-R002"
ROOT = Path(__file__).resolve().parents[1]
CONTRACTS = parse_access_contracts(
    (ROOT / "camunda_mcp/ontology/access_contracts.ttl").read_text()
)
ONTOLOGY = (
    resources.files("camunda_mcp").joinpath("ontology", "camunda.ttl").read_text()
)
CONNECTOR_NS = "https://knuckles-team.github.io/ontology/connector/camunda#"


class _Response:
    status_code = 200
    headers = {"Content-Type": "application/json"}
    encoding = "utf-8"

    def __init__(self, body: bytes):
        self._body = body

    def iter_content(self, chunk_size=0):
        yield self._body

    def close(self):
        pass


def _serve(monkeypatch, operation, recording):
    monkeypatch.setenv("CAMUNDA7_URL", "http://engine.test/engine-rest")
    body = json.dumps(recording).encode()
    monkeypatch.setattr(
        requests.Session, "request", lambda *args, **kw: _Response(body)
    )

    async def call():
        _, mcp = build_server("camunda_mcp", command_args=[])
        async with Client(mcp) as client:
            tools = {t.name for t in await client.list_tools()}
            assert operation in tools
            result = await client.call_tool(operation, {})
            return json.loads(result.content[0].text)

    return asyncio.run(call())


@pytest.mark.spec(ID)
def test_competency_contracts_certified(monkeypatch):
    assert {c.entity for c in CONTRACTS} == {"process_definition", "incident"}
    for contract in CONTRACTS:
        assert contract.source_id == "camunda-mcp"
        assert contract.access_kind == "mcp_tool"
        assert contract.pagination == "none"
        assert contract.class_iri.startswith(CONNECTOR_NS)
        assert f"\n:{contract.class_iri.removeprefix(CONNECTOR_NS)} a owl:Class" in (
            ONTOLOGY
        )
        for prop, _ in contract.predicates:
            if prop.startswith(CONNECTOR_NS):
                local = prop.removeprefix(CONNECTOR_NS)
                assert f"\n:{local} a owl:" in ONTOLOGY, local
        recording = json.loads(
            (ROOT / f"tests/recordings/{contract.entity}.json").read_text()
        )
        assert recording
        served = _serve(monkeypatch, contract.operation, recording)
        assert served == recording
        for record in served:
            assert contract.key_field in record
            assert all(field in record for _, field in contract.predicates)


@pytest.mark.spec(ID)
def test_contract_refuses_a_recording_missing_a_bound_field():
    (contract,) = [c for c in CONTRACTS if c.entity == "incident"]
    record = {"id": "x", "activityId": "a"}
    assert not all(field in record for _, field in contract.predicates)
