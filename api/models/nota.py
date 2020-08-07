from django.db import models
from api.models import Curso , Profile

class Nota(models.Model):
    estudiante =  models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, blank=True, null=True)
    nota = models.PositiveIntegerField(default=0)
    create = models.DateField(auto_now_add=True)

    def __str__(self):
        return "("+str(self.estudiante)+","+str(self.curso)+","+str(self.nota)+")"