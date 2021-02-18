from django.contrib import admin
from .models import Pregunta


# Register your models here.

class PreguntaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Pregunta, PreguntaAdmin)


