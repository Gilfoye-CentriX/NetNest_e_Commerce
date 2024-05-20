from flask import Blueprint, request, jsonify, session, render_template
from flask_login import login_required, current_user

bp = Blueprint('cart', __name__)

@bp.route('/add_to_cart', methods=['POST'])
@bp.route('/cart')
@login_required
def add_to_cart():
    user_id = current_user.id
    product_id = request.json.get('product_id')
    quantity = request.json.get('quantity', 1)

    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM products WHERE id = ?', (product_id,))
    product = cursor.fetchone()
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    cursor.execute('SELECT * FROM cart WHERE user_id = ? AND product_id = ?', (user_id, product_id))
    cart_item = cursor.fetchone()

    if cart_item:
        cursor.execute('UPDATE cart SET quantity = quantity + ? WHERE user_id = ? AND product_id = ?', (quantity, user_id, product_id))
    else:
        cursor.execute('INSERT INTO cart (user_id, product_id, quantity) VALUES (?, ?, ?)', (user_id, product_id, quantity))
    
    conn.commit()
    conn.close()

    return jsonify({'message': 'Product added to cart successfully'})

@bp.route('/view_cart', methods=['GET'])
@login_required
def view_cart():
    user_id = current_user.id
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT products.id, products.name, products.price, cart.quantity
                      FROM cart
                      JOIN products ON cart.product_id = products.id
                      WHERE cart.user_id = ?''', (user_id,))
    cart_items = cursor.fetchall()
    conn.close()

    cart = [{'product_id': item[0], 'name': item[1], 'price': item[2], 'quantity': item[3]} for item in cart_items]
    return jsonify(cart)
