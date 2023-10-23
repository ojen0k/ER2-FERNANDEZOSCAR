from django.db import models

# Create your models here.
class Carrera(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion = models.IntegerField()

    def __str__(self) -> str:
        return self.nombre

class Docente(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    titulo = models.CharField(max_length=50)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre + " " + self.apellido
    
