from django.shortcuts import render
from django.http import HttpResponse
from .models import Informaticas, Mecanicas, Electronicas

# Create your views here.

def index(request):
    title = "Inicio"

    data = {
        "title": title,
    }

    return render(request,'miapp/index.html', data)


def comunicados(request):
    title = "Comunicados Universidad"
    total_comunicados = Informaticas.objects.count()
    comunicados = Informaticas.objects.all()

    data = {
        "title": title,
        "total_comunicados":total_comunicados,
        "comunicados":comunicados
    }

    return render(request,'miapp/comunicados.html' ,data)

