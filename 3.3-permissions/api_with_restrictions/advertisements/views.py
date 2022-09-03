from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from .models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from advertisements.permissions import IsOwner
from .filters import AdvertisementFilter
from django_filters import rest_framework as filters




class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()

    serializer_class = AdvertisementSerializer
    #IsAuthenticatedOrReadOnly - позволит не зарегестрированным пользователям делать безопасные запросы:
    # Get - например
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwner]

    filters_backends = [DjangoFilterBackend]
    filter_class = AdvertisementFilter


    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


