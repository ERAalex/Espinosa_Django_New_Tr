from django.contrib import admin
from .models import Product, Stock, StockProduct


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    pass

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('address',)
    pass


@admin.register(StockProduct)
class StockProductAdmin(admin.ModelAdmin):
    list_display = ('stock', 'product', 'quantity', 'price')
    pass
