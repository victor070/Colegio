from django.db import models
from django.contrib.auth.models import User
from api.models import Profile, Curso


class Rol(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE ,null=True, blank=True )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE ,null=True, blank=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE ,null=True, blank=True)

    invited_by = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name='invited_by'
    )
    remaining_invitations = models.PositiveSmallIntegerField(default=0)
    
    is_teacher = models.BooleanField('teacher', default=False)
    is_studen = models.BooleanField('studen', default=True)
    is_active = models.BooleanField('activo', default=True)

    def __str__(self):
        return '@{} at #{}'.format(
            self.user.username,
            self.curso.curso
        )