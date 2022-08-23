from django.contrib import admin
from .models import Sensor, Measurement


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    pass

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    pass
