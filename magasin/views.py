from django.shortcuts import render

def index(request):
    """
    Affiche la page d'accueil
    """
    return render(request, 'index.html')



