import mysql.connector

#creating connection
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "georgemollel123!@#",
    database = "GLOBAL_FOUNDATION"#database name 
)

#cursor object accesses the database
mycursor = mydb.cursor()


mycursor.execute("")

for x in mycursor:
    print(x)
"""
sql = "INSERT INTO customers (ACCOUNT_No,PIN) VALUES (%s,%d)"
val = (41112097890,1234)
mycursor.execute(sql,val)

mycursor.commit()
"""

