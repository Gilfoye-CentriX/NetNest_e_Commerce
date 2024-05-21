from flask import Flask
from flask_login import LoginManager
import sqlite3
from app.models import get_user_by_id

def create_app():
    app = Flask(__name__)
    app.secret_key = '8427356'
    
    login_manager = LoginManager()
    login_manager.init_app(app)

    from app.routes.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.routes.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.routes.products import bp as products_bp
    app.register_blueprint(products_bp, url_prefix='/products')

    from app.routes.cart import bp as cart_bp
    app.register_blueprint(cart_bp, url_prefix='/cart')

    from app.routes.checkout import bp as checkout_bp
    app.register_blueprint(checkout_bp, url_prefix='/checkout')

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)
    
    return app

def init_db():
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY, 
                       fullname TEXT, 
                       email TEXT UNIQUE, 
                       username TEXT UNIQUE, 
                       password TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS products
                      (id INTEGER PRIMARY KEY, name TEXT, price REAL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS cart
                      (user_id INTEGER, product_id INTEGER, quantity INTEGER)''')
    conn.commit()
    conn.close()
