#____________________________________________________________________  PRODUCTS/MODELS.PY
import os
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=254)

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=254)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='Subcategories'

    def __str__(self):
        return self.name


def product_image_path(instance, filename):
    # Ensure the instance has both category and subcategory associated with it
    if instance.category and instance.subcategory:
        # Generate the upload path based on the category, subcategory, and filename
        return os.path.join('products', instance.category.name, instance.subcategory.name, filename)
    else:
        # If either category or subcategory is not associated, use a default path
        return os.path.join('products', 'uncategorized', filename)

class Product(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    subcategory = models.ForeignKey(Subcategory, null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=0, null=True)
    rating = models.DecimalField(max_digits=5, decimal_places=0, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to=product_image_path, null=True, blank=True)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return "Unnamed Product" 