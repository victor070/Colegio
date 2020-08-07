from rest_framework.permissions import BasePermission
from ..models import Rol

class IsPermisoTeacher(BasePermission):

    def has_object_permission(self, request, view, obj):
        try:
            Rol.objects.get(
                user=request.user,
                curso=obj,
                is_teacher=True
            )
        except Rol.DoesNotExist:
            return False
        return True