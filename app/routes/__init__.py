from flask import Flask
from flask_login import LoginManager
import sqlite3

def create_app():
    app = Flask(__name__)
    app.secret_key = '8427356'
    login_manager = LoginManager()
    login_manager.init_app(app)

    from app.routes.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.routes.cart import bp as cart_bp
    app.register_blueprint(cart_bp, url_prefix='/cart')

    from app.routes.products import bp as products_bp
    app.register_blueprint(products_bp, url_prefix='/products')

    return app

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
