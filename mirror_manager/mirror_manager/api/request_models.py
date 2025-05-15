from pydantic import BaseModel
from typing import Dict, Any


class ApplyOnControlPlaneRQ(BaseModel):
    change_id: int
    entity_definition: Dict[str, Any]
