from rest_framework import viewsets, mixins, status
from api.models import Curso, Rol, Invitation , Nota
from api.serializers import EstudianteSerializer, AddStudenSerializer, NotaSerializer, RolSerializer
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from api.permisos import IsActiveStudent, IsSelfEstuden
from rest_framework.decorators import action
from rest_framework.response import Response
from api.viewsets import UserViewset


class EstudiantesViewset(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    
    serializer_class = EstudianteSerializer
         
    
    def dispatch(self, request, *args, **kwargs):

        curso = kwargs['curso']
        self.curso = get_object_or_404(Curso,curso=curso)
        return super(EstudiantesViewset, self).dispatch(request, *args, **kwargs)
    
    def get_queryset(self):

        return Rol.objects.filter(
            curso=self.curso,
            is_studen=True
        )
    
    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = [IsAuthenticated]
        if self.action != 'create':
            permissions.append(IsActiveStudent)
        if self.action == 'invitations':
            permissions.append(IsSelfEstuden)
        return [p() for p in permissions]
        
    
    def get_object(self):

        return get_object_or_404(
            Rol,
            user__username=self.kwargs['pk'],
            curso= self.curso,
            is_studen=True,
            is_active=True
        )
    
    def perform_destroy(self, instance):
        instance.is_active=False
        instance.is_studen=False
        instance.save()

    @action(detail = True, methods=['get'])
    def invitations(self, request, *args, **kwargs):
        invitado =  Rol.objects.filter(
            curso=self.curso,
            invited_by=request.user,
            is_studen=True,
            is_active=True
        )

        member = self.get_object()
        unused_invitations = Invitation.objects.filter(
            curso=self.curso,
            issued_by=request.user,
            used=False
        ).values_list('code')
        diff = member.remaining_invitations - len(unused_invitations)

        invitations = [x[0] for x in unused_invitations]
        for i in range(0, diff):
            invitations.append(
                Invitation.objects.create(
                    issued_by=request.user,
                    curso=self.curso
                ).code
            )
        data = {
            'used_invitations': EstudianteSerializer(invitado, many=True).data,
            'invitations': invitations

        }   
        return Response(data)

    def create(self, request, *args, **kwargs):
        
        serializer = AddStudenSerializer(
            data=request.data,
            context={'curso': self.curso, 'request': request}
        )
        serializer.is_valid(raise_exception=True)
        member = serializer.save()

        data = self.get_serializer(member).data
        return Response(data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        """Add extra data to the response."""
        response = super(EstudiantesViewset, self).retrieve(request, *args, **kwargs)
        c = Curso.objects.get(curso='idiomas')
        nota = Nota.objects.filter(estudiante=1,curso=c)
        data = {
            'user': response.data,
            'NotaStudent': NotaSerializer(nota, many=True).data
        }
        response.data = data
        return response