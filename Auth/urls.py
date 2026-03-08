from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')

urlpatterns = [
    path('login/', signin, name='login'),
    path('register/', register, name='register'),
    path('token/', ObtainTokenView.as_view(), name='token'),
    path('token/refresh/', AccessTokenFromRefreshToken.as_view(), name='refresh'),
] + router.urls