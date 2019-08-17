from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    message = "You don't own this post"

    my_safe_methods = ['PUT', 'GET', 'DELETE', 'OPTIONS']

    def has_permission(self, request, view):
        print('permission called')
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
