from django.urls import path
from . import views

urlpatterns = [
    # Pages principales
    path('', views.index, name='index'),  # Page d'accueil
    path('about/', views.about, name='about'),  # Page À propos
    path('produits/', views.produits, name='produits'),  # Page des produits
    path('contact/', views.contact, name='contact'),  # Page de contact
    path('submit-contact/', views.submit_contact, name='submit_contact'),  # Soumission du formulaire
    path('newsletter/', views.newsletter_subscription, name='newsletter'),
    
]
