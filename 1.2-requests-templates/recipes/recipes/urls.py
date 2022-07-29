from django.contrib import admin
from django.urls import path
from calculator.views import dishes

urlpatterns = [
    path('dishes/', dishes),
]
