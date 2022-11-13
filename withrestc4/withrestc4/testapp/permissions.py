from rest_framework.permissions import SAFE_METHODS, BasePermission
from django.contrib.auth.models import User
class IsReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return False

class IsGETOrPatch(BasePermission):
    def has_permission(self, request, view):
        allowed_methods=['GET','PATCH']
        if request.method in allowed_methods:
            return True
        else:
            return False

class SunnyPermission(BasePermission):
    def has_permission(self, request, view):
        username=request.user.username
        if username.lower() == 'sunny':
            return True
        elif username != '' and len(username) %2 ==0 and request.method in SAFE_METHODS:
            return True
        else:
            return False