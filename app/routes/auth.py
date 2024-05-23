# app/routes/auth.py
from flask import Blueprint, request, jsonify, redirect, url_for, render_template
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import get_user, User, db

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    fullname = data['fullname']
    email = data['email']
    username = data['username']
    password = generate_password_hash(data['password'], method='sha256')

    if get_user(username):
        return jsonify({'error': 'User already exists'}), 400

    new_user = User(fullname=fullname, email=email, username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'})

@bp.route('/register', methods=['GET'])
def show_register_form():
    return render_template('create_account.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        username = data['username']
        password = data['password']

        user = get_user(username)
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('main.home'))
        return jsonify({'error': 'Invalid credentials'}), 401
    return render_template('login.html')
