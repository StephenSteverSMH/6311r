from flask import Flask
import pymssql
app = Flask(__name__)

#pipreqs

@app.route('/')
def index():
    #conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:6331server1.database.windows.net,1433;Database=database1;Uid=Stephen6331;Pwd=Password6331;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
    conn = pymssql.connect(server='6331server1.database.windows.net', port=1433, user='Stephen6331', password='Password6331', database='database1')
    return 'hello world!'

if __name__ == '__main__':
    app.run()