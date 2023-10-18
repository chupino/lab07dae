from django import forms
from django.forms import SelectDateWidget
from .models import Evento,Usuario

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'fecha', 'descripcion', 'organizador']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre']

class RegistroEventoForm(forms.Form):
    usuario = forms.ModelChoiceField(queryset=Usuario.objects.all(), label='Selecciona un Usuario')
    evento = forms.ModelChoiceField(queryset=Evento.objects.all(), label='Selecciona un Evento')
