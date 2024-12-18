from django.db import models
from django.utils import timezone
# Modèle pour les produits
# Modèle pour les produits
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Boulangerie', 'Boulangerie Pâtisserie'),
        ('Sales', 'Salés'),
        ('Charcuterie', 'Charcuterie'),
        ('Autres', 'Autres'),
    ]

    SUBCATEGORY_CHOICES = [
        ('Pain', 'Pain'),
        ('Viennoiseries', 'Viennoiseries'),
        ('Format Familial', 'Format Familial'),
        ('Format Individuel', 'Format Individuel'),
        ('Biscuits', 'Biscuits'),
        ('Pour Fêtes', 'Pour Fêtes'),
        ('Mousses', 'Mousses'),
        ('Sandwichs', 'Sandwichs'),
        ('Salades', 'Salades'),
        ('Soupes', 'Soupes'),
        ('Autres', 'Autres'),
    ]
    
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="Catégorie", default='Autres')  # Valeur par défaut pour les anciennes données
    sub_category = models.CharField(max_length=50, choices=SUBCATEGORY_CHOICES, verbose_name="Sous-catégorie")
    name_fr = models.CharField(max_length=100, verbose_name="Nom du produit (FR)")
    name_en = models.CharField(max_length=100, verbose_name="Nom du produit (EN)")
    code = models.CharField(max_length=20, unique=True, verbose_name="Code du produit")
    description = models.TextField(verbose_name="Description")
    image = models.ImageField(upload_to='products/', verbose_name="Image du produit")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date d'ajout")

    def __str__(self):
        return f"{self.name_fr} ({self.code})"

# Modèle pour les clients
class Client(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Prénom")
    last_name = models.CharField(max_length=50, verbose_name="Nom")
    email = models.EmailField(unique=True, verbose_name="Adresse e-mail")
    message = models.TextField(blank=True, null=True, verbose_name="Message")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date d'inscription")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

# Modèle pour les promotions
class Promotion(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titre de la promotion")
    description = models.TextField(verbose_name="Description de la promotion")
    start_date = models.DateField(verbose_name="Date de début")
    end_date = models.DateField(verbose_name="Date de fin")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")

    class Meta:
        ordering = ['start_date']
        verbose_name = "Promotion"
        verbose_name_plural = "Promotions"

    def __str__(self):
        return self.title

    @property
    def is_active(self):
        today = timezone.now().date()
        return self.start_date <= today <= self.end_date

    @property
    def formatted_start_date(self):
        return self.start_date.strftime("%d %B %Y")

    @property
    def formatted_end_date(self):
        return self.end_date.strftime("%d %B %Y")
    
    # Modèle pour la Newsletter
class Newsletter(models.Model):
    email = models.EmailField(unique=True, verbose_name="Adresse email")
    subscribed_at = models.DateTimeField(auto_now_add=True, verbose_name="Date d'inscription")

    def __str__(self):
        return self.email
    
# subsrib newsletter
class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True, verbose_name="Adresse email")
    subscribed_at = models.DateTimeField(auto_now_add=True, verbose_name="Date d'inscription")

    def __str__(self):
        return self.email