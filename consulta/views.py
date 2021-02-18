from django.shortcuts import render, HttpResponse

# Create your views here.
def consulta(request):
    return render(request, "consulta/consultar.html")