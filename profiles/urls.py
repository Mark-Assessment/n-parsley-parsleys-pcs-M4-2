from django.urls import path
from . import views

urlpatterns = [
    path('profile/my-profile', views.profile, name='profile'),
]