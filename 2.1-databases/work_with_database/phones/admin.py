from django.contrib import admin
from .models import Phone


@admin.register(Phone)
class PhonesAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name', 'price']