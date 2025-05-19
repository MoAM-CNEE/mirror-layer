from pydantic import BaseModel
from typing import Dict, Any, Optional


class ApplyOnControlPlaneRQ(BaseModel):
    change_id: int
    entity_definition: Dict[str, Any]


class DeleteFromControlPlaneRQ(BaseModel):
    change_id: int
    api_version: str
    kind: str
    name: str
    namespace: Optional[str] = None
