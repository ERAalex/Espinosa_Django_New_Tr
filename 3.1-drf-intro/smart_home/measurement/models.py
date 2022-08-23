from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    id = models.AutoField(primary_key=True,)
    name = models.CharField(max_length=30, verbose_name='Имя счетчика')
    description = models.CharField(max_length=20, verbose_name='расположение датчика')

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete= models.CASCADE, related_name="measurements", default=False)
    temperature = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)

