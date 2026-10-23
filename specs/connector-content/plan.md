# CONN-CAMUNDA-MCP-CONNECTOR-CONTENT — Design and implementation plan

Governing spec: [spec.md](spec.md).

## Architecture

`pyproject.toml` declares `camunda-mcp` as the connector identity. `create_mcp_server` resolves the packaged content of `camunda_mcp` from it.
