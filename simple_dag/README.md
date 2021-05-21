# Simple dag

For testing schedulers with airflow 2.0.2.

## Steps

1. Create virtualenv

$ cd simple_dag/

$ virtualenv venv

2. Use docker compose from https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html

```
$ docker-compose up
```

Go to http://localhost:8080/
Login: airflow/airflow

3. Create the first DAG (Python script)

dags/basic_dag.py

4. Add the the required dependencies

Don't forget!

$ source venv/bin/activate
(venv) $ 

Follow these instructions: https://airflow.apache.org/docs/apache-airflow/stable/start/local.html

$ export AIRFLOW_VERSION=2.0.1
$ export PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
# For example: 3.8
$ export CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
# For example: https://raw.githubusercontent.com/apache/airflow/constraints-2.0.2/constraints-3.6.txt
$ pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

