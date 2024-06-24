from django import template

register = template.Library()

@register.filter(name='currency')
def currency(value):
    """
    Formats a number as currency.
    """
    return "£{:,.2f}".format(value)
