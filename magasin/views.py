from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import EmailMessage
from .models import Product, Client, Promotion# Importation des modèles nécessaires
from datetime import date
from django.utils import timezone
from .models import Newsletter
from .models import NewsletterSubscriber
from .forms import ProduitForm, PromotionForm # Importation des formulaires nécessaires
from django.conf import settings
# Page d'accueil
def index(request):
    """
    Affiche la page d'accueil avec les promotions actives
    """
    today = timezone.now().date()
    promotions = Promotion.objects.filter(start_date__lte=today, end_date__gte=today)
    context = {'promotions': promotions}
    return render(request, 'index.html', context)

# Page À propos
def about(request):
    return render(request, 'about.html')

# Page Produits
def produits(request):
    produits = Product.objects.all()
    categories = {key: value for key, value in Product.CATEGORY_CHOICES}

    # Regroupement des produits par catégorie et sous-catégorie
    produits_par_categorie = {}
    for key, name in categories.items():
        sous_categories = {}
        for produit in produits.filter(category=key):
            sous_cat = produit.sub_category
            if sous_cat not in sous_categories:
                sous_categories[sous_cat] = []
            sous_categories[sous_cat].append(produit)
        produits_par_categorie[name] = sous_categories

    context = {
        'categories': produits_par_categorie,
    }
    return render(request, 'produits.html', context)

# Page Contact
def contact(request):
    """
    Gère le formulaire de contact et l'envoi d'emails
    """
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Envoi de l'email
        send_mail(
            subject=f"Message de {nom}",
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL, # Utilisation de la configuration sécurisée
            recipient_list=[settings.EMAIL_HOST_USER], # Email configuré dans .env
            fail_silently=False,
        )
        return HttpResponse("Message envoyé avec succès !")
    
    return render(request, 'contact.html')

# Soumission du formulaire de contact
def submit_contact(request):
    """
    Traite les données soumises depuis le formulaire de contact.
    """
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Vérifie que tous les champs sont remplis
        if not all([first_name, last_name, email, message]):
            return HttpResponse("Veuillez remplir tous les champs requis.", status=400)

        try:
            # Enregistrement du client dans la base de données
            client, created = Client.objects.get_or_create(
                email=email,
                defaults={
                    'first_name': first_name,
                    'last_name': last_name,
                    'message': message,
                }
            )

            # Si le client existe déjà, on met à jour son message
            if not created:
                client.message = message
                client.save()

            # Envoi de l'email avec EmailMessage pour ajouter reply_to
            subject = f"Message de {first_name} {last_name}"
            email_message = EmailMessage(
                subject=subject,
                body=message,
                from_email=settings.DEFAULT_FROM_EMAIL,  # Email sécurisé depuis .env
                to=[settings.EMAIL_HOST_USER],           # Email configuré dans .env
                reply_to=[email]                         # L'email du client pour répondre directement
            )
            email_message.send(fail_silently=False)

            return render(request, 'success.html', {'first_name': first_name})

        except Exception as e:
            # En cas d'erreur d'envoi d'email
            return HttpResponse(f"Erreur lors de l'envoi du message : {e}", status=500)

    return redirect('contact')

# newsletter
def newsletter(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if email:
            if Newsletter.objects.filter(email=email).exists():
                messages.error(request, "Cet email est déjà inscrit à la Newsletter.")
            else:
                Newsletter.objects.create(email=email)
                messages.success(request, "Merci pour votre inscription à la Newsletter !")
        else:
            messages.error(request, "Veuillez entrer une adresse email valide.")
    return redirect('index')  # Redirige vers la même page (index)

# subscrib newsletter
def newsletter_subscription(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if email:
            # Vérifie si l'email existe déjà
            if not Newsletter.objects.filter(email=email).exists():
                # Crée un nouvel abonné
                Newsletter.objects.create(email=email)
                messages.success(request, "Vous êtes abonné à notre newsletter avec succès !")
            else:
                messages.error(request, "Cet email est déjà abonné à notre newsletter.")
        else:
            messages.error(request, "Veuillez fournir une adresse email valide.")
    return redirect("index")
