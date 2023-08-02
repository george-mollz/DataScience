import mysql.connector

#creating connection
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "georgemollel123!@#",
    database = "NMB"#database name 
)

#cursor object accesses the database
mycursor = mydb.cursor()



#creating table customers with fields id and account
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, account VARCHAR(255)")

mydb.commit()