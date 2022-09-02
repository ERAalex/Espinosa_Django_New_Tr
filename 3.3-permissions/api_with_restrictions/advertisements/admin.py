from django.contrib import admin
from advertisements.models import Advertisement


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status',)


# Register your models here.
