import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.http import require_GET
from .forms import CheckoutForm
from .models import Order
from cart.models import CartItem
from decimal import Decimal

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user, purchased=False)
    total = sum(item.total_price for item in cart_items)

    # Get the selected currency and conversion rate from the session
    currency_info = request.session.get('currency_info', 'GBP:1.0')
    currency, conversion_rate = currency_info.split(':')
    conversion_rate = Decimal(conversion_rate)

    # Convert total to the selected currency
    converted_total = total * conversion_rate
    converted_cart_items = [
        {
            'product': item.product,
            'quantity': item.quantity,
            'total_price': item.total_price * conversion_rate,
        }
        for item in cart_items
    ]

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_amount = converted_total
            order.save()

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
                success_url=request.build_absolute_uri(reverse('order_success')) + f'?order_id={order.id}',
                cancel_url=request.build_absolute_uri(reverse('checkout')),
                metadata={
                    'order_id': order.id,
                }
            )

            return redirect(session.url, code=303)
    else:
        form = CheckoutForm()

    return render(request, 'checkout/checkout.html', {
        'form': form,
        'cart_items': converted_cart_items,
        'total': converted_total,
        'currency': currency,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    })

@require_GET
@login_required
def order_success(request):
    order_id = request.GET.get('order_id')
    order = Order.objects.get(id=order_id, user=request.user)

    # Delete cart items after successful order
    CartItem.objects.filter(user=request.user, purchased=False).delete()

    return render(request, 'checkout/order_success.html', {'order': order})