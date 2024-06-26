from django import forms
from .models import Category, Brand

class ProductFilterForm(forms.Form):
    price_min = forms.DecimalField(required=False, max_digits=10, decimal_places=2, label='Min Price')
    price_max = forms.DecimalField(required=False, max_digits=10, decimal_places=2, label='Max Price')
    rating_min = forms.DecimalField(required=False, max_digits=3, decimal_places=2, label='Min Rating')
    rating_max = forms.DecimalField(required=False, max_digits=3, decimal_places=2, label='Max Rating')
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, label='Category')
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), required=False, label='Brand')
