from flask import Blueprint, request, jsonify, session, render_template
from flask_login import login_required, current_user
import sqlite3

bp = Blueprint('checkout', __name__)

@bp.route('/checkout')
#@login_required
def view_checkout():
    # Logic to display the checkout page
    return render_template('checkout.html')
