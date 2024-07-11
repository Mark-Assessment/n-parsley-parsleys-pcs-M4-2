import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.http import require_GET
from .forms import CheckoutForm
from .models import Order
from cart.models import CartItem
from profiles.models import UserDefaults
from decimal import Decimal

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user, purchased=False)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        cart_items = CartItem.objects.filter(session_key=session_key, purchased=False)

    total = sum(item.total_price for item in cart_items)

    # Get the selected currency and conversion rate from the session
    currency_info = request.session.get('currency_info', 'GBP:1.0')
    currency, conversion_rate = currency_info.split(':')
    conversion_rate = Decimal(conversion_rate)

    # Convert total to the selected currency
    converted_total = total
    converted_cart_items = [
        {
            'product': item.product,
            'quantity': item.quantity,
            'total_price': item.total_price,
        }
        for item in cart_items
    ]

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
            order.total_amount = converted_total
            order.save()

            # Create Stripe payment session
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': currency,
                        'product_data': {
                            'name': item.product.name,
                        },
                        'unit_amount': int((item.product.price * conversion_rate) * 100),
                    },
                    'quantity': item.quantity,
                } for item in cart_items],
                mode='payment',
                success_url=request.build_absolute_uri(reverse('order_success', kwargs={'order_id': order.id})),
                cancel_url=request.build_absolute_uri(reverse('checkout')),
                metadata={
                    'order_id': order.id,
                }
            )

            return redirect(session.url, code=303)
    else:
        initial_data = {}
        if request.user.is_authenticated:
            try:
                user_defaults = UserDefaults.objects.get(user=request.user)
                initial_data = {
                    'first_name': user_defaults.first_name,
                    'last_name': user_defaults.last_name,
                    'address_line_1': user_defaults.address_line1,
                    'address_line_2': user_defaults.address_line2,
                    'city': user_defaults.town_or_city,
                    'county': user_defaults.county,
                    'postcode': user_defaults.postcode,
                    'country': user_defaults.country,
                }
            except UserDefaults.DoesNotExist:
                pass
        form = CheckoutForm(initial=initial_data)

    return render(request, 'checkout/checkout.html', {
        'form': form,
        'cart_items': converted_cart_items,
        'total': converted_total,
        'currency': currency,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    })

@require_GET
def order_success(request, order_id):
    if request.user.is_authenticated:
        order = get_object_or_404(Order, id=order_id, user=request.user)
        # Delete cart items for authenticated user after successful order
        CartItem.objects.filter(user=request.user, purchased=False).delete()
    else:
        session_key = request.session.session_key
        order = get_object_or_404(Order, id=order_id, user__isnull=True, session_key=session_key)
        # Delete cart items for guest user after successful order
        CartItem.objects.filter(session_key=session_key, purchased=False).delete()

    return render(request, 'checkout/order_success.html', {'order': order})