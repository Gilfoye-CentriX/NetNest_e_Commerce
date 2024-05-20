document.addEventListener("DOMContentLoaded", function() {
    const cartItemsContainer = document.getElementById("cart-items");
    const subtotalElement = document.getElementById("subtotal");
    const taxElement = document.getElementById("tax");
    const totalElement = document.getElementById("total");

    let cartItems = []; // Array to store cart items

    // Function to update cart items in the UI
    function updateCartUI() {
        cartItemsContainer.innerHTML = ''; // Clear previous items
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

        // Calculate subtotal, tax, and total
        const subtotal = cartItems.reduce((total, item) => total + item.price, 0);
        const tax = subtotal * 0.15; // Assuming 15% tax
        const total = subtotal + tax;

        subtotalElement.textContent = `R${subtotal.toFixed(2)}`;
        taxElement.textContent = `R${tax.toFixed(2)}`;
        totalElement.textContent = `R${total.toFixed(2)}`;
    }

    // Function to add an item to the cart
    function addToCart(item) {
        cartItems.push(item);
        updateCartUI();
    }

    // Function to remove an item from the cart
    function removeCartItem(name) {
        cartItems = cartItems.filter(item => item.name !== name);
        updateCartUI();
    }

    // Example: Add some initial items to the cart
    addToCart({ name: "Android 6", price: 99.99 });
    addToCart({ name: "Samsung", price: 149.99 });
	addToCart({ name: "Huawei", price: 149.99 });
});