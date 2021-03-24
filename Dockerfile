FROM apache/airflow:latest

USER airflow

RUN pip install pip --upgrade

COPY requirements.txt $AIRFLOW_HOME/requirements.txt

ARG DAGS_FOLDER="dags/"
ENV DAGS_FOLDER=${DAGS_FOLDER}

COPY dags/ $AIRFLOW_HOME/dags/

ARG PLUGINS_FOLDER="plugins/"
ENV PLUGINS_FOLDER=${PLUGINS_FOLDER}

COPY plugins/ $AIRFLOW_HOME/plugins/
