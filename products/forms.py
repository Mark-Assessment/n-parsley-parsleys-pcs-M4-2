from django import forms
from .models import Category, Brand

class ProductFilterForm(forms.Form):
    price_min = forms.DecimalField(required=False, label='Min Price', min_value=0)
    price_max = forms.DecimalField(required=False, label='Max Price', min_value=0)
    rating_min = forms.DecimalField(required=False, label='Min Rating', min_value=0, max_value=5, decimal_places=1)
    rating_max = forms.DecimalField(required=False, label='Max Rating', min_value=0, max_value=5, decimal_places=1)
    
    category = forms.ChoiceField(
        required=False, 
        choices=[('', 'Select a category')] + [(category.name, category.name) for category in Category.objects.all()], 
        label='Category'
    )
    
    brand = forms.ChoiceField(
        required=False, 
        choices=[('', 'Select a brand')] + [(brand.name, brand.name) for brand in Brand.objects.all()], 
        label='Brand'
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