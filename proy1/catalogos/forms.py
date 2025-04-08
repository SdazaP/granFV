from django import forms
from catalogos.models import Carrera,Aula,Maestro,PlanEstudio,Materia,Alumno

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #mostrar con bootstrap
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})

class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #mostrar con bootstrap
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})

class MaestroForm(forms.ModelForm):
    class Meta:
        model = Maestro
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #mostrar con bootstrap
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})

class PlanEstudioForm(forms.ModelForm):
    class Meta:
        model = PlanEstudio
        fields = '__all__'  # This will include all fields, including the foreign key 'carrera'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add the Bootstrap form-control class to all fields
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        
        # Optional: Customize the foreign key field ('carrera') for additional control
        self.fields['carrera'] = forms.ModelChoiceField(
            queryset=Carrera.objects.all(),
            empty_label="Selecciona una carrera",  # Optional: Placeholder text
            widget=forms.Select(attrs={'class': 'form-control'})  # Ensure dropdown uses form-control class
        )

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = '__all__'  # Esto incluirá todos los campos, incluyendo 'plan_estudio'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Agregar la clase Bootstrap 'form-control' a todos los campos
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),
            'fecha_inscripcion': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'readonly': True
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Aplicar clase form-control a todos los campos
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        
        # Manejo especial para fechas
        if self.instance and self.instance.pk:
            # Formatear fecha de nacimiento para input type="date"
            if hasattr(self.instance, 'fecha_nacimiento') and self.instance.fecha_nacimiento:
                self.initial['fecha_nacimiento'] = self.instance.fecha_nacimiento.strftime('%Y-%m-%d')
            
            # Manejar fecha_inscripcion solo si existe en el modelo
            if 'fecha_inscripcion' in self.fields:
                self.fields['fecha_inscripcion'].disabled = True
                if hasattr(self.instance, 'fecha_inscripcion') and self.instance.fecha_inscripcion:
                    self.initial['fecha_inscripcion'] = self.instance.fecha_inscripcion.strftime('%Y-%m-%d')
        
        # Carga dinámica de planes de estudio
        if 'carrera' in self.data:
            try:
                carrera_id = int(self.data.get('carrera'))
                self.fields['plan_estudio'].queryset = PlanEstudio.objects.filter(carrera_id=carrera_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['plan_estudio'].queryset = self.instance.carrera.planestudio_set.all()

class PlanesForm(forms.ModelForm):
    class Meta:
        model = PlanEstudio

        fields = [
            'clave',
            'nombre',
            'carrera'
        ]

        labels = {
            'clave' : 'CLAVE',
            'nombre' : 'NOMBRE',
            'carrera' : 'CARRERA'   
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #mostrar con bootstrap
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})