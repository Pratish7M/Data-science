import mysql.connector
from mysql.connector import Error

try :
    #define the connection parameters
    connectionxxx = mysql.connector.connect(
        host = "localhost",
        # database = 'tour_database',
        user = 'root',
        password = 'root'

    )
    
    if connectionxxx.is_connected():
        db_info = connectionxxx.get_server_info()
        print(f"connection to mysql server {db_info}")

        mycursor = connectionxxx.cursor()
        mycursor.execute("SHOW DATABASES")
        for x in mycursor :
            print(x)

except Error as e :
    print(f"Error while connecting to MySql : {e}")

finally :
    if connectionxxx.is_connected() :
        mycursor.close()
        connectionxxx.close()
        print(" MySql connection is closed")

