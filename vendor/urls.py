# Vendor/urls.py
from django.urls import path
from .views import vendor_dashboard, vendor_create_profile
from rest_framework.routers import DefaultRouter
from .views import *

router= DefaultRouter()
router.register('vendors', VendorViewSets, basename= 'vendor')

urlpatterns = [
    path('dashboard/', vendor_dashboard, name='vendor_dashboard'),
    path('create-profile/', vendor_create_profile, name='vendor_create_profile'),
] + router.urls
