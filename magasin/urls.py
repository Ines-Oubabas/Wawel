from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Page d'accueil
    path('about/', views.about, name='about'), # Page a propos 
    path('produits/', views.produits, name='produits'),
    path('contact/', views.contact, name='contact'),  # Page de contact
]
