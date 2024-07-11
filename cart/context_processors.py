from .models import CartItem
from decimal import Decimal

def cart_total(request):
    total = Decimal(0.00)
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user, purchased=False)
    else:
        session_key = request.session.session_key
        if session_key:
            cart_items = CartItem.objects.filter(session_key=session_key, purchased=False)
        else:
            cart_items = []

    total = sum(item.total_price for item in cart_items)
    
    # Get the selected currency and conversion rate from the session
    currency_info = request.session.get('currency_info', 'GBP:1.0')
    currency, conversion_rate = currency_info.split(':')
    conversion_rate = Decimal(conversion_rate)
    
    converted_total = total * conversion_rate

    return {
        'cart_total': converted_total,
        'currency': currency
    }