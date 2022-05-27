from rest_framework.permissions import SAFE_METHODS, BasePermission


class AllowUserCreate(BasePermission):
    def has_permission(self, request, view):
        return request.method == 'POST'

    def has_object_permission(self, request, view, obj):
        return request.method == 'POST'


class AllowUserChange(BasePermission):
    def has_permission(self, request, view):
        return request.method == 'PATCH' or request.method == 'DELETE'

    def has_object_permission(self, request, view, obj):
        print(obj)
        return obj == request.user


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS


class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        return obj.author == request.user
