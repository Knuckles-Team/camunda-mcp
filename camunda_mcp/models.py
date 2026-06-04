"""Pydantic models for Camunda process automation operations."""

from typing import Any

from pydantic import BaseModel, Field


class StartProcess(BaseModel):
    """Request to start a process instance."""

    key: str | None = Field(
        default=None, description="Process definition key (latest version)."
    )
    id: str | None = Field(default=None, description="Process definition id.")
    variables: dict[str, Any] = Field(
        default_factory=dict, description="Process variables to set on start."
    )
    business_key: str | None = Field(
        default=None, description="Business key for the new instance."
    )


class CompleteTask(BaseModel):
    """Request to complete a user task."""

    task_id: str = Field(description="The user task id.")
    variables: dict[str, Any] = Field(
        default_factory=dict, description="Variables to submit on completion."
    )
