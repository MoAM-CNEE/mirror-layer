from fastapi import FastAPI
from mirror_manager.api.request_models import ApplyOnControlPlaneRQ
from mirror_manager.control_plane.control_plane_service import ControlPlaneService

app = FastAPI()
control_plane_service = ControlPlaneService()

@app.post("/apply")
def apply_resource(rq: ApplyOnControlPlaneRQ):
    return control_plane_service.apply(rq.entity_definition, rq.change_id)
