from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    roles = models.ManyToManyField(User,through='rol', through_fields=('curso','user'))
    curso = models.CharField(max_length=50, unique=True)
    create = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.curso
    
    