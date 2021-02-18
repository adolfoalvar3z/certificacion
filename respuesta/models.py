from django.db import models
from django.contrib.auth.models import User
from core.models import Pregunta


# Create your models here.
class Respuesta(models.Model):
    respuesta = models.TextField('Respuesta otorgada', blank=False, null=False)
    fecha_respuesta = models.DateField('Fecha de Respuesta', blank=False, null=False, auto_now_add=True)
    pregunta = models.ForeignKey('core.Pregunta', on_delete=models.PROTECT, null=False, blank=False)
    user = models.OneToOneField(User, on_delete=models.PROTECT, default='17318072')

    def __str__(self):
        """Return username."""
        return self.user.username
