from django.contrib import admin
from .models import Certificado

# Register your models here.
class CertificadoAdmin(admin.ModelAdmin):
    list_display = ('user', 'fecha_certificado')
    readonly_fields = ('user', 'fecha_certificado')
    pass

admin.site.register(Certificado, CertificadoAdmin)
