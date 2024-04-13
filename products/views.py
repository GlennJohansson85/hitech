#____________________________________________________________________  PRODUCTS/VIEWS.PY
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product, Subcategory

from .forms import ProductForm


def product_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    products = Product.objects.filter(category=category)

    return render(request, 'products/product_category.html', {'category': category, 'products': products})


def product_subcategory(request, category_id):
    category = Category.objects.get(pk=category_id)
    subcategories = Subcategory.objects.filter(category=category)
    
    return render(request, 'products/product_subcategory.html', {'category': category, 'subcategories': subcategories})


def product_list(request):
    """ A view to show all products """
    categories = Category.objects.all()
    category_products = {}
    for category in categories:
        products = Product.objects.filter(category=category)
        category_products[category.name] = products

    return render(request, 'products/product_list.html', {
        'category_products': category_products,
    })


def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)

    return render(request, 'products/product_detail.html', {'product': product})


def product_add(request):
    """ A view to add a new product """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to the product list page
    else:
        form = ProductForm()
        
    return render(request, 'product_add.html', {'form': form})


def product_edit(request, product_id):
    """ A view to edit an existing product """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to the product list page
    else:
        form = ProductForm(instance=product)
        
    return render(request, 'products/product_edit.html', {'form': form, 'product': product})


def product_delete(request, product_id):
    """ A view to delete an existing product """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')  # Redirect to the product list page
    
    return render(request, 'products/product_delete.html', {'product': product})
