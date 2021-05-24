import sqlalchemy as db
from sqlalchemy.engine import URL

server = 'localhost'
database = 'TestDatabase'
username = 'SA'
password = 'YourStrong@Passw0rd'

connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password

connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})

engine = db.create_engine(connection_url)

connection = engine.connect()

results = connection.execute('SELECT * FROM MyTable')

row_list = results.fetchall()

print(row_list)