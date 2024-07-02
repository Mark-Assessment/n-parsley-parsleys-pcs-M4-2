from django import template

register = template.Library()

@register.filter
def to(value, max_value):
    return range(1, int(max_value) + 1)