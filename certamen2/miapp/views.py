from django.shortcuts import render
from django.http import HttpResponse
from .models import Comunicado, Carrera

# Create your views here.

def index(request):
    title = "Inicio"

    data = {
        "title": title,
    }

    return render(request,'miapp/index.html', data)


def comunicados(request):
    title = "Comunicados"

    data = {
        "title": title,
    }

    return render(request,'miapp/comunicados.html', data)

def carreras(request):
    title = "Carreras"
    total_carreras = Carrera.objects.count()
    carreras = Carrera.objects.all()
    data = {
        "title": title,
        "total_carreras":total_carreras,
        "carreras":carreras
    }
    return render(request,'miapp/carreras.html',data)

def docentes(request):
    title = "Docentes"
    
    data = {
        "title": title,
    }
    return render(request,'miapp/docentes.html',data)