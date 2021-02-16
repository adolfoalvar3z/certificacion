from django.contrib import admin
from .models import Pregunta
from .models import Respuesta
from .models import Certificado


# Register your models here.

class PreguntaAdmin(admin.ModelAdmin):
    pass


class CertificadoAdmin(admin.ModelAdmin):
    readonly_fields = ['user', 'fecha_certificado']
    pass

class RespuestaAdmin(admin.ModelAdmin):
    readonly_fields = ['pregunta', 'user', 'fecha_respuesta']
    pass

admin.site.register(Pregunta, PreguntaAdmin)

admin.site.register(Certificado, CertificadoAdmin)

admin.site.register(Respuesta, RespuestaAdmin)
