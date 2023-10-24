from django.db import models
    
class Informaticas(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=30)
    detalle = models.CharField(max_length=250)
    detalle_corto = models.CharField(max_length=50)
    

    def __str__(self) -> str:
        return self.titulo
    
class Mecanicas(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=30)
    detalle = models.CharField(max_length=250)
    detalle_corto = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.titulo
    

class Electronicas(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=30)
    detalle = models.CharField(max_length=250)
    detalle_corto = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.titulo
    
