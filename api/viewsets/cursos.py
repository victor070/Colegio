from rest_framework import viewsets, mixins
from api.models import Curso, Rol
from api.serializers import CursoSerializer
from rest_framework.permissions import IsAuthenticated
from api.permisos import IsPermisoTeacher
class CursoViewset(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    serializer_class = CursoSerializer
    queryset = Curso.objects.all()
    lookup_field="curso"

    def perform_create(self, serializer):
        curso = serializer.save()
        user = self.request.user
        profile = user.profile
        Rol.objects.create(
            user = user,
            profile = profile,
            curso = curso,
            is_teacher = True,
            remaining_invitations = 10
        ) 
    
    def get_permissions(self):
        permissions = [IsAuthenticated]
        if self.action in ['update','partial_update','retrieve']:
            permissions.append(IsPermisoTeacher)
        return[permission() for permission in permissions]