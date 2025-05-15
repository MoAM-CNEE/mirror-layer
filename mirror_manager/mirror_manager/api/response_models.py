from pydantic import BaseModel


class ApplyOnControlPlaneRS(BaseModel):
    change_id: int
    updated: bool
