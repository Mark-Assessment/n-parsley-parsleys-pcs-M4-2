from django.urls import path
from .views import checkout, order_success

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('checkout/order-success/<int:order_id>/', order_success, name='order_success'),
]