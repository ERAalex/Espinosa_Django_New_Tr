from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Advertisement
from advertisements.serializers import AdvertisementSerializer, UserSerializer
from advertisements.permissions import IsOwner



class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    queryset_check = Advertisement.objects.filter(status="OPEN")
    count = queryset_check.count()
    if count >= 10:
        serializer_class = UserSerializer
    else:
        serializer_class = AdvertisementSerializer
        permission_classes = [IsOwner]




    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)





# Разрешения прописаны в permissions.py

