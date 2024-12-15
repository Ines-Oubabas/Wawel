from django.shortcuts import render

def index(request):
    """
    Affiche la page d'accueil
    """
    return render(request, 'index.html') # Page d'accueil

def about(request):
    return render(request, 'about.html')  # Page À propos

def produits(request):
    return render(request, 'produits.html')  # Page produits (si nécessaire)


def contact(request):
    return render(request, 'contact.html') #page contact


