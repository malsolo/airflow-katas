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

5. Add MS Sql Server

Modify the docker compose files.

Run the containers

Try with the console:

$ docker ps
CONTAINER ID   IMAGE                                        COMMAND                  CREATED         STATUS                   PORTS                                                           NAMES
...
simple_dag_11014_mssql_1
(venv) javier@javier-Inspiron-13-5378:~/Projects/github.com/malsolo/airflow-katas/simple_dag_1.10.14$ 

$ docker exec -it simple_dag_11014_mssql_1 /bin/bash
root@e2d22766a155:/# /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P "YourStrong@Passw0rd"
1> USE TestDatabase
2> SELECT * FROM MyTable;
3> GO
Changed database context to 'TestDatabase'.
Id                                                                                                                                                                                                                                                               Value                                                                                                                                                                                                                                                           
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1                                                                                                                                                                                                                                                                Car                                                                                                                                                                                                                                                             
2                                                                                                                                                                                                                                                                Truck                                                                                                                                                                                                                                                           
3                                                                                                                                                                                                                                                                Motorcycle                                                                                                                                                                                                                                                      
4                                                                                                                                                                                                                                                                Bicycle                                                                                                                                                                                                                                                         
5                                                                                                                                                                                                                                                                Horse                                                                                                                                                                                                                                                           
6                                                                                                                                                                                                                                                                Boat                                                                                                                                                                                                                                                            
7                                                                                                                                                                                                                                                                Plane                                                                                                                                                                                                                                                           
8                                                                                                                                                                                                                                                                Scooter                                                                                                                                                                                                                                                         
9                                                                                                                                                                                                                                                                Skateboard                                                                                                                                                                                                                                                      

(9 rows affected)
1> exit
root@e2d22766a155:/# exit
exit
$