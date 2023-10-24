from django.contrib import admin
from .models import Mecanicas
from .models import Electronicas
from .models import Informaticas

# Register your models here.
admin.site.register(Informaticas)
admin.site.register(Electronicas)
admin.site.register(Mecanicas)