import mysql.connector

#creating connection
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "georgemollel123!@#",
    database = "NMB"
)

mycursor = mydb.cursor()




mycursor.execute("")

mydb.commit()