# Product/urls.py

from django.urls import path
from .views import add_product, my_products

urlpatterns = [
    path('add-product/', add_product, name="add_product"),
    path('my-products/', my_products, name="my_products"),
]