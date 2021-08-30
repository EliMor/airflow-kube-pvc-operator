from kubernetes.client.rest import ApiException

from airflow_kbo.kubernetes_util import get_kube_client, base_yaml_validator
from airflow_kpvco.kubernetes_util import get_kube_pvc_client

class KubernetesPVCYaml:
    def __init__(self, yaml):
        base_yaml_validator(yaml, kind='PersistentVolumeClaim')
        self.yaml = yaml
    # other validation checks here

class KubernetesPVCManager:
    def __init__(self, yaml):
        self.yaml = yaml

    def create(self):
        ...
    def delete(self):
        ... 