from django.shortcuts import render

def index(request):
    """
    Affiche la page d'accueil
    """
    return render(request, 'index.html') # Page d'accueil

def about(request):
    return render(request, 'about.html')  # Page À propos

def menu(request):
    return render(request, 'menu.html')  # Page Menu (si nécessaire)


def contact(request):
    return render(request, 'contact.html') #page con


