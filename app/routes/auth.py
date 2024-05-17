from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from app.models import get_user, User

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data['username']
    password = data['password']

    if get_user(username):
        return jsonify({'error': 'User already exists'}), 400

    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()
    return jsonify({'message': 'User registered successfully'})

@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']

    user = get_user(username)
    if user and user.password == password:
        login_user(user)
        return jsonify({'message': 'Login successful'})
    return jsonify({'error': 'Invalid credentials'}), 401

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'})