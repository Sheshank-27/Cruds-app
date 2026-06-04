from flask import Flask, request, redirect

app = Flask(__name__)

employees = []

@app.route("/")
def home():
    html = """
    <h1>Employee Management System-2</h1>

    <form action="/add" method="post">
        Name: <input type="text" name="name"><br><br>
        Department: <input type="text" name="department"><br><br>
        <input type="submit" value="Add Employee">
    </form>

    <hr>

    <h2>Employees</h2>
    """

    for i, emp in enumerate(employees):
        html += f"""
        ID: {i}<br>
        Name: {emp['name']}<br>
        Department: {emp['department']}<br>
        <a href='/delete/{i}'>Delete</a>
        <br><br>
        """

    return html


@app.route("/add", methods=["POST"])
def add_employee():
    employees.append({
        "name": request.form["name"],
        "department": request.form["department"]
    })

    return redirect("/")


@app.route("/delete/<int:id>")
def delete_employee(id):
    if 0 <= id < len(employees):
        employees.pop(id)

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)