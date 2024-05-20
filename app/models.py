from flask_login import UserMixin
import sqlite3

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

def get_user(username):
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, username, password FROM users WHERE username = ?', (username,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return User(id=row[0], username=row[1], password=row[2])
    return None

def get_user_by_id(user_id):
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, username, password FROM users WHERE id = ?', (user_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return User(id=row[0], username=row[1], password=row[2])
    return None
