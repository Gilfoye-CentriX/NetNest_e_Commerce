from flask import Blueprint, request, jsonify

bp = Blueprint('products', __name__)

@bp.route('/products', methods=['GET'])
def get_products():
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()

    products_list = [{'id': prod[0], 'name': prod[1], 'price': prod[2]} for prod in products]
    return jsonify(products_list)

@bp.route('/product', methods=['POST'])
def add_product():
    data = request.json
    name = data['name']
    price = data['price']

    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', (name, price))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Product added successfully'})
