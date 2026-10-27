---
name: camunda-mcp-development
skill_type: skill
description: >-
  Develop and verify camunda-mcp as a connector-owned package while preserving
  its SDK Connector wiring, Camunda 7 and 8 authentication/TLS boundaries,
  typed operation tools, packaged content, and source-backed spec delivery.
license: MIT
tags: [camunda-mcp, development, connector, test, gates, camunda]
tier: repository
metadata:
  author: Repository Maintainers
  version: '0.1.0'
---

# Camunda MCP development

Use this skill for changes to the `camunda-mcp` connector. The package owns the
Camunda API calls, MCP tool registration, knowledge-graph mappings, connector
sources, and packaged skills. The SDK transport, shared Pages renderer, and
Pipelines hooks remain external boundaries.

## Repository map and runtime boundary

- `camunda_mcp/__init__.py` creates the SDK `Connector` with the Camunda 7 and
  Camunda 8 client classes, `get_client`, and `camunda_mcp.mcp_server` as the
  tool module. Preserve this connector identity and its verbose tool prefixes.
- `camunda_mcp/mcp_server.py` exposes `register_camunda_tools`, while
  `camunda_mcp/mcp/mcp_camunda.py` owns the two connector-specific tools:
  `camunda_deploy` and `camunda_ingest_processes`. The SDK supplies the
  `camunda7_*` and `camunda8_*` one-operation tools; do not reintroduce a
  condensed or duplicate action facade.
- `camunda_mcp/api/api_client_camunda7.py` owns the Camunda 7 Engine REST
  surface and `camunda_mcp/api/api_client_camunda8.py` owns the Zeebe, Operate,
  and Tasklist REST surfaces. `camunda_mcp/api/api_client_base.py` centralizes
  bounded requests, origin checks, redirects, response limits, and TLS setup.
- `camunda_mcp/auth.py` reads `CAMUNDA_PLATFORM`, `CAMUNDA7_URL`,
  `CAMUNDA7_TOKEN`, `CAMUNDA7_USERNAME`, `CAMUNDA7_PASSWORD`,
  `CAMUNDA8_ZEEBE_REST_URL`, `CAMUNDA8_OPERATE_URL`,
  `CAMUNDA8_TASKLIST_URL`, `CAMUNDA8_CLIENT_ID`, `CAMUNDA8_CLIENT_SECRET`,
  and `CAMUNDA8_OAUTH_URL`, plus timeout/response limits and the named
  `CAMUNDA_TLS_PROFILE` or `CAMUNDA_TLS_PROFILE_REF`. Preserve SDK setting
  lookup, OAuth/basic/bearer behavior, and TLS verification; never embed a
  credential or weaken verification.
- `camunda_mcp/connector_sources.py`, `camunda_mcp/ontology/`, and
  `camunda_mcp/skills/` are packaged connector content. `pyproject.toml`
  includes these trees through package data; inspect a built wheel when
  changing packaged content.
- The declared console script is `camunda-mcp = agent_connector_sdk.cli:serve`
  and the connector entry point is `camunda-mcp = camunda_mcp:connector`.
  Do not invent a second server or agent entry point.

## Rapid delivery: the 5-minute contract

1. Read the owning `specs/` row, this repository's `AGENTS.md`, and the focused
   tests before editing. Find the row with `git grep -n '<term>' -- specs` and
   put its identifier in the commit trailer.
2. Inspect the active SDK Connector, `mcp_server.py` registrar, typed operation
   clients, auth/TLS path, and package-data declaration before changing runtime
   or packaged content. Reuse those seams instead of creating a second client,
   tool registry, or content loader.
3. Make the smallest connector-owned change. Preserve tool names and payload
   shapes, Camunda 7/8 REST paths, `CAMUNDA_*` settings, TLS verification,
   ontology/source mappings, and the SDK Connector boundary unless the owning
   requirement changes.
4. Bind each delivered requirement to a focused test. Run the actual tests
   through the narrow test-slot wrapper, then run the repository hooks normally;
   never use `--no-verify`, skipped hooks, or a live credential-bearing test.
5. When packaged content changes, advance the patch version and update
   `uv.lock` together. Inspect the built wheel or sdist to confirm the skill is
   included before claiming package publication.
6. Generated `specs/*/status.json` files are written by `pipelines-hook
   spec-status`; never hand-edit them. Treat Pages as separate proof: after an
   exact main SHA has a successful Pages run, check `/spec-delivery/` over HTTPS
   and record the observed snapshot revision.

## Focused development commands

From the repository root:

```bash
uv sync --locked

/var/tmp/arbora-delivery/scale/run-narrow-test-slot.sh \
  uv run --locked --extra test pytest -q \
    tests/test_publication_workflow.py \
    tests/test_tool_surface.py \
    tests/test_http_security.py \
    tests/test_kg_ingest.py

uvx pre-commit run --all-files
uvx pre-commit run --all-files --hook-stage pre-push
```

These checks cover the source-backed publication contract, the SDK-discovered
tool surface, bounded outbound HTTP behavior, and typed KG ingestion. Do not
replace them with a live Camunda call or a credential-bearing test.

## Pages and package publication

`.github/workflows/pages.yml` is the sole Pages caller. It invokes
`pages_pipeline.yml@main` with `content_source: docs`,
`spec_dashboard_enabled: true`, and `.github/spec-dashboard.json`; its push
filters cover `docs/**`, `mkdocs.yml`, `README.md`, `specs/**`, the dashboard
config, and the Pages workflow. The package workflow uses the shared
`connector: true` and `render_connector: true` callers. Keep those callers and
their permissions intact while changing connector content.

After a merge, verify the exact main SHA in the successful Pages run and probe:

```bash
curl -fsSI https://knuckles-team.github.io/camunda-mcp/
curl -fsSI https://knuckles-team.github.io/camunda-mcp/spec-delivery/
curl -fsSI https://knuckles-team.github.io/camunda-mcp/spec-delivery/index.html
curl -fsS https://knuckles-team.github.io/camunda-mcp/spec-delivery/snapshot.json
```

Do not claim a Pages or package result from local source inspection alone. Keep
generated status changes with the Pipelines/status owner.

## Change discipline

- Keep Camunda API calls, MCP schemas, auth settings, TLS resolution, ontology
  mappings, and ingestion declarations under this connector's boundary. SDK and
  shared renderer behavior belong to their owner repositories.
- Use injected `CAMUNDA_*` configuration only; never print or commit tokens,
  client secrets, passwords, host-specific profiles, or generated runtime state.
- Preserve Camunda request/auth/TLS semantics and the existing one-operation
  tool mapping. For mutations, inspect current state and verify the durable
  result through the governed procedure.
- Generated status files and central promotion are owned by Pipelines; this
  skill does not authorize editing `specs/*/status.json`.
