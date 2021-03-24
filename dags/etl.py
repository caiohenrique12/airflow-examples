from datetime import datetime, timedelta

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'caiohenrique',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}
dag = DAG(
    'etl',
    default_args=default_args,
    description='A simple ETL',
    schedule_interval=timedelta(days=1),
    start_date=datetime.now(),
    tags=['example'],
)

t1 = BashOperator(
    task_id='donwload_csv',
    dag=dag,
    bash_command="""
    cd $AIRFLOW_HOME/dags/etl_scripts/
    python3 download_file.py
   """)

t2 = BashOperator(
    task_id='execute_partner_etl',
    dag=dag,
    depends_on_past=True,
    bash_command="""
    cd $AIRFLOW_HOME/dags/etl_scripts/
    python3 socios_etl.py
    """)

t3 = BashOperator(
    task_id='execute_business_etl',
    dag=dag,
    depends_on_past=True,
    bash_command="""
    cd $AIRFLOW_HOME/dags/etl_scripts/
    python3 empresas_etl.py
    """)

t1 >> [t2, t3]
