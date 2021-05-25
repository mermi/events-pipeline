import logging
from sqlalchemy import create_engine
import json

from pandas.io.json import json_normalize

from shared_utils.dag_utils.utils import get_query as get_query

logger = logging.getLogger(f'logging_steps')


def create_table(conn, create_query):
    cur=conn.cursor()
    cur.execute(create_query)
    conn.commit() 


def load_json_postgres(conn, create_query):
    with open('shared_utils/data/flink_data_engieering_sample_data.json', 'r') as data_file:
        data = json.load(data_file)
    create_table(conn, create_query)
    df = json_normalize(data)

    engine = create_engine(conn)
    df.to_sql("stafing.events", engine, index=False, if_exists='append')
    logger.info("table created")
