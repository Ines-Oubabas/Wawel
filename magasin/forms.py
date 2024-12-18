from django import forms
from .models import Product, Promotion

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['sub_category', 'name_fr', 'name_en', 'code', 'description', 'image']

class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ['title', 'description', 'start_date', 'end_date']
