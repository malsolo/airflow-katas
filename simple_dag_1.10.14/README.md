# Simple dag 1.10.14

For testing schedulers with airflow 1.10.14.

## Steps

1. Use docker compose from within the project

$ docker-compose -f docker-compose-LocalExecutor.yml up

You can also try:

$ docker-compose -f docker-compose-CeleryExecutor.yml up

2. Open http://localhost:8080/admin/

3. Create virtualenv

$ cd simple_dag_1.10.14/

$ virtualenv venv -p /usr/local/bin/python3.7

$ source venv/bin/activate

$ python -V
Python 3.7.10

4. Add the the required dependencies

Follow these instructions: https://airflow.readthedocs.io/en/1.10.14/installation.html

$ export AIRFLOW_VERSION=1.10.14
$ export PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
# For example: 3.7
$ export CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
# For example: https://raw.githubusercontent.com/apache/airflow/constraints-1.10.14/constraints-3.7.txt
$ pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"


