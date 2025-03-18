from django.shortcuts import render

def homeCatalogos(request):
    return render(request, 'homeCatalogos.html')

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