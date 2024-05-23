// app\static\js\product_script.js
document.addEventListener("DOMContentLoaded", function() {
    const categoryFilter = document.getElementById("category-filter");
    const productCards = document.querySelectorAll(".product-card");
    const addToCartButtons = document.querySelectorAll(".product-card button");

    function addToCart(productId, quantity = 1) {
        fetch('/add_to_cart', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ product_id: productId, quantity: quantity }),
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
        });
    }

    addToCartButtons.forEach(button => {
        button.addEventListener("click", function() {
            const productCard = this.closest(".product-card");
            const productId = productCard.getAttribute("data-product-id");
            const quantity = 1; // You can change this to get quantity from user input
            addToCart(productId, quantity);
        });
    });

    categoryFilter.addEventListener("change", function() {
        const selectedCategory = categoryFilter.value;
        productCards.forEach(card => {
            const cardCategory = card.getAttribute("data-category");
            if (selectedCategory === "all" || selectedCategory === cardCategory) {
                card.style.display = "block";
            } else {
                card.style.display = "none";
            }
        });
    });
});
