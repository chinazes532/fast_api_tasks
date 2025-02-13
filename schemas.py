from typing import Optional

from pydantic import ConfigDict, BaseModel


class STaskAdd(BaseModel):
    title: str
    description: Optional[str] = None
    status: bool


class STask(STaskAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class STaskID(BaseModel):
    ok: bool = True
    task_id: int


