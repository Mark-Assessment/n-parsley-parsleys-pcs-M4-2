from django import forms
from .models import Order

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address_line_1', 'address_line_2', 'city', 'county', 'postcode', 'country']