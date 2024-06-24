from django.utils.deprecation import MiddlewareMixin
from decimal import Decimal

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


