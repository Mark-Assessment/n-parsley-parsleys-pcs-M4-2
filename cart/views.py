from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import CartItem
from products.models import Product

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product, purchased=False)

    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity
    cart_item.total_price = cart_item.product.price * cart_item.quantity
    cart_item.save()

    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart_items = CartItem.objects.filter(user=request.user, purchased=False)
    total = sum(item.total_price for item in cart_items)
    return render(request, 'cart/cart_detail.html', {'cart_items': cart_items, 'total': total})


@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('cart_detail')