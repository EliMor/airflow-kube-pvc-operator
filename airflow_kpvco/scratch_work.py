## Ideas for how the client will engage with this.

## workflow 1
from airflow import DAG
from datetime import datetime, timedelta
from airflow_kjo import KubernetesJobOperator
from airflow_kpvco import KubernetesPVCOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1, # the number of times the pod will retry, can pass in per-task
    'retry_delay': timedelta(minutes=5), 
    'start_date': datetime(2021, 2, 24, 12, 0),
}
with DAG(
    'kubernetes_job_operator',
    default_args=default_args,
    description='KJO example DAG',
    schedule_interval=None,
    catchup=False
) as dag:
    task_1 = KubernetesPVCOperator(task_id='create_pvc', 
                                   yaml_file_name='/path/to/airflow/kubernetes/pvc/1gb_pvc.yaml',
                                   command='create')

    task_2 = KubernetesJobOperator(task_id='example_kubernetes_job_operator',
                                   yaml_file_name='/path/to/airflow/kubernetes/job/do_a_job.yaml',
                                   in_cluster=True)

    task_3 = KubernetesJobOperator(task_id='example_kubernetes_job_operator_2',
                                   yaml_file_name='/path/to/airflow/kubernetes/job/do_a_job_2.yaml',
                                   in_cluster=True)

    task_4 = KubernetesPVCOperator(task_id='delete_pvc',
                                   yaml_file_name='/path/to/airflow/kubernetes/pvc/1gb_pvc.yaml',
                                   command='delete')
    
    task_1 >> task_2 >> task_3 >> task_4
####


## workflow 2
from airflow import DAG
from datetime import datetime, timedelta
from airflow_kjo import KubernetesJobOperator
from airflow_kpvco import KubernetesPVCOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1, # the number of times the pod will retry, can pass in per-task
    'retry_delay': timedelta(minutes=5), 
    'start_date': datetime(2021, 2, 24, 12, 0),
}
with DAG(
    'kubernetes_job_operator',
    default_args=default_args,
    description='KJO example DAG',
    schedule_interval=None,
    catchup=False
) as dag:

    with KubernetesPVCOperator(task_id='pvc_for_jobs') as pvc_across_jobs:
        # display as a task group
        # create pvc
        task_1 = KubernetesJobOperator(task_id='example_kubernetes_job_operator',
                                    yaml_file_name='/path/to/airflow/kubernetes/job/do_a_job.yaml',
                                    in_cluster=True)

        task_2 = KubernetesJobOperator(task_id='example_kubernetes_job_operator_2',
                                    yaml_file_name='/path/to/airflow/kubernetes/job/do_a_job_2.yaml',
                                    in_cluster=True)
        task_1 >> task_2
        #delete pvc

## workflow 3
from airflow import DAG
from datetime import datetime, timedelta
from airflow_kjo import KubernetesJobOperator
from airflow_kpvco import KubernetesPVCOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1, # the number of times the pod will retry, can pass in per-task
    'retry_delay': timedelta(minutes=5), 
    'start_date': datetime(2021, 2, 24, 12, 0),
}
with DAG(
    'kubernetes_job_operator',
    default_args=default_args,
    description='KJO example DAG',
    schedule_interval=None,
    catchup=False
) as dag:

    # yaml has pvc bound within it already, autodetect and manage its life along with the Job
    task_1 = KubernetesJobOperator(task_id='example_kubernetes_job_operator',
        yaml_file_name='/path/to/airflow/kubernetes/job/do_a_job_with_pvc.yaml',
        in_cluster=True)
