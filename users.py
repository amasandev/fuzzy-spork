import sqlite3

def get_user(name):
    conn = sqlite3.connect("users.db")
    try:
        row = conn.execute(
            "SELECT * FROM users WHERE name = ?",
            (name,)
        ).fetchone()

        if row is None:
            return None

        return {"id": row[0], "name": row[1]}
    finally:
        conn.close()
