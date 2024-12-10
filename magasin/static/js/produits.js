document.addEventListener('DOMContentLoaded', function () {
    // Animation sur les produits
    const products = document.querySelectorAll('.product-item');
    products.forEach((product) => {
        product.addEventListener('mouseover', function () {
            product.style.transform = 'scale(1.1)';
            product.style.transition = 'transform 0.3s ease';
        });

        product.addEventListener('mouseout', function () {
            product.style.transform = 'scale(1)';
        });
    });

    // Ajout d'une transition fluide
    products.forEach((product) => {
        product.addEventListener('click', function () {
            alert(`Vous avez cliqué sur ${product.querySelector('h3').innerText}!`);
        });
    });
});
