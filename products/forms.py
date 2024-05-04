#____________________________________________________________________  PRODUCTS/FORMS.PY
from django import forms
from .models import Product, Category, Subcategory

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image:
            raise forms.ValidationError("Please upload an image.")
        
        return image
