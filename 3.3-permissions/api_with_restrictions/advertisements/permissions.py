from rest_framework.permissions import BasePermission
from .models import Advertisement


class IsOwner(BasePermission):
    # данный параметр проверяет права на конкретный объект
    def has_object_permission(self, request, view, obj):
        # если request пользователь является собственником объекта, то можно изменять объект
        return request.user == obj.creator


