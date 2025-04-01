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

class Aula(models.Model):
    nombre = models.CharField(max_length=20, unique=True)
    capacidad = models.PositiveIntegerField()
    
    def __str__(self):
        return "{0}-{1}".format(self.nombre, self.capacidad)
    
class Maestro(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    especialidad = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return "{0}-{1}-{2}-{3}-{4}-{5}".format(self.nombre, self.apellidos, self.email, self.telefono, self.especialidad, self.activo)