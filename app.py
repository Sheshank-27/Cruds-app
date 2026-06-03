from flask import Flask, request, redirect
import pymysql

app = Flask(__name__)

def get_connection():
    return pymysql.connect(
        host="employee-db.cv4mok8i6rh5.ap-south-1.rds.amazonaws.com",
        user="admin",
        password="Sheshank123",
        database="employee_db",
        port=3306
    )

@app.route("/")
def home():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    connection.close()

    html = """
    <h1>Employee Management System -ci-cd-test</h1>

    <form action='/add' method='post'>
        Name: <input type='text' name='name'><br><br>
        Department: <input type='text' name='department'><br><br>
        <input type='submit' value='Add Employee'>
    </form>

    <hr>

    <h2>Employees</h2>
    """

    for emp in employees:
        html += f"""
        ID: {emp[0]} |
        Name: {emp[1]} |
        Department: {emp[2]}
        <a href='/delete/{emp[0]}'>Delete</a>
        <br><br>
        """

    return html

@app.route("/add", methods=["POST"])
def add_employee():
    name = request.form["name"]
    department = request.form["department"]

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO employees(name, department) VALUES(%s,%s)",
        (name, department)
    )

    connection.commit()
    connection.close()

    return redirect("/")

@app.route("/delete/<int:id>")
def delete_employee(id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM employees WHERE id=%s",
        (id,)
    )

    connection.commit()
    connection.close()

    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")