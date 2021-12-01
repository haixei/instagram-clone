from rest_framework import permissions
from rest_framework.permissions import IsAdminUser, SAFE_METHODS


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        try:
            return obj.author == request.user
        except AttributeError:
            return obj.user == request.user
