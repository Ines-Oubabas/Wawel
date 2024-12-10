from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('magasin.urls')),  # Inclure les routes de l'application "magasin"
]
