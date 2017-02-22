from flask import Flask, render_template, request, session, redirect, url_for, json
import os
from utils import accountManager, initialize
import math

app = Flask(__name__)
#establish secret key for session
with open("utils/key", "a+b") as f:
    secret_key = f.read()
    if not secret_key:
        secret_key = os.urandom(64)
        f.write(secret_key)
        f.flush()
    app.secret_key = secret_key

#home route
@app.route("/")
def index():
    if "username" in session:
        return redirect("/loggedIn")
    else:
        return render_template("loginOrReg.html")

#diplayed when logged in
@app.route("/loggedIn")
def loggedIn():
    if "username" in session:
        return render_template("loggedIn.html")
    else:
        return redirect("/")

#login route
@app.route("/login", methods=["POST"])
def login():
    form = request.form
    username = form["username"]
    password = form["password"]
    success, message = accountManager.authenticate(username, password)
    if success:
        session["username"] = username
        return redirect("/")
    return render_template("loginOrReg.html",status=message)

#register route
@app.route("/register", methods=["POST"])
def register():
    form = request.form
    username = form["username"]
    password = form["password"]
    pwd = form["pwd"]
    success, message = accountManager.register(username, password, pwd)
    return render_template("loginOrReg.html",status=message)

#logout route
@app.route("/logout", methods=["POST", "GET"])
def logout():
    if "username" in session:
        session.pop("username")
        return render_template("loginOrReg.html",status="logged out")
    else:
        return redirect(url_for("index"))

#returns fib(n) for ajax call
@app.route("/fib", methods=["POST","GET"])
def fib():
    n = request.form.get("n")
    n = int(n)
    Phi = (1 + math.sqrt(5)) / 2.0
    phi = (1 - math.sqrt(5)) / 2.0
    answer = math.floor((math.pow(Phi, n) - math.pow(phi, n)) / math.sqrt(5))
    result = {"result": answer}
    return json.dumps(result)

#returns the sum of two numbers for ajax call
@app.route("/add", methods=["POST","GET"])
def add():
    a = request.form.get("a")
    b = request.form.get("b")
    a , b = int(a), int(b)
    answer = a + b
    result = {"result": answer}
    return json.dumps(result)

#run
if __name__ == "__main__":
    initialize.initialize_tables()
    app.debug = True
    app.run()
