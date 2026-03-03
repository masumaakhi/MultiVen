from django.shortcuts import render, redirect
from .models import Product
from Vendor.models import Vendor

def add_product(request):
    if request.method == "POST":
        # ✅ vendor profile আছে কিনা আগে চেক
        vendor = Vendor.objects.filter(user=request.user).first()
        if not vendor:
            return redirect("/admin/Vendor/vendor/add/")  # বা নিজের vendor-create page

        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        is_active = True if request.POST.get('is_active') == "on" else False

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