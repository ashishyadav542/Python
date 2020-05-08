import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="1234", database='myproject')
print("Success")

mycursor = mydb.cursor()

mycursor.execute("select * from student")

result = mycursor.fetchone()

print(result)
