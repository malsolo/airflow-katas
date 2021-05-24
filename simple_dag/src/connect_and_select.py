import pyodbc


def printResults(rows):
        if len(rows)==0:
                print('No rows returned')
        else:
                print(str(len(rows)) + ' row(s) returned:')        
                print(', '.join(c[0] for c in rows[0].cursor_description))
                for row in rows:
                        print(', '.join(str(value) for value in row))


def printResultsInfo(cursor):
        print('Result description:')
        for column in cursor.description:
                print('Name: ' + column[0])
                print('Python type: ' + str(column[1]))
                print('Nullable: ' + str(column[6]))


server = 'localhost'
database = 'TestDatabase'
username = 'SA'
password = 'YourStrong@Passw0rd'

connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password

with pyodbc.connect(connectionString) as connection:
    cursor = connection.cursor()

    cursor.execute("SELECT @@version;") 
    rows = cursor.fetchall() 

    #note the -1 return for a SELECT
    print('Cursor row count: ' + str(cursor.rowcount))

    #print results
    printResultsInfo(cursor)
    printResults(rows)
    input('Press Enter to continue...')

    sql = "SELECT * FROM MyTable;"

    cursor.execute(sql)
    my_table_rows = cursor.fetchall()

    #note the -1 return for a SELECT
    print('Cursor row count: ' + str(cursor.rowcount))

    #print results
    printResultsInfo(cursor)
    printResults(my_table_rows)
    
    print('End.')
