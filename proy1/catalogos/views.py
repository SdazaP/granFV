from django.shortcuts import render
from catalogos.models import Carrera

def homeCatalogos(request):
    return render(request, 'homeCatalogos.html')

def carrerasRead(request):
    carreras = Carrera.objects.all()
    data = {'carreras':carreras}
    return render(request, 'carrerasRead.html', data)

def datosRead(request):
    #Obtención de los datos
    """ 
    estudiantes = Estudiantes.objects.all
    data = {'estudiantes': estudiantes}
     
    """
    data = {
        'nombre' : 'Ruben',
        'edad' : 22,
        'promedio' : 90.0
    }
    return render(request,'datosRead.html', data)