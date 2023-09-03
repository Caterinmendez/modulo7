from django.forms import ModelForm
from django import forms
from ...models import Tarea
from django.utils import timezone


                  
class TareaForm(ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'vencimiento','identificador', 'etiqueta_tarea', 'estados',]
        widgets = {
            'vencimiento': forms.DateInput( attrs={'type': 'date' , 'value': f'{timezone.now().date()}'}),
        }