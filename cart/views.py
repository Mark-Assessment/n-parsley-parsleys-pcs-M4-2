from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.crypto import get_random_string
from .models import CartItem
from products.models import Product
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))

    if request.user.is_authenticated:
        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product, purchased=False)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        cart_item, created = CartItem.objects.get_or_create(session_key=session_key, product=product, purchased=False)

    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity
    cart_item.total_price = cart_item.product.price * cart_item.quantity
    cart_item.save()

    return redirect('cart_detail')

def cart_detail(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user, purchased=False)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        cart_items = CartItem.objects.filter(session_key=session_key, purchased=False)

    total = sum(item.total_price for item in cart_items)
    return render(request, 'cart/cart_detail.html', {'cart_items': cart_items, 'total': total})

def remove_from_cart(request, item_id):
    if request.user.is_authenticated:
        item = get_object_or_404(CartItem, id=item_id, user=request.user)
    else:
        session_key = request.session.session_key
        item = get_object_or_404(CartItem, id=item_id, session_key=session_key)
    item.delete()
    return redirect('cart_detail')

@receiver(user_logged_in)
def merge_cart_items(sender, request, user, **kwargs):
    session_key = request.session.session_key
    if not session_key:
        return

    session_cart_items = CartItem.objects.filter(session_key=session_key, purchased=False)
    user_cart_items = CartItem.objects.filter(user=user, purchased=False)

    for session_item in session_cart_items:
        user_item, created = user_cart_items.get_or_create(product=session_item.product)
        if not created:
            user_item.quantity += session_item.quantity
        else:
            user_item.quantity = session_item.quantity
        user_item.total_price = user_item.product.price * user_item.quantity
        user_item.save()

    session_cart_items.delete()