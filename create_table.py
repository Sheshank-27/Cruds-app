import pymysql

connection = pymysql.connect(
    host="employee-db.cv4mok8i6rh5.ap-south-1.rds.amazonaws.com",
    user="admin",
    password="Sheshank123",
    database="employee_db",
    port=3306
)

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100)
)
""")

connection.commit()

print("Employees table created successfully!")

connection.close()