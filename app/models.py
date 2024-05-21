from flask_login import UserMixin
import sqlite3

class User(UserMixin):
    def __init__(self, id, fullname, email, username, password):
        self.id = id
        self.fullname = fullname
        self.email = email
        self.username = username
        self.password = password

    @staticmethod
    def get(user_id):
        conn = sqlite3.connect('ecommerce.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        user = cursor.fetchone()
        conn.close()
        if user:
            return User(*user)
        return None

def get_user(username):
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    if user:
        return User(*user)
    return None

def get_user_by_id(user_id):
    return User.get(user_id)