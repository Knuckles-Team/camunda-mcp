# Camunda Mcp
## API | MCP Server | A2A Agent

![PyPI - Version](https://img.shields.io/pypi/v/camunda-mcp)
![MCP Server](https://badge.mcpx.dev?type=server 'MCP Server')
![PyPI - Downloads](https://img.shields.io/pypi/dd/camunda-mcp)
![GitHub Repo stars](https://img.shields.io/github/stars/Knuckles-Team/camunda-mcp)
![GitHub forks](https://img.shields.io/github/forks/Knuckles-Team/camunda-mcp)
![GitHub contributors](https://img.shields.io/github/contributors/Knuckles-Team/camunda-mcp)
![PyPI - License](https://img.shields.io/pypi/l/camunda-mcp)
![GitHub](https://img.shields.io/github/license/Knuckles-Team/camunda-mcp)
![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/Knuckles-Team/camunda-mcp)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Knuckles-Team/camunda-mcp)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/Knuckles-Team/camunda-mcp)
![GitHub issues](https://img.shields.io/github/issues/Knuckles-Team/camunda-mcp)
![GitHub top language](https://img.shields.io/github/languages/top/Knuckles-Team/camunda-mcp)
![GitHub language count](https://img.shields.io/github/languages/count/Knuckles-Team/camunda-mcp)
![GitHub repo size](https://img.shields.io/github/repo-size/Knuckles-Team/camunda-mcp)
![GitHub repo file count (file type)](https://img.shields.io/github/directory-file-count/Knuckles-Team/camunda-mcp)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/camunda-mcp)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/camunda-mcp)

Camunda (7 & 8) process automation **API + MCP Server + A2A Agent** for the
agent-utilities ecosystem.

*Version: 0.5.0*

> **Documentation** — Installation, deployment, usage across the API, CLI, and MCP
> interfaces, and guidance for provisioning the Camunda platform are maintained in the
> [official documentation](https://knuckles-team.github.io/camunda-mcp/).

`camunda-mcp` wraps the Camunda process automation APIs with thin, deterministic MCP
tools, targeting both platforms from a single server: the **Camunda 7** Engine REST
API and the **Camunda 8** Zeebe / Operate / Tasklist REST APIs. It additionally ships
an **A2A agent server** that exposes the same capability through a Pydantic-AI graph
agent for agent-to-agent orchestration.

## What it provides

- **`Api`** (`camunda_mcp.api_client`) — a facade holding both the Camunda 7 Engine
  REST client (`Camunda7Api`) and the Camunda 8 Zeebe / Operate / Tasklist client
  (`Camunda8Api`), each constructed lazily so a server configured for one platform
  never needs the other's URLs or credentials.
- **Action-dispatch MCP tools** (`camunda-mcp` console script): `camunda_process`,
  `camunda_instance`, `camunda_task`, `camunda_deploy`, `camunda_message`,
  `camunda_external_task`, `camunda_job`, `camunda_history`, `camunda_deployment`,
  and `camunda_ops`. Each takes a `platform` argument (`7` or `8`). See
  [`docs/overview.md`](docs/overview.md) for the full surface.
- **An A2A agent server** (`camunda-agent` console script, described by
  [`a2a.json`](a2a.json)) wrapping the tool surface in a Pydantic-AI graph agent.

## Configuration (environment)

| Var | Default | Meaning |
|---|---|---|
| `CAMUNDA_PLATFORM` | `7` | Target platform: `7` or `8` |
| `CAMUNDA_SSL_VERIFY` | `True` | Verify TLS (set `False` for self-signed homelab) |
| `CAMUNDA7_URL` | `http://localhost:8080/engine-rest` | Camunda 7 Engine REST base URL |
| `CAMUNDA7_TOKEN` / `CAMUNDA7_USERNAME` / `CAMUNDA7_PASSWORD` | — | Camunda 7 bearer or basic auth |
| `CAMUNDA8_ZEEBE_REST_URL` | `http://localhost:8080` | Camunda 8 Zeebe REST base URL |
| `CAMUNDA8_OPERATE_URL` / `CAMUNDA8_TASKLIST_URL` | — | Camunda 8 Operate / Tasklist URLs |
| `CAMUNDA8_CLIENT_ID` / `CAMUNDA8_CLIENT_SECRET` / `CAMUNDA8_OAUTH_URL` / `CAMUNDA8_AUDIENCE` | — | Camunda 8 OAuth `client_credentials` |
| `CAMUNDATOOL` | `True` | Register the Camunda tool set |

Credentials left blank leave the corresponding platform inactive — the connector
remains inactive when credentials are absent. A starter [`.env.example`](.env.example)
ships with the repository; copy it to `.env` and populate the values for the platform
you use.

## Install & run

```bash
pip install -e ".[all]"
camunda-mcp                       # stdio MCP server (default transport)
camunda-mcp --transport streamable-http --host 0.0.0.0 --port 8000
```

Run the A2A agent server against a deployed MCP endpoint:

```bash
MCP_URL=http://camunda-mcp:8000/mcp camunda-agent --host 0.0.0.0 --port 8001
```

## MCP config

Register in the multiplexer under nickname `camun` (tools surface as
`camun__process`, `camun__instance`, `camun__task`, …). See
`camunda_mcp/mcp_config.json`.

<!-- BEGIN GENERATED: additional-deployment-options -->
### Additional Deployment Options

`camunda-mcp` can also run as a **local container** (Docker / Podman / `uv`) or be
consumed from a **remote deployment**. The
[Deployment guide](https://knuckles-team.github.io/camunda-mcp/deployment/) has full, copy-paste
`mcp_config.json` for all four transports — **stdio**, **streamable-http**,
**local container / uv**, and **remote URL**:

- **Local container / uv** — launch the server from `mcp_config.json` via `uvx`,
  `docker run`, or `podman run`, or point at a local streamable-http container by `url`.
- **Remote URL** — connect to a server deployed behind Caddy at
  `http://camunda-mcp.arpa/mcp` using the `"url"` key.
<!-- END GENERATED: additional-deployment-options -->

## Documentation

The complete documentation is published as the
[official documentation site](https://knuckles-team.github.io/camunda-mcp/) and is the
recommended reference for installation, deployment, and day-to-day operation.

| Page | Contents |
|---|---|
| [Installation](https://knuckles-team.github.io/camunda-mcp/installation/) | pip, source, extras, prebuilt Docker image |
| [Deployment](https://knuckles-team.github.io/camunda-mcp/deployment/) | run the MCP and agent servers, Compose, Caddy + Technitium, env config |
| [Usage](https://knuckles-team.github.io/camunda-mcp/usage/) | the MCP tools, the `Api` client, the CLI |
| [Backing Platform](https://knuckles-team.github.io/camunda-mcp/platform/) | deploy Camunda with Docker |
| [Overview](https://knuckles-team.github.io/camunda-mcp/overview/) | the Camunda 7 / Camunda 8 surface |
| [Concepts](https://knuckles-team.github.io/camunda-mcp/concepts/) | concept registry (`CONCEPT:CAMUNDA-*`) |

`AGENTS.md` is the canonical contributor/agent guidance.


<!-- BEGIN agent-os-genesis-deploy (generated; do not edit between markers) -->

## Deploy with `agent-os-genesis`

This package can be provisioned for you — skill-guided — by the **`agent-os-genesis`**
universal skill (its *single-package deploy mode*): it picks your install method, seeds
secrets to OpenBao/Vault (or `.env`), trusts your enterprise CA, registers the MCP
server, and verifies it — the same machinery that stands up the whole Agent OS, narrowed
to just this package. Ask your agent to **"deploy `camunda-mcp` with agent-os-genesis"**.

| Install mode | Command |
|------|---------|
| Bare-metal, prod (PyPI) | `uvx camunda-mcp` · or `uv tool install camunda-mcp` |
| Bare-metal, dev (editable) | `uv pip install -e ".[all]"` · or `pip install -e ".[all]"` |
| Container, prod | deploy `knucklessg1/camunda-mcp:latest` via docker-compose / swarm / podman / podman-compose / kubernetes |
| Container, dev (editable) | deploy `docker/compose.dev.yml` (source-mounted at `/src`; edits live on restart) |

Secrets are read-existing + seeded via `vault_sync` — you are only prompted for what's missing.

<!-- END agent-os-genesis-deploy -->
