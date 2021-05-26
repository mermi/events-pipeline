import datetime
import logging
from shared_utils.load_json_data import load_json_postgres

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresHook

from shared_utils.schema_verification import validate_data as validator
from shared_utils.dag_utils.utils import get_query as get_query
from shared_utils.load_json_data import load_json_postgres as raw_loader

DAG_ID = 'events_flow'
POSTGRES_CONN_ID = 'postgres'
BASE_SQL_PATH = f'sql/{DAG_ID}'
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


# def etl():
#     create_query = get_query(
#         f'{BASE_SQL_PATH}/create_staging/create_staging_table', extension='sql')
#     hook = PostgresHook(postgres_conn_id=POSTGRES_CONN_ID)
#     with hook.get_conn() as conn:
#         raw_data = raw_loader(conn=conn, query=create_query)
    
    
    # load to final table


validate_data = PythonOperator(
    dag=dag,
    task_id='validate_data',
    python_callable=validator
)


# load_data = PythonOperator(
#     dag=dag,
#     task_id='load_data',
#     python_callable=etl
# )
