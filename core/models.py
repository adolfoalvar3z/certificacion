from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.utils.timezone import now


class Pregunta(models.Model):
    pregunta = models.TextField('Pregunta a ser consultada', blank=False, null=False)

    def __str__(self):
        """Return username."""
        return self.pregunta

class Respuesta(models.Model):
    respuesta = models.TextField('Respuesta otorgada', blank=False, null=False)
    fecha_respuesta = models.DateField('Fecha de Respuesta', blank=False, null=False, auto_now_add=True)
    pregunta = models.ForeignKey('Pregunta', on_delete=models.PROTECT, null=False)
    user = models.OneToOneField(User, on_delete=models.PROTECT, default='17318072')

    def __str__(self):
        """Return username."""
        return self.user.username

class Certificado(models.Model):
    fecha_certificado = models.DateField('Fecha de Certificado', blank=False, null=False, auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT, default='17318072')

    def __str__(self):
        """Return username."""
        return self.user.username
