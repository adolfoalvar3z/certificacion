from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Certificado(models.Model):
    fecha_certificado = models.DateField('Fecha de Certificado', blank=False, null=False, auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT, default='17318072')

    def __str__(self):
        """Return username."""
        return self.user.username