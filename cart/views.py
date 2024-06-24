from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import CartItem
from products.models import Product

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product, purchased=False)

    if not created:
        cart_item.quantity += 1
    cart_item.total_price = cart_item.product.price * cart_item.quantity
    cart_item.save()

    return redirect(reverse('cart_detail'))

def cart_detail(request):
    cart_items = CartItem.objects.filter(user=request.user, purchased=False)
    return render(request, 'cart/cart_detail.html', {'cart_items': cart_items})
