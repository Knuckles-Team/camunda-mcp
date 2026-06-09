# camunda-mcp

Camunda (7 & 8) process automation **API + MCP Server + A2A Agent** for the
agent-utilities ecosystem — a typed, deterministic tool surface over the Camunda 7
Engine REST API and the Camunda 8 Zeebe / Operate / Tasklist REST APIs.

!!! info "Official documentation"
    This site is the canonical reference for `camunda-mcp`, maintained alongside every
    release.

[![PyPI](https://img.shields.io/pypi/v/camunda-mcp)](https://pypi.org/project/camunda-mcp/)
![MCP Server](https://badge.mcpx.dev?type=server 'MCP Server')
[![License](https://img.shields.io/pypi/l/camunda-mcp)](https://github.com/Knuckles-Team/camunda-mcp/blob/main/LICENSE)
[![GitHub](https://img.shields.io/badge/source-GitHub-181717?logo=github)](https://github.com/Knuckles-Team/camunda-mcp)

## Overview

`camunda-mcp` wraps the Camunda process automation APIs with thin, deterministic MCP
tools, supporting both platforms from a single server. It provides:

- **`Api`** — a facade (`camunda_mcp.api_client`) holding both the Camunda 7 Engine
  REST client (`Camunda7Api`) and the Camunda 8 Zeebe / Operate / Tasklist client
  (`Camunda8Api`), each constructed lazily so a server configured for one platform
  never needs the other's URLs or credentials.
- **Action-dispatch MCP tools** — `camunda_process`, `camunda_instance`,
  `camunda_task`, `camunda_deploy`, `camunda_message`, `camunda_external_task`,
  `camunda_job`, `camunda_history`, `camunda_deployment`, and `camunda_ops`, each
  taking a `platform` argument (`7` or `8`).
- **An A2A agent server** — the `camunda-agent` console script exposes the same
  capability through a Pydantic-AI graph agent for agent-to-agent orchestration.

## Explore the documentation

<div class="grid cards" markdown>

- :material-rocket-launch: **[Installation](installation.md)** — pip, source, extras, and the prebuilt Docker image.
- :material-server-network: **[Deployment](deployment.md)** — run the MCP and agent servers, Docker Compose, Caddy + Technitium.
- :material-console: **[Usage](usage.md)** — the MCP tools, the `Api` client, and the CLI.
- :material-database-cog: **[Backing Platform](platform.md)** — deploy Camunda with Docker.
- :material-text-box-outline: **[Overview](overview.md)** — the Camunda 7 / Camunda 8 surface.
- :material-tag-multiple: **[Concepts](concepts.md)** — the `CONCEPT:CAMUNDA-*` registry.

</div>

## Quick start

```bash
pip install "camunda-mcp[mcp]"
camunda-mcp                       # stdio MCP server (default transport)
```

Connect it to a Camunda platform:

```bash
export CAMUNDA_PLATFORM=7
export CAMUNDA7_URL=http://your-camunda:8080/engine-rest
camunda-mcp --transport streamable-http --host 0.0.0.0 --port 8000
```

See **[Installation](installation.md)** and **[Deployment](deployment.md)** for the
full matrix (PyPI extras, Docker image, all transports, the agent server, reverse
proxy, DNS).
