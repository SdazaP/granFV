from django import forms
from catalogos.models import Carrera

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #mostrar con bootstrap
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})