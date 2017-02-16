from flask import Flask, render_template, request, session, redirect, url_for
import os
from utils import accountManager, initialize

app = Flask(__name__)
with open("utils/key", "a+b") as f:
    secret_key = f.read()
    if not secret_key:
        secret_key = os.urandom(64)
        f.write(secret_key)
        f.flush()
    app.secret_key = secret_key

@app.route("/")
def loginOrRegister():
    if "username" in session:
        return redirect("/loggedIn")
    else:
        return render_template("loginOrReg.html")

@app.route("/loggedIn")
def loggedIn():
    if "username" in session:
        return render_template("loggedIn.html")
    else:
        return redirect("/")

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

@app.route("/register", methods=["POST"])
def register():
    form = request.form
    username = form["username"]
    password = form["password"]
    pwd = form["pwd"]
    success, message = accountManager.register(username, password, pwd)
    return render_template("loginOrReg.html",status=message)

@app.route("/logout", methods=["POST", "GET"])
def logout():
    if "username" in session:
        session.pop("username")
        return render_template("loginOrReg.html",status="logged out")
    else:
        return redirect(url_for("loginOrRegister"))

if __name__ == "__main__":
    initialize.initialize_tables()
    app.debug = True
    app.run()
