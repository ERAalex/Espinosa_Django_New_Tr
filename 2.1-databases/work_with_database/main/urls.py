
from django.contrib import admin
from django.urls import path
from phones.views import index, show_catalog, show_product, sort_name, sort_price_max, sort_price_min



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('catalog/', show_catalog, name='catalog'),
    path('catalog/<slug:slug>/', show_product, name='phone'),
    path('sort_by_name', sort_name, name='sort_by_name'),
    path('sort_by_price_max', sort_price_max, name='sort_by_price_max'),
    path('sort_by_price_min', sort_price_min, name='sort_by_price_min'),
]
