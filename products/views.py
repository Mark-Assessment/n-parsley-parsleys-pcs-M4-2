from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Brand
from .forms import ProductFilterForm
from django.db.models import Q


def all_products(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    brands = Brand.objects.all()

    # Filter by category name
    category_name = request.GET.get('category')
    if category_name:
        category = get_object_or_404(Category, name=category_name)
        products = products.filter(category=category)

    # Filter by brand name
    brand_name = request.GET.get('brand')
    if brand_name:
        brand = get_object_or_404(Brand, name=brand_name)
        products = products.filter(brand=brand)

    form = ProductFilterForm(request.GET or None)
    if form.is_valid():
        if form.cleaned_data['price_min']:
            products = products.filter(
                price__gte=form.cleaned_data['price_min'])
        if form.cleaned_data['price_max']:
            products = products.filter(
                price__lte=form.cleaned_data['price_max'])
        if form.cleaned_data['rating_min']:
            products = products.filter(
                rating__gte=form.cleaned_data['rating_min'])
        if form.cleaned_data['rating_max']:
            products = products.filter(
                rating__lte=form.cleaned_data['rating_max'])
        if form.cleaned_data['sort_by']:
            products = products.order_by(form.cleaned_data['sort_by'])

    return render(request, 'products/all_products.html', {
        'products': products,
        'form': form,
        'categories': categories,
        'brands': brands,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(
        request, 'products/product_detail.html', {'product': product})


def search(request):
    query = request.GET.get('searchbar')
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query) |
            Q(brand__name__icontains=query)
        )
    else:
        products = Product.objects.all()
    return render(
        request,
        'products/search_results.html',
        {'products': products, 'query': query}
        )
