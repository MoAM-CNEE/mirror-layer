from fastapi import HTTPException
from kubernetes import config
from kubernetes.client import ApiException
from kubernetes.config.config_exception import ConfigException
from kubernetes.dynamic import DynamicClient

from mirror_manager.api.response_models import ApplyOnControlPlaneRS


class ControlPlaneService:
    def __init__(self):
        try:
            config.load_incluster_config()
        except ConfigException:
            config.load_kube_config()
        self.k8s_client = DynamicClient(config.new_client_from_config())

    def apply(self, entity_definition: dict, change_id: int) -> ApplyOnControlPlaneRS:
        try:
            api_version = entity_definition.get("apiVersion")
            kind = entity_definition.get("kind")
            resource = self.k8s_client.resources.get(api_version=api_version, kind=kind)

            name = entity_definition["metadata"]["name"]
            namespace = entity_definition["metadata"].get("namespace", "default")
            updated = False
            try:
                existing_resource = resource.get(name=name, namespace=namespace)
                existing_resource.update(body=entity_definition)
                updated = True
            except ApiException as e:
                if e.status == 404:
                    resource = self.k8s_client.resources.get(api_version=api_version, kind=kind)
                    resource.create(body=entity_definition)
                else:
                    raise HTTPException(status_code=500, detail={"change_id": change_id, "error": str(e)})
            return ApplyOnControlPlaneRS(change_id=change_id, updated=updated)
        except Exception as e:
            raise HTTPException(status_code=500, detail={"change_id": change_id, "error": str(e)})
