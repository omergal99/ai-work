from typing import Literal, Optional
from pydantic import BaseModel, Field


class AgentState(BaseModel):
    agent_id: str = Field(..., description="Unique agent identifier")
    role: str = Field(..., description="Agent role")
    status: Literal["idle", "running", "blocked", "error", "offline"]
    token_budget: int = Field(..., ge=0)
    current_task: Optional[str] = None
    state_pointer: str = Field(..., description="Pointer to the shared state source")
    health_score: float = Field(default=1.0, ge=0.0, le=1.0)
    last_update: Optional[str] = None
    permissions: list[str] = Field(default_factory=list)


class TaskState(BaseModel):
    task_id: str
    objective: str
    status: Literal["pending", "running", "completed", "blocked", "failed"]
    owner: str
    artifacts: list[str] = Field(default_factory=list)
    idempotency_key: Optional[str] = None
    notes: list[str] = Field(default_factory=list)


class AgentEvent(BaseModel):
    event_id: str
    agent_id: str
    event_type: str
    payload: dict
    timestamp: str
