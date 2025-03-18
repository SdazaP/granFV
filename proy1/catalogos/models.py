from django.db import models

# Create your models here.
class Carrera(models.Model):
    clave = models.CharField(max_length=4)
    nombre = models.CharField(max_length=60, blank=True)

    #Metodos
    def __str__(self):
        return "{0}-{1}".format(self.clave,self.nombre)

class PlanEstudio(models.Model):
    clave = models.CharField(max_length=8)
    nombre = models.CharField(max_length=50)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.clave, self.nombre, self.carrera)
    
class Materia(models.Model):
    clave = models.CharField(max_length=8)
    nombre = models.CharField(max_length=50)
    creditos = models.IntegerField()
    PlanEstudio = models.ForeignKey(PlanEstudio, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}-{1}".format(self.clave, self.nombre,)
    
    