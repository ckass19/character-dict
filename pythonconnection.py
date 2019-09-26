

import mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='project',
                                         user='root',
                                         password='Ordinateur19')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connection is successful!", db_Info)
        cursor = connection.cursor()
        cursor.execute("SELECT Standard FROM charlist")
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
        print(myresult)
#        cursor.execute("select database();")
#        record = cursor.fetchone()
#        print("You're connected to - ", record)
except Error as e:
    print("Error while connecting to MYSQL", e)
finally:
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
