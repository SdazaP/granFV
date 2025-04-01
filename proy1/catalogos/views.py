from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from catalogos.models import Carrera, Aula, Maestro, PlanEstudio, Materia, Alumno
from catalogos.forms import CarreraForm, AulaForm, MaestroForm, PlanEstudioForm, MateriaForm, AlumnoForm

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

#CRUD PLANES ESTUDIO

def planesRead(request):
    planesEstudio= PlanEstudio.objects.all()
    data = {'planesEstudio':planesEstudio}
    return render(request, 'planesRead.html', data)
        
def planesCreate(request):
    if request.method == 'POST':
        form = PlanEstudioForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('planesRead')  # Redirect after saving
    else:
        form = PlanEstudioForm()

    return render(request, 'planesCreate.html', {'form': form})


def planesUpdate(request, id):
    planesEstudio = PlanEstudio.objects.get(id=id)  # Get the PlanEstudio object by ID
    
    if request.method == 'GET':
        form = PlanEstudioForm(instance=planesEstudio)  # Render the form with existing data
    else:
        form = PlanEstudioForm(request.POST, instance=planesEstudio)  # Bind the form with POST data
        if form.is_valid():
            form.save()  # Save the updated PlanEstudio instance
        return redirect('planesRead')
    
    return render(request, 'planesCreate.html', {'form': form})   

def planesDelete(request, id):
    planesEstudio = PlanEstudio.objects.get(id=id)  # Fetch the PlanEstudio object by ID
    if request.method == 'POST':  # Confirm delete on POST request
        planesEstudio.delete()  # Delete the PlanEstudio object
        return redirect('planesRead')  # Redirect to the list of PlanEstudio objects
    
    # Render the confirmation page with the PlanEstudio object if GET request
    return render(request, 'planesDelete.html', {'planesEstudio': planesEstudio})

#CRUD Materias
def materiasRead(request):
    materias= Materia.objects.all()
    data = {'materias':materias}
    return render(request, 'materiasRead.html', data)

def materiasCreate(request):
    if request.method == 'POST':
        form = MateriaForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('materiasRead')  # Redirect after saving
    else:
        form = MateriaForm()

    return render(request, 'materiasCreate.html', {'form': form})


def materiasUpdate(request, id):
    materia = Materia.objects.get(id=id)  # Obtener la Materia por ID o devolver 404
    
    if request.method == 'POST':
        form = MateriaForm(request.POST, instance=materia)  # Formulario con datos de la solicitud
        if form.is_valid():
            form.save()
            return redirect('materiasRead')  # Asegúrate de que esta vista existe
    else:
        form = MateriaForm(instance=materia)  # Formulario con datos existentes
    
    return render(request, 'materiasCreate.html', {'form': form})


def materiasDelete(request, id):
    materia = Materia.objects.get(id=id)  # Fetch the PlanEstudio object by ID
    if request.method == 'POST':  # Confirm delete on POST request
        materia.delete()  # Delete the PlanEstudio object
        return redirect('materiasRead')  # Redirect to the list of PlanEstudio objects
    
    # Render the confirmation page with the PlanEstudio object if GET request
    return render(request, 'materiasDelete.html', {'materia': materia})

# Vistas para Alumnos
def alumnosRead(request):
    alumnos = Alumno.objects.all().select_related('carrera', 'plan_estudio')
    return render(request, 'alumnosRead.html', {'alumnos': alumnos})

def alumnosCreate(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alumnosRead')
    else:
        form = AlumnoForm()
    return render(request, 'alumnosCreate.html', {'form': form})

def alumnosUpdate(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('alumnosRead')
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, 'alumnosCreate.html', {'form': form})

def alumnosDelete(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    if request.method == 'POST':
        alumno.delete()
        return redirect('alumnosRead')
    return render(request, 'alumnoDelete.html', {'alumno': alumno})

def get_planes_estudio(request):
    carrera_id = request.GET.get('carrera_id')
    if carrera_id:
        planes = PlanEstudio.objects.filter(carrera_id=carrera_id)
        options = '<option value="">---------</option>'
        for plan in planes:
            options += f'<option value="{plan.id}">{plan.nombre}</option>'
        return JsonResponse({'options': options})
    return JsonResponse({'options': '<option value="">---------</option>'})


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

