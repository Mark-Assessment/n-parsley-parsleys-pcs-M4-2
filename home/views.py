from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.


def home(request):
    return render(request, 'home/index.html')


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
