from django.contrib import admin
from django.shortcuts import render
from .models import Product, Client, Promotion, Newsletter

# Fonction pour modifier les produits sélectionnés
def update_selected_products(modeladmin, request, queryset):
    if 'apply' in request.POST:
        # Mettre à jour chaque produit sélectionné
        for idx, product in enumerate(queryset):
            name_fr = request.POST.get(f'name_fr_{idx+1}')
            name_en = request.POST.get(f'name_en_{idx+1}')
            code = request.POST.get(f'code_{idx+1}')
            category = request.POST.get(f'category_{idx+1}')
            subcategory = request.POST.get(f'subcategory_{idx+1}')
            description = request.POST.get(f'description_{idx+1}')
            image = request.FILES.get(f'image_{idx+1}')  # Gestion des fichiers

            # Afficher les valeurs récupérées dans la console pour vérifier
            print(f"Updating Product {product.id}: {name_fr}, {name_en}, {code}, {category}, {subcategory}, {description}")

            if name_fr:
                product.name_fr = name_fr
            if name_en:
                product.name_en = name_en
            if code:
                product.code = code
            if category:
                product.category = category
            if subcategory:
                product.sub_category = subcategory
            if description:
                product.description = description
            if image:
                product.image = image
            
            product.save()

        # Message de confirmation
        modeladmin.message_user(request, f"{queryset.count()} produits ont été mis à jour.")
        return None

    # Sinon, afficher le formulaire
    return render(request, 'admin/update_products.html', {'products': queryset})

# Ajoute une description pour l'action
update_selected_products.short_description = "Modifier les produits sélectionnés"

# Configuration de l'administration pour les produits
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_fr', 'name_en', 'code', 'category', 'sub_category', 'created_at')
    search_fields = ('name_fr', 'name_en', 'code')
    list_filter = ('category', 'sub_category')
    ordering = ('-created_at',)

    # Utilisation de fieldsets uniquement pour organiser les champs
    fieldsets = (
        (None, {
            'fields': ('name_fr', 'name_en', 'code', 'category', 'sub_category')
        }),
        ('Détails du produit', {
            'fields': ('description', 'image')
        }),
    )

    actions = [update_selected_products]  # Ajoute l'action de mise à jour des produits sélectionnés
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

# Configuration de l'administration pour la newsletter
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    search_fields = ('email',)
    ordering = ('-subscribed_at',)

# Enregistrement des modèles dans l'interface d'administration
admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Promotion, PromotionAdmin)
admin.site.register(Newsletter, NewsletterAdmin)