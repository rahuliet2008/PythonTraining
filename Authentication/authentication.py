from Authentication.sqlconnect import SQLConnection


class DataProcessor:

    def __init__(self, sql_conn):
        self.sql_conn = sql_conn

    def process_data(self):
        query = "SELECT * FROM AdventureWorks.SalesLT.Customer"
        result = self.sql_conn.execute_query(query)
        print(type(result))

    def Authenticate(self,username,password):
        try:
            query = "SELECT * FROM AdventureWorks.SalesLT.Customer where EmailAddress = '{}'".format(username)
            result = self.sql_conn.execute_query(query)
            records=0
            for row in result:
                records+=1
                print(row)
                print(records)
            print(records)
            if(int(records)>0):
               print("you are authenticated")
            else:
               print("you are not authenticated")
               raise Exception("you are not authenticated")

        except Exception as e:
            print(e)


# Example usage:
if __name__ == "__main__":
    server = 'WPO1L5CG94404BY\\SQLEXPRESS'
    username = 'sa'
    password = 'Asap123#'
    database = 'AdventureWorks'
    sql_conn = SQLConnection(server, database,username, password)
    sql_conn.connect()
    data_processor = DataProcessor(sql_conn)
    data_processor.process_data()
    username=input('Enter your username: ')
    data_processor.Authenticate(username,password)
    sql_conn.close_connection()
