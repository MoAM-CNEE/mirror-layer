from fastapi import FastAPI
from mirror_manager.api.request_models import ApplyOnControlPlaneRQ, DeleteFromControlPlaneRQ
from mirror_manager.api.response_models import ApplyOnControlPlaneRS, DeleteFromControlPlaneRS
from mirror_manager.control_plane.control_plane_service import ControlPlaneService

app = FastAPI()
control_plane_service = ControlPlaneService()

@app.post("/apply")
async def apply_resource(rq: ApplyOnControlPlaneRQ) -> ApplyOnControlPlaneRS:
    return await control_plane_service.apply(rq.change_id, rq.entity_definition)

@app.delete("/delete")
async def delete_resource(rq: DeleteFromControlPlaneRQ) -> DeleteFromControlPlaneRS:
    return await control_plane_service.delete(rq.change_id, rq.api_version, rq.kind, rq.name, rq.namespace)
