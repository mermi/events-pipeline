import datetime
import logging

from airflow import DAG
from airflow.operators.python import PythonOperator

from shared_utils.schema_verification import validate_data as validator

DAG_ID = 'events_flow'
POSTGRES_CONN_ID = 'postgres'
BASE_SQL_PATH = f'sql/postgres/{DAG_ID}'
TARGET_TABLE = 'FLINK.EVENTS'


logger = logging.getLogger(f'postgres.{DAG_ID}')


default_args = {
    'owner': 'Manel',
    'depends_on_past': False,
    'start_date': datetime.datetime(2021, 5, 10),
    'retries': 1,
    'retry_delay': datetime.timedelta(seconds=5),
    'execution_timeout': datetime.timedelta(minutes=15)
}


dag = DAG(
    DAG_ID,
    default_args=default_args,
    description='A DAG that validate JSON events and load them to postgres db',
    schedule_interval='00 9,15 * * *',
    tags=[DAG_ID, 'postgres', 'events']
)

validate_data = PythonOperator(
    dag=dag,
    task_id='validate_data',
    python_callable=validator
)