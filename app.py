from flask import Flask, render_template, request, session, redirect, url_for
import hashlib
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
    if 'username' in session:
        return redirect("/loggedIn")
    else:
        return render_template("loginOrReg.html")

@app.route("/loggedIn")
def loggedIn():
    if 'username' in session:
        return render_template("loggedIn.html")
    else:
        return redirect("/")

@app.route("/login", methods=["POST"])
def login():
    formDict = request.form
    username = formDict["username"]
    password = formDict["password"]
    loginStatus = ""
    if  accountManager.authenticate(username,password): #returns true or false
        loginStatus = "login successful"
        return render_template("loggedIn.html",status=loginStatus)
    else:
        loginStatus = "login failed"
        return render_template("loginOrReg.html",status=loginStatus)

@app.route("/register", methods=["POST"])
def register():
    formDict = request.form
    username = formDict["username"]
    password = formDict["password"]
    pwd = formDict["pwd"]  #confirm password
    registerStatus = ""
    if accountManager.register(username,password,pwd): #returns true or false
        registerStatus = "register successful"
    else :
        registerStatus = "register failed"
    return render_template("loginOrReg.html",status=registerStatus) #status is the login/creation message

#logout of user
@app.route('/logout', methods=["POST", "GET"])
def logout():
    if "username" in session:
        session.pop('username')
        return render_template("loginOrReg.html",status="logged out")
    else:
        return redirect(url_for('loginOrRegister'))

if __name__ == "__main__":
    initialize.initialize_tables()
    app.debug = True
    app.run()
