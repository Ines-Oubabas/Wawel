from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Page d'accueil
    path('contact/', views.contact, name='contact'),  # Page de contact
    path('produits/', views.produits, name='produits'),  # Page des produits
]
