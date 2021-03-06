from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    my_safe_methods = ['PUT', 'GET', 'PATCH', 'DELETE', 'OPTIONS']

    def has_permission(self, request, view):
        if request.method in self.my_safe_methods:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user != obj.moder and request.method == "GET":
            return True
        elif request.user == obj.moder and request.method in self.my_safe_methods:
            return True
        else:
            return False


class IsMediaManager(BasePermission):
    def has_permission(self, request, view, obj):
        if request.user.userprofile.type == 0:
            return True
        else:
            return False


class IsMediaManagerOrReadOnly(BasePermission):
    def has_permission(self, request, view, obj):
        if request.user.userprofile.type == 0:
            return True
        if request.user.userprofile.type != 0 and request.method == 'GET':
            return True
        else:
            return False


class IsManager(BasePermission):
    def has_permission(self, request, view):
        if request.user.userprofile.type == 1:
            return True
        else:
            return False


class IsManagerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.userprofile.type == 1:
            return True
        if request.user.userprofile.type != 1 and request.method == 'GET':
            return True
        else:
            return False


class NotMediaManager(BasePermission):
    def has_permission(self, request, view):
        if request.user.userprofile.type != 0:
            return True
        else:
            return False


class NotManager(BasePermission):
    def has_permission(self, request, view):
        if request.user.userprofile.type != 1:
            return True
        else:
            return False
