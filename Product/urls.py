# Product/urls.py

from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', ProductViewSet, basename='product')
router.register('category', CategoryViewSet, basename='category')

urlpatterns = [
    path('add-product/', add_product, name="add_product"),
    path('my-products/', my_products, name="my_products"),
    path('demo/', demoAPIView.as_view(), name='demo_api'),
] + router.urls
