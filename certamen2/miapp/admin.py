from django.contrib import admin
from .models import Carrera
from .models import Docente
from .models import Comunicado

# Register your models here.
admin.site.register(Carrera)
admin.site.register(Docente)
admin.site.register(Comunicado)