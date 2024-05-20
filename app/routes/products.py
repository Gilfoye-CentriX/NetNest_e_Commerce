from flask import Blueprint, render_template

bp = Blueprint('products', __name__)

@bp.route('/products')
def show_products():
    # Logic to fetch and display products
    return render_template('products.html')

@bp.route('/products/add', methods=['GET', 'POST'])
def add_product():
    # Logic to add a new product
    return render_template('add_product.html')
