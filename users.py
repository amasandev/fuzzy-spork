import sqlite3

def get_user(name):
    conn = sqlite3.connect("users.db")
    row = conn.execute(f"SELECT * FROM users WHERE name = '{name}'").fetchone()
    return {"id": row[0], "name": row[1]}
