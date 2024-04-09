import pyodbc
class SQLConnection:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn = None

    def connect(self):
        try:
            conn_str = f"DRIVER={{SQL Server Native Client 11.0}};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}"
            self.conn = pyodbc.connect(conn_str)
            print("Connected to SQL Server successfully!")
        except Exception as e:
            print(f"Error connecting to SQL Server: {e}")

    def execute_query(self, query):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print("Error executing query: {e}")

    def close_connection(self):
        if self.conn:
            self.conn.close()
            print("Connection closed.")


if __name__ == "__main__":
    server = 'WPO1L5CG94404BY\\SQLEXPRESS'
    username = 'sa'
    password = 'Asap123#'
    database = 'AdventureWorks'
    sql_conn = SQLConnection(server, database,
                             username, password)
    sql_conn.connect()
    query = "SELECT count(*) FROM AdventureWorks.SalesLT.Customer"
    results = sql_conn.execute_query(query)
    for row in results:
        print(row)

    sql_conn.close_connection()

