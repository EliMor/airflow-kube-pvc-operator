from airflow_kbo import KubernetesBaseOperator
from airflow_kpvco.kubernetes_pvc_manager import KubernetesPVCManager, KubernetesPVCYaml

class KubernetesPVCOperator(KubernetesBaseOperator):
    """
    Opinionated operator for kubernetes PVC type management.
    Only allow client to pass in yaml files
    """
    def __init__(self, command, **kwargs):
        super().__init__(**kwargs)
        self.command = command.lower()

    def execute(self, context):
        dag = context["dag"]
        yaml_obj = self.get_rendered_template(dag)
        kpy = KubernetesPVCYaml(yaml_obj)
        kpm = KubernetesPVCManager(kpy.yaml)
        if self.command == 'create':
            kpm.create()
        elif self.command == 'delete':
            kpm.delete()

