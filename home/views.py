from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def set_currency(request, currency):
    request.session['currency'] = currency
    return redirect(request.META.get('HTTP_REFERER', reverse('home')))