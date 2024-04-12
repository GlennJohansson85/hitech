#____________________________________________________________________  PRODUCTS/VIEWS.PY
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product, Subcategory


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
    # Assuming you have a form defined for adding products
    form = None
    template = 'product/product_add.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def product_edit(request, product_id):
    """ A view to edit an existing product """
    # Assuming you have a form defined for editing products
    form = None
    product = get_object_or_404(Product, pk=product_id)
    template = 'product/product_edit.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)


def product_delete(request, product_id):
    """ A view to delete an existing product """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    # Assuming you're using Django's messages framework
    from django.contrib import messages
    messages.success(request, 'Product deleted!')

    return redirect('products')
