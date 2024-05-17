from flask import Flask
from flask_login import LoginManager
import sqlite3

app = Flask(__name__)
app.secret_key = '8427356'  
login_manager = LoginManager()
login_manager.init_app(app)

def init_db():
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS products
                      (id INTEGER PRIMARY KEY, name TEXT, price REAL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS cart
                      (user_id INTEGER, product_id INTEGER, quantity INTEGER)''')
    conn.commit()
    conn.close()

from app.routes import auth, cart, products
app.register_blueprint(auth.bp)
app.register_blueprint(cart.bp)
app.register_blueprint(products.bp)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)