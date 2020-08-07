from rest_framework import viewsets, mixins
from api.models import Nota, Rol
from api.serializers import NotaSerializer

class NotaViewset(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    serializer_class = NotaSerializer
    queryset = Nota.objects.all()


    