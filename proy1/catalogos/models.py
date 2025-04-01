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
    
class Alumno(models.Model):
    ESTADOS = [
        ('ACT', 'Activo'),
        ('EGR', 'Egresado'),
        ('BAJ', 'Baja'),
    ]
    
    matricula = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50, blank=True)
    fecha_nacimiento = models.DateField()
    email = models.EmailField()
    telefono = models.CharField(max_length=15, blank=True)
    estado = models.CharField(max_length=3, choices=ESTADOS, default='ACT')
    carrera = models.ForeignKey(Carrera, on_delete=models.PROTECT)
    plan_estudio = models.ForeignKey(PlanEstudio, on_delete=models.PROTECT, blank=True, null=True)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.matricula} - {self.nombre} {self.apellido_paterno}"

