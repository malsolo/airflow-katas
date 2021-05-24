from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from tables.MyTable import MyTable

engine = create_engine(
    "mssql+pyodbc://SA:YourStrong@Passw0rd@localhost:1433/TestDatabase"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)

Session = sessionmaker(bind=engine)

session = Session()

for value in session.query(MyTable):
    print(value)

