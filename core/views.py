from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from consulta.models import Certificado

# Create your views here.
def home(request):
    usuarios = User.objects.all()
    certificados = Certificado.objects.all()

    return render(request, "core/home.html",{'usuarios':usuarios, 'certificados':certificados})


