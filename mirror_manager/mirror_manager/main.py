from fastapi import FastAPI
from mirror_manager.api.request_models import ControlPlaneApplyRQ, ControlPlaneDeleteRQ
from mirror_manager.api.response_models import ControlPlaneApplyRS, ControlPlaneDeleteRS
from mirror_manager.control_plane.control_plane_service import ControlPlaneService

app = FastAPI()
control_plane_service = ControlPlaneService()

@app.post("/apply")
async def apply_resource(rq: ControlPlaneApplyRQ) -> ControlPlaneApplyRS:
    return await control_plane_service.apply(rq.change_id, rq.entity_definition)

@app.delete("/delete")
async def delete_resource(rq: ControlPlaneDeleteRQ) -> ControlPlaneDeleteRS:
    return await control_plane_service.delete(rq.change_id, rq.api_version, rq.kind, rq.name, rq.namespace)
