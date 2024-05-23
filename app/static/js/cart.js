// app\static\js\cart.js
document.addEventListener("DOMContentLoaded", function() {
    const cartItemsContainer = document.getElementById("cart-items");
    const subtotalElement = document.getElementById("subtotal");
    const taxElement = document.getElementById("tax");
    const totalElement = document.getElementById("total");

    let cartItems = [];

    function updateCartUI() {
        cartItemsContainer.innerHTML = '';
        cartItems.forEach(item => {
            const itemElement = document.createElement("div");
            itemElement.classList.add("cart-item");
            itemElement.innerHTML = `
                <img src="images/product-image.jpg" alt="${item.name}">
                <div>
                    <h3>${item.name}</h3>
                    <p>Price: R${item.price.toFixed(2)}</p>
                </div>
                <button onclick="removeCartItem('${item.name}')">Remove</button>
            `;
            cartItemsContainer.appendChild(itemElement);
        });

        const subtotal = cartItems.reduce((total, item) => total + item.price * item.quantity, 0);
        const tax = subtotal * 0.15;
        const total = subtotal + tax;

        subtotalElement.textContent = `R${subtotal.toFixed(2)}`;
        taxElement.textContent = `R${tax.toFixed(2)}`;
        totalElement.textContent = `R${total.toFixed(2)}`;
    }

    function fetchCartItems() {
        fetch('/view_cart')
            .then(response => response.json())
            .then(data => {
                cartItems = data;
                updateCartUI();
            });
    }

    function addToCart(item) {
        fetch('/add_to_cart', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(item),
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            fetchCartItems();
        });
    }

    function removeCartItem(name) {
        cartItems = cartItems.filter(item => item.name !== name);
        updateCartUI();
    }

    fetchCartItems();
});
