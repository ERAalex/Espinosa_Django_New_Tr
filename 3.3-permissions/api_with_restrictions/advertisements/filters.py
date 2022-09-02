from django_filters import rest_framework as filters, DateTimeFromToRangeFilter
from .models import Advertisement

class AdvertisementFilter(filters.FilterSet):
    created_at = filters.DateTimeFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ["creator", "created_at", "status"]

