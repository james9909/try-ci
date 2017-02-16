import hashlib
import sqlite3

def authenticate(user, password):
    f = "database.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    hashed = hashlib.sha1(password).hexdigest()

    c.execute("SELECT * FROM users WHERE username = ?", (user,))
    l = c.fetchone()

    if l == None:
        success = False
        message = "User does not exist"
    elif l[1] == hashed:
        success = True
        message = "Logged in"
    else:
        success = False
        message = "Invalid credentials"

    db.commit()
    db.close()
    return success, message

def register(user, password, password_confirm):
    f="database.db"
    db = sqlite3.connect(f)
    c = db.cursor()

    c.execute("SELECT * FROM users WHERE username = ?", (user,))
    result = c.fetchone()

    if result:
        success = False
        message = "Username taken"
    elif password != password_confirm:
        success = False
        message = "Passwords do not match"
    elif password == password_confirm:
        hashed = hashlib.sha1(password).hexdigest()
        c.execute("INSERT INTO users VALUES (?, ?)", (user, hashed,))

        success = True
        message = "User registered"

    db.commit()
    db.close()
    return success, message
