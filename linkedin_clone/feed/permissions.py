from rest_framework import permissions


class CanEditDeleteAnyPost(permissions.BasePermission):
    """The User can delete/update any post."""

    def has_permission(self, request, view):
        return request.user.has_perm('feed.can_edit_delete_any_post')


class CanEditDeleteOwnPost(permissions.BasePermission):
    """The User can only delete/update their own post."""

    def has_object_permission(self, request, view, obj):
        return request.user.has_perm('feed.can_edit_delete_own_post') or obj.post_owner.user == request.user
