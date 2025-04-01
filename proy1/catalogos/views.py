from django.shortcuts import render, redirect
from catalogos.models import Carrera, Aula, Maestro
from catalogos.forms import CarreraForm, AulaForm, MaestroForm

def homeCatalogos(request):
    return render(request, 'homeCatalogos.html')


#Carreras
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

#Aulas
def aulasRead(request):
    aulas = Aula.objects.all()
    data = {'aulas': aulas}
    return render(request, 'aulasRead.html', data)

def aulasCreate(request):
    if request.method == 'POST':
        form = AulaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aulasRead')
    else:
        form = AulaForm()
    return render(request, 'aulasCreate.html', {'form': form})

def aulasUpdate(request, id):
    aula = Aula.objects.get(id=id)
    if request.method == 'GET':
        form = AulaForm(instance=aula)
    else:
        form = AulaForm(request.POST, instance=aula)
        if form.is_valid():
            form.save()
            return redirect('aulasRead')
    return render(request, 'aulasCreate.html', {'form': form})

def aulasDelete(request, id):
    aula = Aula.objects.get(id=id)
    if request.method == 'POST':
        aula.delete()
        return redirect('aulasRead')
    return render(request, 'aulasDelete.html', {'aula': aula})

#Maestros
def maestrosRead(request):
    maestros = Maestro.objects.all()
    data = {'maestros': maestros}
    return render(request, 'maestrosRead.html', data)

def maestroCreate(request):
    if request.method == 'POST':
        form = MaestroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('maestrosRead')
    else:
        form = MaestroForm()
    return render(request, 'maestrosCreate.html', {'form': form})

def maestrosUpdate(request, id):
    maestro = Maestro.objects.get(id=id)
    if request.method == 'GET':
        form = MaestroForm(instance=maestro)
    else:
        form = MaestroForm(request.POST, instance=maestro)
        if form.is_valid():
            form.save()
            return redirect('maestrosRead')
    return render(request, 'maestrosCreate.html', {'form': form})

def maestrosDelete(request, id):
    maestro = Maestro.objects.get(id=id)
    if request.method == 'POST':
        maestro.delete()
        return redirect('maestrosRead')
    return render(request, 'maestrosDelete.html', {'maestro': maestro})

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

