from django import forms
from .models import Category, Brand

class ProductFilterForm(forms.Form):
    price_min = forms.DecimalField(required=False, label='Min Price', min_value=0)
    price_max = forms.DecimalField(required=False, label='Max Price', min_value=0)
    rating_min = forms.DecimalField(required=False, label='Min Rating', min_value=0, max_value=5, decimal_places=1)
    rating_max = forms.DecimalField(required=False, label='Max Rating', min_value=0, max_value=5, decimal_places=1)
    
    category = forms.ModelChoiceField(
        required=False, 
        queryset=Category.objects.all(), 
        label='Category',
        empty_label='Select a category'
    )
    
    brand = forms.ModelChoiceField(
        required=False, 
        queryset=Brand.objects.all(), 
        label='Brand',
        empty_label='Select a brand'
    )
    
    sort_by = forms.ChoiceField(
        required=False, 
        choices=[
            ('', 'Sort By'),
            ('name', 'Name'),
            ('price', 'Price'),
            ('rating', 'Rating'),
        ], 
        label='Sort By'
    )