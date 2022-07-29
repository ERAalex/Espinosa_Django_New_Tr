from django.contrib import admin
from django.urls import path
from calculator import views

urlpatterns = [
    path('<choose>/', views.dishes, name='dishes'),
    path('', views.index, name='index')
]
