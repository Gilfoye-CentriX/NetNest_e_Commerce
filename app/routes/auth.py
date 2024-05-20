from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
import sqlite3
from app.models import get_user, User

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        fullname = data['fullname']
        email = data['email']
        username = data['username']
        password = data['password']

        if get_user(username):
            return jsonify({'error': 'User already exists'}), 400

        conn = sqlite3.connect('ecommerce.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (fullname, email, username, password) VALUES (?, ?, ?, ?)', 
                           (fullname, email, username, password))
        conn.commit()
        conn.close()
        return jsonify({'message': 'User registered successfully'})
    return render_template('create_account.html')
    
@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        username = data['username']
        password = data['password']

        user = get_user(username)
        if user and user.password == password:
            login_user(user)
            return jsonify({'message': 'Login successful'})
        return jsonify({'error': 'Invalid credentials'}), 401
    return render_template('login.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'})
