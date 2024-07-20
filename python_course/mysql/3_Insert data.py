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
        mycursor.execute( " insert into test.test_table values(22,'pratish',5.9,1,'Data Scientist')") # always write string in ' '
        connectionxxx.commit()
        mycursor.execute(" SELECT * FROM test.test_table")
        for i in mycursor.fetchall() :
            print(i)

        mycursor.execute(" SELECT c1,c2 FROM test.test_table")
        for i in mycursor.fetchall() :
            print(i)

except Error as e :
    print(f"Error while connecting to MySql : {e}")

else :
    mycursor.close()      
    if connectionxxx.is_connected():
        connectionxxx.close()
        print(" MySql connection is closed")

