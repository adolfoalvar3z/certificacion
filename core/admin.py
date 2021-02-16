from django.contrib import admin
from .models import Pregunta
from .models import Respuesta
from .models import Certificado


# Register your models here.

class PreguntaAdmin(admin.ModelAdmin):
    pass


class CertificadoAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'fecha_certificado')
    pass


class RespuestaAdmin(admin.ModelAdmin):
    list_display = ('user', 'fecha_respuesta', 'respuesta', 'pregunta')
    readonly_fields = ('respuesta', 'pregunta', 'user', 'fecha_respuesta')
    pass


admin.site.register(Pregunta, PreguntaAdmin)

admin.site.register(Certificado, CertificadoAdmin)

admin.site.register(Respuesta, RespuestaAdmin)
