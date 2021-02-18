from django.contrib import admin
from .models import *

# Register your models here.
class RespuestaAdmin(admin.ModelAdmin):
    list_display = ('user', 'fecha_respuesta', 'respuesta', 'pregunta')
    readonly_fields = ('respuesta', 'pregunta', 'user', 'fecha_respuesta')
    pass

admin.site.register(Respuesta, RespuestaAdmin)
