from fastapi import HTTPException
from kubernetes import config, client
from kubernetes.client import ApiException
from kubernetes.config.config_exception import ConfigException
from kubernetes.dynamic import DynamicClient

from mirror_manager.api.response_models import ApplyOnControlPlaneRS, DeleteFromControlPlaneRS


class ControlPlaneService:
    def __init__(self):
        try:
            config.load_incluster_config()
        except ConfigException:
            config.load_kube_config()
        self.k8s_client = DynamicClient(client.ApiClient())

    async def apply(self, change_id: int, entity_definition: dict) -> ApplyOnControlPlaneRS:
        try:
            api_version = entity_definition.get('apiVersion')
            kind = entity_definition.get('kind')
            name = entity_definition.get('metadata', {}).get('name')
            dynamic_resource = self.k8s_client.resources.get(api_version=api_version, kind=kind)
            updated = False
            try:
                dynamic_resource.patch(name=name, body=entity_definition,
                                       content_type='application/merge-patch+json')
                updated = True
            except ApiException as e:
                if e.status == 404:
                    dynamic_resource.create(body=entity_definition)
                else:
                    raise e
            return ApplyOnControlPlaneRS(change_id=change_id, updated=updated)
        except Exception as e:
            print(f"[ERROR] change_id={change_id}, detail={str(e)}")
            raise HTTPException(status_code=500, detail=str(e))

    async def delete(self, change_id: int, api_version: str, kind: str, name: str,
               namespace: str = None) -> DeleteFromControlPlaneRS:
        try:
            dynamic_resource = self.k8s_client.resources.get(api_version=api_version, kind=kind)
            if namespace:
                dynamic_resource.namespace(namespace).delete(name=name)
            else:
                dynamic_resource.delete(name=name)
            return DeleteFromControlPlaneRS(change_id=change_id)
        except Exception as e:
            print(f"[ERROR] change_id={change_id}, detail={str(e)}")
            raise HTTPException(status_code=500, detail=str(e))
