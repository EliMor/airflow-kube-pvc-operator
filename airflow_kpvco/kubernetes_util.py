from kubernetes import client as k_client

def get_kube_pvc_client(kube_client):
    """
    base operator has util for getting kube_client objects
    """
    core_api = k_client.CoreV1Api(api_client=kube_client)
    return core_api


