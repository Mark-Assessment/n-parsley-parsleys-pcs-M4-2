from decimal import Decimal
from django.utils.deprecation import MiddlewareMixin
from cart.models import CartItem

class CurrencyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        currency = request.session.get('currency', 'GBP')
        request.currency = currency

        conversion_rates = {
            'GBP': Decimal('1'),
            'USD': Decimal('1.37'),
            'EUR': Decimal('1.15'),
        }

        conversion_rate = conversion_rates.get(currency, Decimal('1'))
        request.conversion_info = f"{currency}:{conversion_rate}"

        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, purchased=False)
            cart_total = sum(item.product.price * item.quantity for item in cart_items)
            request.cart_total = cart_total * conversion_rate
        else:
            request.cart_total = 0
