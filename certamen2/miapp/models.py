from django.db import models
from django.contrib.auth.models import User, Group



class Informaticas(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=30)
    detalle = models.CharField(max_length=250)
    detalle_corto = models.CharField(max_length=50)
    publicado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    entidad = models.ForeignKey(Group, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to="miapp/static/miapp/img/", blank=True, null=True)

    def __str__(self) -> str:
        return self.titulo
    
class Mecanicas(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=30)
    detalle = models.CharField(max_length=250)
    detalle_corto = models.CharField(max_length=50)
    publicado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    entidad = models.ForeignKey(Group, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to="miapp/static/miapp/img/", blank=True, null=True)

    def __str__(self) -> str:
        return self.titulo
    

class Electronicas(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=30)
    detalle = models.CharField(max_length=250)
    detalle_corto = models.CharField(max_length=50)
    publicado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    entidad = models.ForeignKey(Group, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to="miapp/static/miapp/img/", blank=True, null=True)

    def __str__(self) -> str:
        return self.titulo
    
