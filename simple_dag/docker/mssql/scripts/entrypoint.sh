#!/bin/bash
database=TestDatabase
wait_time=10s
user=SA
password=YourStrong@Passw0rd

# wait for SQL Server to come up
echo ·········· importing data will start in $wait_time...
sleep $wait_time
echo ·········· importing data...

echo ·········· Create DATABASE AND TABLES
/opt/mssql-tools/bin/sqlcmd -S localhost -U $user -P $password -i /var/opt/mssql/scripts/DDL.sql

echo ·········· Import data from CSV file
sleep 1s
/opt/mssql-tools/bin/bcp TestDatabase.dbo.MyTable in "/var/opt/mssql/scripts/MyTable.csv" -c -t',' -S localhost -U $user -P $password