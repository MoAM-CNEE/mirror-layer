from fastapi import FastAPI
from mirror_manager.api.request_models import ControlPlaneApplyRQ, ControlPlaneDeleteRQ
from mirror_manager.control_plane.control_plane_service import ControlPlaneService

app = FastAPI()
control_plane_service = ControlPlaneService()

@app.post("/apply")
def apply_resource(rq: ControlPlaneApplyRQ):
    return control_plane_service.apply(rq.entity_definition, rq.change_id)

@app.delete("/delete")
async def delete_resource(rq: ControlPlaneDeleteRQ):
    return control_plane_service.delete(rq.api_version, rq.kind, rq.name, rq.namespace)
