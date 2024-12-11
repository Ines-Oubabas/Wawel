from django.shortcuts import render

def index(request):
    """
    Affiche la page d'accueil
    """
    return render(request, 'index.html')

# Vue pour la page de contact
def contact(request):
    return render(request, 'contact.html')

