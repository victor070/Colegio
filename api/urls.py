from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import url
from api import viewsets
from .viewsets import estudiantes as EstudiantesViewset 

router = DefaultRouter()
router.register(r'user', viewsets.UserViewset)
router.register(r'curso', viewsets.CursoViewset)
router.register(r'curso/(?P<curso>[-a-zA-Z0-9_]*)/estudiante', viewsets.EstudiantesViewset, basename="estudiantes")
router.register(r'nota', viewsets.NotaViewset)




urlpatterns = [
    path('api/', include(router.urls)),
    url(r"^api/token", obtain_auth_token, name="api-token"),
    path('api-auth/', include('rest_framework.urls')),
]
