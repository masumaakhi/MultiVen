from django.shortcuts import render, redirect
from .models import Product
from vendor.models import vendor

def add_product(request):

    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        is_active = True if request.POST.get('is_active') == "on" else False

        vendor = vendor.objects.get(user=request.user)

        Product.objects.create(
            name=name,
            description=description,
            price=price,
            stock=stock,
            is_active=is_active,
            vendor=vendor
        )

        return redirect('/')

    return render(request, "product/add_product.html")