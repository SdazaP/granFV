from django.shortcuts import render, redirect
from catalogos.models import Carrera
from catalogos.forms import CarreraForm

def homeCatalogos(request):
    return render(request, 'homeCatalogos.html')

def carrerasRead(request):
    carreras = Carrera.objects.all()
    data = {'carreras':carreras}
    return render(request, 'carrerasRead.html', data)

def carrerasCreate(request):
    if request.method == 'POST':                    #Listo para guardar datos
        form = CarreraForm(request.POST)
        if form.is_valid():                         #Llenado correcto
            form.save()
            return redirect('carrerasRead')         #Redirección a carrerasRead
    else:
        form = CarreraForm()                        #Capturar datos
    return render(request, 'carreraCreate.html',{'form':form})


def carrerasUpdate(request, id):
    carrera = Carrera.objects.get(id=id)        #Obtener carrera segun id
    if request.method == 'GET' : 
        form = CarreraForm(instance=carrera)    #Se pinta formulario
    else:
        form = CarreraForm(request.POST, instance=carrera)      #Formulario actualizado
        if form.is_valid():
            form.save()
        return redirect('carrerasRead')
    return render(request, 'carreraCreate.html', {'form':form})


def carrerasDelete(request, id):
    carrera = Carrera.objects.get(id=id)        #Obtener carrera segun id
    if request.method == 'POST':     #Confirmar eliminación
        carrera.delete()            #Se elimina de la base de datos real
        return redirect('carrerasRead')
    return render(request, 'carrerasDelete.html', {'carrera':carrera})


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

