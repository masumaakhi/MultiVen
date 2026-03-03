# Vendor/urls.py
from django.urls import path
from .views import vendor_dashboard, vendor_create_profile

urlpatterns = [
    path('dashboard/', vendor_dashboard, name='vendor_dashboard'),
    path('create-profile/', vendor_create_profile, name='vendor_create_profile'),
]
