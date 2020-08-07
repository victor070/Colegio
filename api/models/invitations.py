
from django.db import models
from api.managers import InvitationManager
from django.contrib.auth.models import User
from api.models import Curso

class Invitation(models.Model):
    

    code = models.CharField(max_length=50, unique=True)

    issued_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='issued_by'
    )
    used_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
    )

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    used = models.BooleanField(default=False)
    used_at = models.DateTimeField(blank=True, null=True)

    # Manager
    objects = InvitationManager()

    def __str__(self):
        
        return '#{}: {}'.format(self.curso.curso, self.code)
