from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductFilterForm

def all_products(request):
    products = Product.objects.all()
    form = ProductFilterForm(request.GET)

    if form.is_valid():
        if form.cleaned_data['price_min']:
            products = products.filter(price__gte=form.cleaned_data['price_min'])
        if form.cleaned_data['price_max']:
            products = products.filter(price__lte=form.cleaned_data['price_max'])
        if form.cleaned_data['rating_min']:
            products = products.filter(rating__gte=form.cleaned_data['rating_min'])
        if form.cleaned_data['rating_max']:
            products = products.filter(rating__lte=form.cleaned_data['rating_max'])
        if form.cleaned_data['category']:
            products = products.filter(category=form.cleaned_data['category'])
        if form.cleaned_data['brand']:
            products = products.filter(brand=form.cleaned_data['brand'])
        if form.cleaned_data['sort_by']:
            products = products.order_by(form.cleaned_data['sort_by'])

    return render(request, 'products/all_products.html', {'products': products, 'form': form})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'products/product_detail.html', {'product': product})
