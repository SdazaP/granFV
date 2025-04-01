from django import forms
from catalogos.models import Carrera,Aula,Maestro

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