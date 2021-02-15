from django.db import models

# Create your models here.
from django.utils.timezone import now


class Preguntas(models.Model):
    pregunta = models.TextField('Pregunta a ser consultada', blank=False, null=False)


class Respuestas(models.Model):
    respuesta = models.TextField('Pregunta a ser consultada', blank=False, null=False)
    fecha_respuesta = models.DateField('Fecha de respuesta', blank=False, null=False)
    pregunta = models.ForeignKey(
        'Preguntas',
        on_delete=models.CASCADE,
    )
    r_usuario = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )

class Certificados(models.Model):
    fecha_certificado = models.DateField('Fecha de respuesta', blank=False, null=False)
    c_usuario = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )