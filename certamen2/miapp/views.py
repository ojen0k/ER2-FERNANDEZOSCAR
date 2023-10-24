from django.shortcuts import render
from django.http import HttpResponse
from .models import Informaticas, Mecanicas, Electronicas, Entidades
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    title = "Inicio"

    data = {
        "title": title,
    }

    return render(request,'miapp/index.html', data)


def comunicados(request):
    title = "Comunicados Universidad"
    total_comunicados = int(Informaticas.objects.count()) + int(Electronicas.objects.count()) + int(Mecanicas.objects.count())
    comunicados = Informaticas.objects.all()
    comunicados2= Electronicas.objects.all()
    comunicados3 = Mecanicas.objects.all()
    

    data = {
        "title": title,
        "total_comunicados":total_comunicados,
        "comunicados":comunicados,
        "comunicados2":comunicados2,
        "comunicados3":comunicados3,
    }

    return render(request,'miapp/comunicados.html' ,data)

def com_informatica(request):
    title = "Comunicados Informatica"
    total_comunicados = Informaticas.objects.count()
    comunicados = Informaticas.objects.all()
    

    data = {
        "title": title,
        "total_comunicados":total_comunicados,
        "comunicados":comunicados,
    }

    return render(request,'miapp/com_inf.html' ,data)

def com_electronica(request):
    title = "Comunicados Electronica"
    total_comunicados = Electronicas.objects.count()
    comunicados = Electronicas.objects.all()
    

    data = {
        "title": title,
        "total_comunicados":total_comunicados,
        "comunicados":comunicados,
    }

    return render(request,'miapp/com_elo.html' ,data)


def com_mecanica(request):
    title = "Comunicados Mecanica"
    total_comunicados = Mecanicas.objects.count()
    comunicados = Mecanicas.objects.all()
    

    data = {
        "title": title,
        "total_comunicados":total_comunicados,
        "comunicados":comunicados,
    }

    return render(request,'miapp/com_mec.html' ,data)

def entidades(request):
    title = "Entidades Universidad"
    entidades = Entidades.objects.all()

    data ={
        "title": title,
        "entidades":entidades,
    }
    return render(request, 'miapp/header.html', data)



