# CONN-CAMUNDA-MCP — Implementation plan

Governing spec: [spec.md](spec.md). Rows: [requirements.md](requirements.md).

## Summary

This plan delivers connector identity and release metadata for the connector, reusing the SDK for shared capabilities.

## Technical Context

- **Language/Version**: Python 3.14 (floor 3.12)
- **Primary Dependencies**: scion-sdk, fastmcp
- **Storage**: N/A; the connector stores nothing
- **Testing**: pytest; the proof level each row names
- **Target Platform**: Linux containers
- **Project Type**: connector (MCP server)
- **Performance Goals**: N/A
- **Constraints**: one tool per API operation; shared capabilities come from the SDK
- **Scale/Scope**: 3 rows

## Constitution Check

- One owner per concept: pass. The connector owns one external system's calls, mappings and tools only.
- Connectors depend on the SDK and are called through arbora: pass.
- No ratchets: pass. The rows add no suppression.

## Project Structure

```text
pyproject.toml  existing
camunda_mcp/__init__.py  existing
camunda_mcp/mcp/mcp_camunda.py  existing
camunda_mcp/mcp_server.py  existing
```

## Phase 0: Research

No unknowns. Each row names the code it touches.

## Phase 1: Design

The rows are delivered in place; the design is the caller chain below.

## Phase 2: Task approach

`tasks.md` holds one task line per row, producer first.

## Complexity Tracking

None. The constitution check passed.

## Build contract

The repository pre-commit hooks apply: `ruff-format`, `connector-standard`, `secrets`, `tests-fast`. Each row names its proving test. No suppression and no duplicate implementation.

## Production caller chain

1. `CONN-CAMUNDA-MCP-R001`: the installed `camunda-mcp` distribution metadata (`pyproject.toml` line 7) -> `__version__ = _v("camunda-mcp")` in `camunda_mcp/api_client.py:18`, imported by the code that builds `Api`; `camunda_mcp/__init__.py` defines no `__version__`.
2. `CONN-CAMUNDA-MCP-R002`: the `camunda-mcp` console script (`scion_sdk.cli:serve`) loads `camunda_mcp:connector` (`camunda_mcp/__init__.py:85`); its `verbose_targets` prefixes `camunda7` and `camunda8` yield one tool per client method, and `camunda_mcp/mcp/mcp_camunda.py` registers `camunda_deploy` (line 50) and `camunda_ingest_processes` (line 83).
3. `CONN-CAMUNDA-MCP-R003`: the `camunda-mcp` console script (`scion_sdk.cli:serve`) -> `camunda_mcp:connector` (`camunda_mcp/__init__.py:85`) -> SDK `build_server` -> the tools in `camunda_mcp/mcp/mcp_camunda.py` and the generated `camunda7_*` and `camunda8_*` tools.

## Cross-repo seams

none
