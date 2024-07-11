from django import forms
from .models import UserDefaults

class UserDefaultsForm(forms.ModelForm):
    class Meta:
        model = UserDefaults
        fields = ['first_name', 'last_name', 'phone_number', 'address_line1', 'address_line2', 'town_or_city', 'county', 'postcode', 'country']