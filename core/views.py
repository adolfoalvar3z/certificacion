from django.shortcuts import render, HttpResponse
from .models import User
from .models import Certificado



# Create your views here.
def home(request):
    usuarios = User.objects.all()
    certificados = Certificado.objects.all()

    return render(request, "core/home.html",{'usuarios':usuarios, 'certificados':certificados})

def generar(request):
    return render(request, "core/home.html")
