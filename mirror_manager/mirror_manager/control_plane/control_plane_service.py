from fastapi import HTTPException
from kubernetes import config, client
from kubernetes.config.config_exception import ConfigException
from kubernetes.dynamic import DynamicClient

from mirror_manager.api.response_models import ApplyOnControlPlaneRS


class ControlPlaneService:
    def __init__(self):
        try:
            config.load_incluster_config()
        except ConfigException:
            config.load_kube_config()
        self.k8s_client = DynamicClient(client.ApiClient())

    def apply(self, entity_definition: dict, change_id: int) -> ApplyOnControlPlaneRS:
        try:
            api_version = entity_definition.get('apiVersion')
            kind = entity_definition.get('kind')
            dynamic_resource = self.k8s_client.resources.get(api_version=api_version, kind=kind)
            obj = dynamic_resource.create(body=entity_definition)
            return {"message": f"{kind} {obj.metadata.name} applied successfully", "stdout": str(obj)}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def delete(self, api_version: str, kind: str, name: str, namespace: str = None, change_id: int = None) -> dict:
        try:
            dynamic_resource = self.k8s_client.resources.get(api_version=api_version, kind=kind)
            if namespace:
                dynamic_resource.namespace(namespace).delete(name=name)
            else:
                dynamic_resource.delete(name=name)
            return {"message": f"{kind} {name} deleted successfully", "stdout": "Resource deleted successfully."}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
