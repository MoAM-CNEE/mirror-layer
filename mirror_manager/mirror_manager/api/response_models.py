from pydantic import BaseModel


class ControlPlaneApplyRS(BaseModel):
    change_id: int
    updated: bool


class ControlPlaneDeleteRS(BaseModel):
    change_id: int
