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

    // Slider d'images d'accueil
    const slides = document.querySelectorAll('.background-slideshow .slide');
    let currentIndex = 0;

    function showSlide(index) {
        const slideshow = document.querySelector('.background-slideshow');
        slideshow.style.transform = `translateX(-${index * 100}%)`;
        slideshow.style.transition = 'transform 1s ease-in-out';
    }

    setInterval(() => {
        currentIndex = (currentIndex + 1) % slides.length;
        showSlide(currentIndex);
    }, 5000);

    // Slider des témoignages
    const slider = document.querySelector('.testimonial-slider');
    const testimonials = document.querySelectorAll('.testimonial');
    const prevButton = document.getElementById('prev-btn');
    const nextButton = document.getElementById('next-btn');
    let testimonialIndex = 0;

    // Fonction pour afficher le témoignage actif
    function showTestimonial(index) {
        slider.style.transform = `translateX(-${index * 100}%)`;
        slider.style.transition = 'transform 0.5s ease-in-out';
    }

    // Gérer le clic sur le bouton précédent
    prevButton.addEventListener('click', function () {
        testimonialIndex = (testimonialIndex - 1 + testimonials.length) % testimonials.length;
        showTestimonial(testimonialIndex);
    });

    // Gérer le clic sur le bouton suivant
    nextButton.addEventListener('click', function () {
        testimonialIndex = (testimonialIndex + 1) % testimonials.length;
        showTestimonial(testimonialIndex);
    });

    // Défilement automatique des témoignages toutes les 5 secondes
    setInterval(() => {
        testimonialIndex = (testimonialIndex + 1) % testimonials.length;
        showTestimonial(testimonialIndex);
    }, 5000);

    // Optionnel : Arrêter le défilement automatique au survol du slider des témoignages
    slider.addEventListener('mouseenter', function () {
        clearInterval(autoScroll);
    });

    slider.addEventListener('mouseleave', function () {
        autoScroll = setInterval(() => {
            testimonialIndex = (testimonialIndex + 1) % testimonials.length;
            showTestimonial(testimonialIndex);
        }, 5000);
    });
});
