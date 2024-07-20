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
        mycursor.execute(" CREATE DATABASE if not exists test1")
        # mycursor.execute("SHOW DATABASES ")

except Error as e :
    print(f"Error while connecting to MySql : {e}")

else :
    mycursor.close()      
    if connectionxxx.is_connected():
        connectionxxx.close()
        print(" MySql connection is closed")

