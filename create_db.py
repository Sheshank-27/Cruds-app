import pymysql

connection = pymysql.connect(
    host="employee-db.cv4mok8i6rh5.ap-south-1.rds.amazonaws.com",
    user="admin",
    password="Sheshank123",
    port=3306
)

cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS employee_db")

print("Database created successfully!")

connection.close()