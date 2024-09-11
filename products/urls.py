from django.urls import path
from . import views

urlpatterns = [
    path('all-products', views.all_products, name='all_products'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
    path('manage/', views.product_list, name='product_list'),
    path('add/<str:product_type>/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
