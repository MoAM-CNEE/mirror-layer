from pydantic import BaseModel
from typing import Dict, Any, Optional


class ControlPlaneApplyRQ(BaseModel):
    change_id: int
    entity_definition: Dict[str, Any]


class ControlPlaneDeleteRQ(BaseModel):
    api_version: str
    kind: str
    name: str
    namespace: Optional[str] = None
