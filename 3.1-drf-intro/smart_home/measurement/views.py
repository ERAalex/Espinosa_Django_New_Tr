# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework import generics

from .serializers import SensorDetail, MeasurementSerializer, SensorSeeAll
from .models import Sensor, Measurement




# Вывести все счетчики + возможность создание счетчика
class See_and_Create_All_Api(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSeeAll


# изменение, удаление счетчика +  полная инфа
class Count_Update_Delete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetail



# Вывести все показания + возможность создание нового показания, Указываются ID датчика и температура.
class Meas_Create(generics.ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer



class Meas_Update_Delete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer