from django.db import models

# Create your models here.
class Pregunta(models.Model):
    pregunta = models.TextField('Pregunta a ser consultada', blank=False, null=False)

    def __str__(self):
        """Return username."""
        return self.pregunta
