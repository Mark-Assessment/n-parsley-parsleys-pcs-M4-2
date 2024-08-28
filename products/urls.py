from django.urls import path
from . import views

urlpatterns = [
    path('all-products', views.all_products, name='all_products'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
]
