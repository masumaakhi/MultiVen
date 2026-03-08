from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model= User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }