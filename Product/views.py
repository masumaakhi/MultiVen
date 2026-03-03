# Product/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from Vendor.models import Vendor

@login_required
def add_product(request):
    vendor = Vendor.objects.filter(user=request.user).first()
    if not vendor:
        return redirect('vendor_create_profile')

    if request.method == "POST":
        Product.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            price=request.POST.get('price'),
            stock=request.POST.get('stock'),
            is_active=True if request.POST.get('is_active') == "on" else False,
            vendor=vendor
        )
        return redirect('my_products')

    return render(request, "product/add_product.html")

@login_required
def my_products(request):
    vendor = Vendor.objects.filter(user=request.user).first()
    if not vendor:
        return redirect('vendor_create_profile')

    products = Product.objects.filter(vendor=vendor).order_by('-id')
    return render(request, "product/my_products.html", {"products": products})