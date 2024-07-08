// Add event listener to add to cart button
document.addEventListener('DOMContentLoaded', function() {
    const addToCartButtons = document.querySelectorAll('.product-list button');
    addToCartButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            const productId = button.parentNode.dataset.productId;
            fetch('/add-to-cart/' + productId)
               .then(response => response.json())
               .then(data => console.log(data))
               .catch(error => console.error(error));
        });
    });
});