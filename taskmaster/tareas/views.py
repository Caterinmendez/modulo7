from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, View
from .models import Tarea
from .forms.tareas.forms import TareaForm

# Create your views here.
def index(request):
    return render(request,"tareas/index.html")


def crearTarea(request):
    form = TareaForm()    
    if request.method == 'POST':
        form = TareaForm(request.POST)
        
        if form.is_valid():
            titulo = form.cleaned_data["titulo"]
            descripcion = form.cleaned_data["descripcion"]
            vencimiento = form.cleaned_data["vencimiento"]
            estados = form.cleaned_data["estados"]
            identificador = form.cleaned_data["identificador"]
            etiqueta_tarea = form.cleaned_data["etiqueta_tarea"]

            post = Tarea(
                titulo = titulo,
                descripcion = descripcion,
                vencimiento = vencimiento,
                estados = estados,
                identificador = identificador,
                etiqueta_tarea = etiqueta_tarea,                
            )
            post.save()
            return redirect('home')
        else:
            return render(request, 'tareas/layouts/partials/crearTarea.html', {"form":form})
    return render(request, 'tareas/layouts/partials/crearTarea.html', {"form":form})


class PostUpdateView(UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tareas/layouts/partials/editarTarea.html'
    success_url = reverse_lazy('home')


class EiminarTarea(DeleteView):
    model = Tarea
    success_url = reverse_lazy('home')


class TareaListView(View):
    def get(self, request):
        queryset = Tarea.objects.filter(identificador=request.user)
        etiqueta_tarea = request.GET.get('etiqueta_tarea')

        if etiqueta_tarea:
            queryset = queryset.filter(etiqueta_tarea=etiqueta_tarea)

        return render(request, 'tareas/home.html', {"context": queryset})



def cambiarEstado(request, id):
    tarea = Tarea.objects.get(pk=id)
    if request.method == "POST":
        tarea.estados = 'meta cumplida'
        tarea.save()
        return redirect('home') 