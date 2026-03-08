# Auth/views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
# Create your views here.
def signin(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect("dashboard")   # or dashboard
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "auth/login.html")


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('password_confirm')

        if not all([username, email, password, confirm_password, firstname, lastname]):
            messages.error(request, "All fields are required!")
            return redirect('register')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('register')

        User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=firstname,
            last_name=lastname
        )

        messages.success(request, "User created successfully!")
        return redirect('login')

    return render(request, 'auth/signup.html')

class UserViewSet(ModelViewSet):
    queryset= User.objects.all()
    serializer_class= UserSerializer


class ObtainTokenView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is None:
            return Response(
                {'error': 'Invalid credentials'},
                status=status.HTTP_400_BAD_REQUEST
            )

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            },
            status=status.HTTP_200_OK
        )
class AccessTokenFromRefreshToken(APIView):

    def post(self, request):
        refresh = request.data.get('refresh')

        try:
            token = RefreshToken(refresh)
            print(token)

            user = User.objects.get(id=token['user_id'])

            access = AccessToken.for_user(user)

            return Response(
                {'access': str(access)},
                status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response(
                {'error': 'Invalid refresh token'},
                status=status.HTTP_400_BAD_REQUEST
            )