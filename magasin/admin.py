from django.contrib import admin
from .models import Product, Client, Promotion
from .models import Newsletter

# Configuration de l'administration pour les produits
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_fr', 'name_en', 'code', 'category', 'sub_category', 'created_at')
    search_fields = ('name_fr', 'name_en', 'code')
    list_filter = ('category', 'sub_category')
    ordering = ('-created_at',)

# Configuration de l'administration pour les clients
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'created_at')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('-created_at',)

# Configuration de l'administration pour les promotions
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'is_active_display', 'created_at')
    search_fields = ('title',)
    list_filter = ('start_date', 'end_date')
    ordering = ('-created_at',)

    def is_active_display(self, obj):
        """Ajoute une colonne qui affiche si la promotion est active."""
        return obj.is_active
    is_active_display.boolean = True  # Affiche sous forme de ✅ ou ❌ dans l'admin
    is_active_display.short_description = "Active"

# Enregistrement des modèles dans l'interface d'administration
admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Promotion, PromotionAdmin)

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    search_fields = ('email',)
    ordering = ('-subscribed_at',)

admin.site.register(Newsletter, NewsletterAdmin)