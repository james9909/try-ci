import sqlite3

def initialize_tables():
    database = "database.db"
    db = sqlite3.connect(database)
    c = db.cursor()

    q = "CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)"
    c.execute(q)

    db.commit()
    db.close()
    return db

if __name__ == "__main__":
    initialize_tables()
