import mysql.connector

print("hhhhhhhh")

    #
def databaseconnection():

    conn = mysql.connector.connect(user='toad', password='Blast@123',
                          host='toadai.database.windows.net', database='toad')
                        #   auth_plugin='mysql_native_password')
    cursor=conn.cursor()
    print("commmmmmm")
    return cursor,conn