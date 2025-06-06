from typing import Optional

from pydantic import BaseModel

class STaskAdd(BaseModel):
    name: str
    description: Optional[str]

class STask(STaskAdd):
        id: int

class STaskID(BaseModel):
    ok: bool = True
    task_id: int