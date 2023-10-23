from django.contrib import admin
from .models import Carrera
from .models import Docente

# Register your models here.
admin.site.register(Carrera)
admin.site.register(Docente)