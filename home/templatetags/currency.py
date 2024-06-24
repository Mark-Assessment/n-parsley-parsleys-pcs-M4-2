from django import template
from decimal import Decimal

register = template.Library()

currency_symbols = {
    'GBP': '£',
    'USD': '$',
    'EUR': '€',
}

@register.filter(name='convert_price')
def convert_price(value, currency_info):
    """
    Converts a price to the specified currency using the conversion rate and symbol.
    """
    try:
        currency, conversion_rate = currency_info.split(':')
        value = Decimal(value)
        conversion_rate = Decimal(conversion_rate)
        converted_value = value * conversion_rate
        symbol = currency_symbols.get(currency, '$')
        return f"{symbol}{converted_value:,.2f}"
    except (ValueError, TypeError, InvalidOperation):
        return value 
