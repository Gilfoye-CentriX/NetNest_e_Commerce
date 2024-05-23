from flask import Blueprint, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
from app import db
from app.models import Product

bp = Blueprint('products', __name__)

@bp.route('/')
def show_products():
    products = Product.query.all()
    return render_template('products.html', products=products)

@bp.route('/add', methods=['POST'])
def add_product():
    if 'image' not in request.files:
        return jsonify({'error': 'No image part'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join('app/static/images', filename)
        file.save(file_path)

        new_product = Product(
            name=request.form['name'],
            price=request.form['price'],
            category=request.form['category'],
            image=filename
        )

        db.session.add(new_product)
        db.session.commit()

        return jsonify({'message': 'Product added successfully!'}), 200

    return jsonify({'error': 'An error occurred while adding the product'}), 500
