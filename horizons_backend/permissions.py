from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.permissions import IsAdminUser, SAFE_METHODS

"""
Custom permission classes for API access control.

Classes:
    IsOwnerOrReadOnly: Grants read-only access for any user, but restricts
                       write access to the owner of the object.
    IsAdminUserOrReadOnly: Defines admin only permissions to super users,
                       otherwise read on
    IsOwnerOrAdmin: Allows both an owner and an allow to edit and delete
    a post or comment.
"""


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsAdminUserOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super(
            IsAdminUserOrReadOnly,
            self).has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user or request.user.is_staff