import sys
sys.path.insert(0, 'C:\\Users\\MU59BM\\source\\repos\\PythonTraining')
from Authentication.sqlconnect import SQLConnection
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Server Works!'


@app.route('/greet')
def say_hello():
    return 'Hello from Server'

@app.route('/customer')
def customer():
    return customerData()

def customerData():
    server = 'WPO1L5CG94404BY\\SQLEXPRESS'
    username = 'sa'
    password = 'Asap123#'
    database = 'AdventureWorks'
    sql_conn = SQLConnection(server, database,username, password)
    sql_conn.connect()
    query = "SELECT * FROM AdventureWorks.SalesLT.Customer"
    result = sql_conn.execute_query(query)
    sql_conn.close_connection()
    return result
