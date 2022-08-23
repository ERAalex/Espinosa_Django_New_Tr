from rest_framework import serializers
from .models import Measurement, Sensor
from django.db import models

# TODO: опишите необходимые сериализаторы


# Добавить измерение. Указываются ID датчика и температура.
class MeasurementSerializer(serializers.ModelSerializer):
    # благодаря related_name='measurements наши модели связаны и я могу вызвать поля из Sensor (т.е. к какому счетчику отнести измерения)
    sensor = models.ForeignKey(Sensor, related_name='measurements', on_delete=models.CASCADE)

    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at', 'sensor' ]



# изменение, удаление счетчика + полная инфа по счетчику
class SensorDetail(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)  #### !!! ТУТ ЯВНО СВЯЗЬ, т.е. надо связать 2 таблицы в models. Foreign например

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']



# Создать счетчик + вывести все счетчики, Краткая инфа
class SensorSeeAll(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

