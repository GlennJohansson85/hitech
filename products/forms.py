#____________________________________________________________________  PRODUCTS/FORMS.PY
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'subcategory', 'title', 'description', 'price', 'rating', 'image']

    
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image:
            raise forms.ValidationError("Please upload an image.")
        
        return image
