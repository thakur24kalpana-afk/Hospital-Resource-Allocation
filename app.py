from flask import Flask, render_template, request, redirect
from pulp import *

app = Flask(__name__)

# LOGIN PAGE
@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == "admin" and password == "1234":
            return redirect('/dashboard')

    return render_template("login.html")


# DASHBOARD
@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
    result = None

    if request.method == 'POST':
        beds = int(request.form.get('beds', 100))
        ventilators = int(request.form.get('ventilators', 50))

        model = LpProblem("Hospital_Allocation", LpMaximize)

        x1 = LpVariable('Critical', lowBound=0)
        x2 = LpVariable('Serious', lowBound=0)
        x3 = LpVariable('Mild', lowBound=0)

        model += 10*x1 + 6*x2 + 2*x3

        model += x1 + x2 + x3 <= beds
        model += x1 + 0.5*x2 <= ventilators

        model.solve()

        result = {
            "critical": x1.value(),
            "serious": x2.value(),
            "mild": x3.value(),
            "score": value(model.objective)
        }

    return render_template("dashboard.html", result=result)


if __name__ == '__main__':
    app.run(debug=True)