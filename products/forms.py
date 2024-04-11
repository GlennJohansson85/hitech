#____________________________________________________________________  PRODUCTS/FORMS.PY
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'subcategory', 'title', 'description', 'price', 'rating', 'image_url', 'image']