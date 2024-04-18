#____________________________________________________________________  PRODUCTS/VIEWS.PY
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Category, Subcategory, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
    """ A view to show all products with pagination """
    categories = Category.objects.all()
    category_subcategories = {}
    for category in categories:
        subcategories = Subcategory.objects.filter(category=category)
        subcategory_products = {}
        for subcategory in subcategories:
            products = Product.objects.filter(category=category, subcategory=subcategory)
            subcategory_products[subcategory] = products
        category_subcategories[category] = subcategory_products
    
    # Paginate the products
    paginator = Paginator(Product.objects.all(), 10)  # Number of products per page
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'products/product_list.html', {
        'category_subcategories': category_subcategories,
        'products': products,  # Pass paginated products to the template
    })


def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)
    
    # Fetch the next and previous products based on some criteria
    next_product = Product.objects.filter(id__gt=product.id).first()  # Get the next product by ID
    prev_product = Product.objects.filter(id__lt=product.id).last()   # Get the previous product by ID
    
    next_product_url = reverse('product_detail', args=[next_product.id]) if next_product else None
    prev_product_url = reverse('product_detail', args=[prev_product.id]) if prev_product else None
    
    context = {
        'product': product,
        'next_product_url': next_product_url,
        'prev_product_url': prev_product_url,
    }
    
    return render(request, 'products/product_detail.html', context)


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
