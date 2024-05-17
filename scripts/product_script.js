document.addEventListener("DOMContentLoaded", function() {
    const categoryFilter = document.getElementById("category-filter");
    const productCards = document.querySelectorAll(".product-card");
    const addToCartButtons = document.querySelectorAll(".product-card button");

    // Function to add a product to the cart
    function addToCart(productName, productPrice) {
        const cartItem = { name: productName, price: parseFloat(productPrice) };
        // Send the cart item to the cart.js file for processing (assuming cart.js handles cart functionality)
        addToCartFunction(cartItem);
        alert("Item added to cart!");
    }

    // Event listener for Add to Cart buttons
    addToCartButtons.forEach(button => {
        button.addEventListener("click", function() {
            const productCard = this.closest(".product-card");
            const productName = productCard.querySelector("h2").textContent;
            const productPrice = productCard.querySelector("p").textContent.replace("R", "");
            addToCart(productName, productPrice);
        });
    });

    // Event listener for category filter
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