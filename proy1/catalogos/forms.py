from django import forms
from catalogos.models import Carrera,Aula,Maestro,PlanEstudio,Materia

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