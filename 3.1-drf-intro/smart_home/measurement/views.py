# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework import generics

from .serializers import SensorDetailSerializer, MeasurementSerializer
from .models import Sensor, Measurement




# создание счетчика
class Count_List_Create(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer



# изменение, удаление счетчика
class Count_Update_Delete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer







class Meas_Create(generics.ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class Meas_Update_Delete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer