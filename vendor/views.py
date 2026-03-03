from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Vendor

@login_required
def vendor_dashboard(request):
    vendor = Vendor.objects.filter(user=request.user).first()
    if not vendor:
        return redirect('vendor_create_profile')

    return render(request, 'vendor/dashboard.html', {'vendor': vendor})


@login_required
def vendor_create_profile(request):
    vendor = Vendor.objects.filter(user=request.user).first()
    if vendor:
        return redirect('vendor_dashboard')

    if request.method == "POST":
        Vendor.objects.create(
            user=request.user,
            name=request.POST.get("name"),
            phone=request.POST.get("phone"),
            address=request.POST.get("address"),
            city=request.POST.get("city"),
            state=request.POST.get("state"),
            country=request.POST.get("country"),
            zip=request.POST.get("zip"),
            logo=request.FILES.get("logo"),
            description=request.POST.get("description"),
        )
        return redirect('vendor_dashboard')

    # ✅ এখানে create_profile.html render হবে
    return render(request, "vendor/create_profile.html")