from django.shortcuts import render, redirect
from django.contrib.auth import logout

def dashboard(request):
    return render(request, 'home/dashboard.html')

def user_logout(request):
    logout(request)
    return redirect('dashboard')
