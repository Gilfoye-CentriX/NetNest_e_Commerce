import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Cart() {
    const [cartItems, setCartItems] = useState([]);

    useEffect(() => {
        axios.get('/view_cart')
            .then(response => {
                setCartItems(response.data);
            })
            .catch(error => {
                console.error('There was an error fetching the cart items!', error);
            });
    }, []);

    return (
        <div>
            {cartItems.length === 0 ? (
                <p>Your cart is empty</p>
            ) : (
                cartItems.map(item => (
                    <div key={item.product_id}>
                        <h3>{item.name}</h3>
                        <p>{item.price} x {item.quantity}</p>
                    </div>
                ))
            )}
        </div>
    );
}

export default Cart;
