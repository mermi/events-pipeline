FROM apache/airflow:2.0.2-python3.8

ARG AIRFLOW_USER_HOME=/usr/local/airflow
ENV AIRFLOW_HOME=${AIRFLOW_USER_HOME}

USER root

COPY config/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh


# Needed line just when adding libraries
ENV PYTHONPATH ${AIRFLOW_HOME}:${AIRFLOW_HOME}/shared_utils:$PYTHONPATH

USER airflow
# install extra requirements
COPY requirements.txt /
RUN pip install --user --no-cache-dir -r /requirements.txt


# copy config and artifacts after install requirements to avoid to install requirements on each code change
# add always chwown to each COPY to make airflow the owner
COPY --chown=airflow:airflow config/airflow.cfg ${AIRFLOW_USER_HOME}/airflow.cfg
COPY --chown=airflow:airflow dags ${AIRFLOW_HOME}/dags

COPY --chown=airflow:airflow shared_utils ${AIRFLOW_HOME}/shared_utils
COPY --chown=airflow:airflow sql ${AIRFLOW_HOME}/sql

EXPOSE 8080

WORKDIR ${AIRFLOW_USER_HOME}
ENTRYPOINT ["/entrypoint.sh"]
CMD ["webserver"]