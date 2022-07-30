from django.contrib import admin
from django.urls import path
from calculator import views

urlpatterns = [
#    path('<choose>/', views.dishes, name='dishes'),    # вариант использования без шаблона. только запросы и http
    path('index/<decision>', views.index, name='index'),
    path('', views.start, name='starts')

]
