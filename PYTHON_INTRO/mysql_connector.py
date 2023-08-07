import mysql.connector

#creating connection
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "georgemollel123!@#",
    #database = "GLOBAL_FOUNDATION"#database name 
)

#cursor object accesses the database
mycursor = mydb.cursor()


mycursor.execute("CREATE DATABASE GLOBAL_FOUNDATION")
