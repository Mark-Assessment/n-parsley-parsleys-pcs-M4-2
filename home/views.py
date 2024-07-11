from django.shortcuts import render, redirect
from django.urls import reverse
from products.models import Product

# Create your views here.

def home(request):
    discounted_products = Product.objects.filter(is_discounted=True)
    featured_products = Product.objects.filter(is_featured=True)
    return render(request, 'home/index.html', {
        'discounted_products': discounted_products,
        'featured_products': featured_products
    })

def set_currency(request, currency):
    conversion_rates = {
        'GBP': 1.0,
        'USD': 1.33,
        'EUR': 1.13,
    }
    conversion_rate = conversion_rates.get(currency, 0.75)
    request.session['currency_info'] = f'{currency}:{conversion_rate}'
    request.session['currency'] = currency
    return redirect(request.META.get('HTTP_REFERER', reverse('home')))