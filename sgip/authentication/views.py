from django.shortcuts import render, redirect, HttpResponse
from urllib.parse import unquote
from .forms import ProductForm
from .models import Product, Category


def home(request):
    categories = Category.objects.filter(parent_category__isnull=True)
    return render(request, 'home.html', {'categories': categories})


def new_product(request, category, subcategory=None):
    try:
        category_obj = Category.objects.get(name=unquote(category))
    except Category.DoesNotExist:
        return HttpResponse(f'Category not found - {category}')

    if subcategory:
        try:
            subcategory_obj = category_obj.subcategories.get(name=unquote(subcategory))
            description = subcategory_obj.description
        except Category.DoesNotExist:
            return HttpResponse(f'Subcategory not found - {subcategory}')
    else:
        description = category_obj.description

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.category = category_obj
            product.save()
            return redirect('/products')
    else:
        initial_data = {'category': category_obj, 'description': description}
        if subcategory:
            initial_data['subcategory'] = subcategory_obj.name
        form = ProductForm(initial=initial_data)

    return render(request, 'cadastrate.html', {'form': form, 'category': category, 'subcategory': subcategory})


def display_products(request):
    products = Product.objects.all()
    return render(request, 'display.html', {'products': products})

