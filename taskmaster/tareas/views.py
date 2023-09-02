from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Tarea
from .forms.tareas.forms import TareaForm

# Create your views here.
def index(request):
    return render(request,"tareas/index.html")

"""def home(request):
    return render(request,"tareas/home.html")"""

class CrearListaTarea(ListView):
    model = Tarea 
    template_name = 'tareas/home.html'
    context_objects_name = 'context'

    def get_queryset(self):
        queryset = super().get_queryset()
        filtro = self.request.GET.get('filtro')

        if filtro:
            queryset = queryset.filter(titulo__contains=filtro)

        return queryset


class CrearTarea(CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tareas/layouts/partials/crearTarea.html'
    success_url = reverse_lazy('home')

class EditarTarea(UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tareas/layouts/partials/editarTarea.html'
    success_url = reverse_lazy('home')

class EiminarTarea(DeleteView):
    model = Tarea
    success_url = reverse_lazy('home')


def listarTarea(request):
    tarea = Tarea.objects.all()
    return render(request, 'tareas/home.html' ,{"context": tarea})
