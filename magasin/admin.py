from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from .models import Product, Client, Promotion, Newsletter


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name_fr", "name_en", "code", "category", "sub_category", "created_at")
    search_fields = ("name_fr", "name_en", "code")
    list_filter = ("category", "sub_category")
    ordering = ("-created_at",)
    
    # Ajout d'une action pour rediriger vers une page de modification
    actions = ["redirect_to_modify_products"]

    def get_urls(self):
        """
        Ajout d'une URL personnalisée pour la modification en lot des produits.
        """
        urls = super().get_urls()
        custom_urls = [
            path(
                "modify-products/",
                self.admin_site.admin_view(self.modify_products_view),
                name="modify_products",
            ),
        ]
        return custom_urls + urls

    def modify_products_view(self, request):
        """
        Vue pour modifier les produits sélectionnés.
        """
        if "apply" in request.POST:
            # Sauvegarder les modifications
            product_ids = request.POST.getlist("product_ids")
            for product_id in product_ids:
                product = Product.objects.get(pk=product_id)
                product.name_fr = request.POST.get(f"name_fr_{product_id}", product.name_fr)
                product.name_en = request.POST.get(f"name_en_{product_id}", product.name_en)
                product.code = request.POST.get(f"code_{product_id}", product.code)
                product.description = request.POST.get(f"description_{product_id}", product.description)
                product.save()
            self.message_user(request, "Les modifications ont été enregistrées avec succès.")
            return redirect("admin:magasin_product_changelist")

        # Affichage de la page avec les produits sélectionnés
        selected_products = Product.objects.filter(pk__in=request.GET.getlist("ids"))
        return render(request, "admin/modify_products.html", {"products": selected_products})

    def redirect_to_modify_products(self, request, queryset):
        """
        Action pour rediriger vers la vue de modification en lot.
        """
        ids = ",".join(str(obj.id) for obj in queryset)
        return redirect(f"{request.path}modify-products/?ids={ids}")

    redirect_to_modify_products.short_description = "Modifier les produits sélectionnés"


# Enregistrement des autres modèles
class ClientAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "created_at")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("-created_at",)


class PromotionAdmin(admin.ModelAdmin):
    list_display = ("title", "start_date", "end_date", "created_at")
    search_fields = ("title",)
    list_filter = ("start_date", "end_date")
    ordering = ("-created_at",)


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ("email", "subscribed_at")
    search_fields = ("email",)
    ordering = ("-subscribed_at",)


admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Promotion, PromotionAdmin)
admin.site.register(Newsletter, NewsletterAdmin)
