from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    """
    Affiche la page d'accueil
    """
    return render(request, 'index.html')


def contact(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        adresse_postale = request.POST.get('adresse_postale')
        mot_de_passe = request.POST.get('mot_de_passe')
        confirmation_mot_de_passe = request.POST.get('confirmation_mot_de_passe')

        # Vérification des mots de passe
        if mot_de_passe != confirmation_mot_de_passe:
            return HttpResponse("Les mots de passe ne correspondent pas !")

        # Simulez le traitement des données
        print(f"Nom: {nom}, Prénom: {prenom}, Email: {email}, Adresse: {adresse_postale}")

        return HttpResponse("Merci, votre message a été envoyé avec succès !")

    return render(request, 'contact.html')

def produits(request):
    """
    Affiche la page des produits
    """
    # Exemple de liste de produits (cela peut venir d'une base de données plus tard)
    produits = [
        {"nom": "Beignes Artisanaux", "image": "magasin/images/beigne.jpg", "description": "Délicieux beignes faits maison."},
        {"nom": "Gâteaux Personnalisés", "image": "magasin/images/gateau.jpg", "description": "Des gâteaux pour toutes les occasions."},
        {"nom": "Pains Frais", "image": "magasin/images/pain.jpg", "description": "Pains frais préparés tous les jours."},
    ]

    # Passer les produits au template
    return render(request, 'produits.html', {'produits': produits})
