from rest_framework.permissions import BasePermission
from api.models import Rol
class IsActiveStudent (BasePermission):
    def has_permission(self, request, view):
        try:
            Rol.objects.get(
                user=request.user,
                curso = view.curso,
                is_studen=True

            )
        except Rol.DoesNotExist:
            return False
        return True

class IsSelfEstuden(BasePermission):
    """Allow access only to member owners."""

    def has_permission(self, request, view):
        """Let object permission grant access."""
        obj = view.get_object()
        return self.has_object_permission(request, view, obj)

    def has_object_permission(self, request, view, obj):
        """Allow access only if member is owned by the requesting user."""
        return request.user == obj.user
