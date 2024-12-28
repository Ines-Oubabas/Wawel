from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from .models import Product, Client, Promotion, Newsletter
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django import forms
from django.contrib.admin.helpers import ActionForm
from django.conf import settings

# ActionForm pour personnaliser les emails
class EmailActionForm(ActionForm):
    subject = forms.CharField(required=True, max_length=255, label="Sujet")
    message = forms.CharField(widget=forms.Textarea, label="Message")

# PRODUCTS
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name_fr", "name_en", "code", "category", "sub_category", "created_at")
    search_fields = ("name_fr", "name_en", "code")
    list_filter = ("category", "sub_category")
    ordering = ("-created_at",)
    actions = ["redirect_to_modify_products"]

    def get_urls(self):
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
        if "apply" in request.POST:
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

        selected_products = Product.objects.filter(pk__in=request.GET.getlist("ids"))
        return render(request, "admin/modify_products.html", {"products": selected_products})

    def redirect_to_modify_products(self, request, queryset):
        ids = ",".join(str(obj.id) for obj in queryset)
        return redirect(f"{request.path}modify-products/?ids={ids}")

    redirect_to_modify_products.short_description = "Modifier les produits sélectionnés"

# Action pour envoyer un email aux clients sélectionnés
@admin.action(description="Envoyer un email aux clients sélectionnés")
def send_email_to_clients(modeladmin, request, queryset):
    emails = [client.email for client in queryset]
    subject = request.POST.get("subject", "Nouvelle promotion Wawel")
    message = request.POST.get("message", "Cher client, découvrez nos nouvelles offres sur notre site web !")

    # Générer le contenu HTML de l'email
    html_message = render_to_string('admin/email_template.html', {
        'subject': subject,
        'message': message,
        'footer_note': "Merci de nous faire confiance. Nous espérons vous voir bientôt en magasin ou sur notre site !",
    })

    # Envoyer l'email en HTML
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=settings.EMAIL_HOST_USER,
        to=emails,
    )
    email.content_subtype = "html"  # Définit le type de contenu à HTML
    email.send(fail_silently=False)

    modeladmin.message_user(request, f"L'email a été envoyé avec succès à {len(emails)} clients.")

class ClientAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "created_at")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("-created_at",)
    actions = [send_email_to_clients]
    action_form = EmailActionForm

# Promotion
class PromotionAdmin(admin.ModelAdmin):
    list_display = ("title", "start_date", "end_date", "created_at")
    search_fields = ("title",)
    list_filter = ("start_date", "end_date")
    ordering = ("-created_at",)

# Action pour envoyer un email aux abonnés de la newsletter
@admin.action(description="Envoyer un email aux abonnés sélectionnés")
def send_newsletter_email(modeladmin, request, queryset):
    emails = [subscriber.email for subscriber in queryset]
    subject = request.POST.get("subject", "Nouvelle promotion Wawel")
    message = request.POST.get("message", "Découvrez nos nouvelles promotions sur le site !")

    # Générer le contenu HTML de l'email
    html_message = render_to_string('admin/email_template.html', {
        'subject': subject,
        'message': message,
        'footer_note': "Abonnez-vous pour ne rien rater de nos délicieuses offres et nouveautés !",
    })

    # Envoyer l'email en HTML
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=settings.EMAIL_HOST_USER,
        to=emails,
    )
    email.content_subtype = "html"
    email.send(fail_silently=False)

    modeladmin.message_user(request, f"Email envoyé à {len(emails)} abonnés.")

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ("email", "subscribed_at")
    search_fields = ("email",)
    ordering = ("-subscribed_at",)
    actions = [send_newsletter_email]
    action_form = EmailActionForm

admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Promotion, PromotionAdmin)
admin.site.register(Newsletter, NewsletterAdmin)
