from django.shortcuts import render, redirect, HttpResponse
from .forms import ProdutoForm
from .models import Produto


def home(request):
	return render(request, "home.html")


def new_product(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/products')
    else:
        form = ProdutoForm()

    return render(request, 'cadastrate.html', {'form': form})


def display_products(request):
    products = Produto.objects.all()
    return render(request, 'display.html', {'produtos': products})
