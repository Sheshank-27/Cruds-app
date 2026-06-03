import pymysql

connection = pymysql.connect(
    host="employee-db.cv4mok8i6rh5.ap-south-1.rds.amazonaws.com",
    user="admin",
    password="Sheshank123",
    port=3306
)

print("connected successfully!")
connection.close()