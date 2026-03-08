# Product/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from Vendor.models import Vendor
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Product, Category
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import CustomPermission
from .permissions import IsVendorUser
from Vendor.models import Vendor
from django_filters.rest_framework import DjangoFilterBackend

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

@api_view(['GET'])
def demoAPI(request):
    response = {
        "Name": "Product API",
        "Message": "This is a demo API for Product"
    }
    return Response(response, status=status.HTTP_201_CREATED)

class demoAPIView(APIView):

    def get(self, request):
        response = {
            "Name": "Product API",
            "Message": "This is a demo API for Product"
        }
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request):
        return Response(
            {"message": "Post Request"},
            status=status.HTTP_201_CREATED
        )

    def put(self, request):
        return Response(
            {"message": "Put Request"},
            status=status.HTTP_200_OK
        )

    def delete(self, request):
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsVendorUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'category']
        
    def get_queryset(self):
        vendor = Vendor.objects.filter(user=self.request.user).first()
        if not vendor:
            return Product.objects.none()
        return Product.objects.filter(vendor=vendor).order_by('-id')

    def perform_create(self, serializer):
        vendor = Vendor.objects.filter(user=self.request.user).first()
        serializer.save(vendor=vendor)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CustomPermission]