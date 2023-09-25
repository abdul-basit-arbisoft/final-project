from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow GET requests to anyone, and restrict PUT and DELETE
    requests to the post owner.
    """

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        
        return obj.post_owner.user == request.user
