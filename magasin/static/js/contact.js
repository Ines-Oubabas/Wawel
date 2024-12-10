document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form'); // Sélectionner le formulaire
    if (form) {
        form.addEventListener('submit', function (event) {
            event.preventDefault(); // Empêcher l'envoi par défaut
            const nom = form.querySelector('input[name="nom"]').value;
            alert(`Merci ${nom}, votre message a été envoyé avec succès !`);
            form.reset(); // Réinitialiser le formulaire après soumission
        });
    }
});
