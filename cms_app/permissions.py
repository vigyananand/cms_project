from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in ['GET', 'HEAD'] or obj.owner == request.user

class IsOwnerOrPublicPost(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in ['GET', 'HEAD'] or (obj.is_public or obj.owner == request.user)
