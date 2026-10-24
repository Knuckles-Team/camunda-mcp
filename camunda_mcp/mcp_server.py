"""Main FastMCP server and tool registration for camunda-mcp."""

from camunda_mcp.mcp.mcp_camunda import register_camunda_tools  # noqa: F401

# SDK discovery registers the register_<tag>_tools functions bound in this module.
__all__ = ["register_camunda_tools"]
