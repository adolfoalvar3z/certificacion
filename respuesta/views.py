from django.shortcuts import render, HttpResponse

# Create your views here.
def respuesta(request):
    return render(request, "respuesta/respuesta.html")