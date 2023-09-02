from django.forms import ModelForm
from django import forms
from ...models import Tarea


                  
class TareaForm(ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'vencimiento','identificador', 'etiqueta_tarea', 'estados',]