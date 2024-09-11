from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import Product, Motherboard, CPU, RAM, PSU, GPU, Case, Storage, Category, Brand
from .forms import (ProductFilterForm, MotherboardForm, CPUForm, RAMForm, PSUForm, GPUForm, CaseForm, StorageForm)
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

def superuser_required(user):
    return user.is_superuser


@user_passes_test(superuser_required)
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})


@user_passes_test(superuser_required)
def add_product(request, product_type):
    form = None
    category_map = {
        'motherboard': 'Motherboard',
        'cpu': 'CPU',
        'ram': 'RAM',
        'psu': 'PSU',
        'gpu': 'GPU',
        'case': 'Case',
        'storage': 'Storage',
    }

    category = get_object_or_404(Category, name=category_map.get(product_type))

    if request.method == 'POST':
        if product_type == 'motherboard':
            form = MotherboardForm(request.POST or None, request.FILES or None)
        elif product_type == 'cpu':
            form = CPUForm(request.POST or None, request.FILES or None)
        elif product_type == 'ram':
            form = RAMForm(request.POST or None, request.FILES or None)
        elif product_type == 'psu':
            form = PSUForm(request.POST or None, request.FILES or None)
        elif product_type == 'gpu':
            form = GPUForm(request.POST or None, request.FILES or None)
        elif product_type == 'case':
            form = CaseForm(request.POST or None, request.FILES or None)
        elif product_type == 'storage':
            form = StorageForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            product = form.save(commit=False)
            product.category = category 
            product.save()
            return redirect('product_list')

    else:
        if product_type == 'motherboard':
            form = MotherboardForm(initial={'category': category})
        elif product_type == 'cpu':
            form = CPUForm(initial={'category': category})
        elif product_type == 'ram':
            form = RAMForm(initial={'category': category})
        elif product_type == 'psu':
            form = PSUForm(initial={'category': category})
        elif product_type == 'gpu':
            form = GPUForm(initial={'category': category})
        elif product_type == 'case':
            form = CaseForm(initial={'category': category})
        elif product_type == 'storage':
            form = StorageForm(initial={'category': category})

    return render(request, 'products/add_product.html', {'form': form})


@user_passes_test(superuser_required)
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    form = None
    if hasattr(product, 'motherboard'):
        product = product.motherboard  
        form = MotherboardForm(request.POST or None, request.FILES or None, instance=product)
    elif hasattr(product, 'cpu'):
        product = product.cpu  
        form = CPUForm(request.POST or None, request.FILES or None, instance=product)
    elif hasattr(product, 'ram'):
        product = product.ram  
        form = RAMForm(request.POST or None, request.FILES or None, instance=product)
    elif hasattr(product, 'psu'):
        product = product.psu  
        form = PSUForm(request.POST or None, request.FILES or None, instance=product)
    elif hasattr(product, 'gpu'):
        product = product.gpu  
        form = GPUForm(request.POST or None, request.FILES or None, instance=product)
    elif hasattr(product, 'case'):
        product = product.case  
        form = CaseForm(request.POST or None, request.FILES or None, instance=product)
    elif hasattr(product, 'storage'):
        product = product.storage  
        form = StorageForm(request.POST or None, request.FILES or None, instance=product)
    else:
        form = ProductForm(request.POST or None, request.FILES or None, instance=product)

    if form and form.is_valid():
        form.save()
        return redirect('product_list')

    return render(request, 'products/edit_product.html', {'form': form, 'product': product})


@user_passes_test(superuser_required)
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('product_list')