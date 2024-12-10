document.addEventListener('DOMContentLoaded', function () {
    // Mise en surbrillance du lien actif dans le menu de navigation
    const navLinks = document.querySelectorAll('header nav ul li a');
    const currentUrl = window.location.pathname;
    navLinks.forEach((link) => {
        if (link.getAttribute('href') === currentUrl) {
            link.style.textDecoration = 'underline';
            link.style.fontWeight = 'bold';
        }
    });

    // Slider des témoignages
    const slider = document.querySelector('.testimonial-slider');
    const testimonials = document.querySelectorAll('.testimonial');
    const prevButton = document.getElementById('prev-btn');
    const nextButton = document.getElementById('next-btn');
    let currentIndex = 0;

    // Fonction pour afficher le témoignage actif
    function showTestimonial(index) {
        slider.style.transform = `translateX(-${index * 100}%)`;
        slider.style.transition = 'transform 0.5s ease-in-out';
    }

    // Gérer le clic sur le bouton précédent
    prevButton.addEventListener('click', function () {
        currentIndex = (currentIndex - 1 + testimonials.length) % testimonials.length;
        showTestimonial(currentIndex);
    });

    // Gérer le clic sur le bouton suivant
    nextButton.addEventListener('click', function () {
        currentIndex = (currentIndex + 1) % testimonials.length;
        showTestimonial(currentIndex);
    });

    // Défilement automatique des témoignages toutes les 5 secondes
    setInterval(() => {
        currentIndex = (currentIndex + 1) % testimonials.length;
        showTestimonial(currentIndex);
    }, 5000);

    // Optionnel : Arrêter le défilement automatique au survol du slider
    slider.addEventListener('mouseenter', function () {
        clearInterval(autoScroll);
    });

    slider.addEventListener('mouseleave', function () {
        autoScroll = setInterval(() => {
            currentIndex = (currentIndex + 1) % testimonials.length;
            showTestimonial(currentIndex);
        }, 5000);
    });
});


