from rest_framework.permissions import BasePermission
from .models import Advertisement


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return request.user == obj.creator
