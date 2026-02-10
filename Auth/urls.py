# Auth/urls.py  ← এই ফাইলে অবশ্যই থাকতে হবে

from django.urls import path
from .views import * 

urlpatterns = [          # ← এই নাম ঠিকঠাক "urlpatterns" হতে হবে (ছোট হাতের s দিয়ে শেষ)
    # path('', views.some_view, name='some-name'),
    path('login/', signin, name='login'),
    path('register/', register, name='register'),
]