# camunda-mcp

A Model Context Protocol (MCP) server for Camunda integration.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Architecture](#architecture)
- [Deployment](#deployment)
- [Environment Variables](#environment-variables)
- [MCP Tools](#mcp-tools)

## Overview
camunda-mcp exposes a standardized interface to interact with Camunda using the Model Context Protocol.

## Installation
```bash
pip install -e .
```

## Usage
Run the MCP server directly:
```bash
python -m camunda_mcp
```

## Architecture
See `/docs` for architectural diagrams and further documentation.

## Deployment
### Bare-metal
```bash
python -m camunda_mcp.agent_server
```

### Docker
```bash
docker compose -f docker/agent.compose.yml up -d
```

## Environment Variables
| Variable | Description |
|----------|-------------|
| `CAMUNDA_URL` | URL for the Camunda instance |
| `CAMUNDA_TOKEN` | Authentication token |

## MCP Tools
| Tool | Description |
|------|-------------|
| `get_camunda_info` | Retrieve basic information from Camunda |
| `query_camunda` | Run a query against the Camunda instance |
