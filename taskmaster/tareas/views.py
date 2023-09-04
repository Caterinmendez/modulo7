from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, ListView
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
            comentario = form.cleaned_data["comentario"]

            post = Tarea(
                titulo = titulo,
                descripcion = descripcion,
                vencimiento = vencimiento,
                estados = estados,
                identificador = identificador,
                etiqueta_tarea = etiqueta_tarea,    
                comentario = comentario,            
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


class TareaListView(ListView):
    model = Tarea
    template_name = 'tareas/home.html'
    context_object_name = 'context'

    def get_queryset(self):
        queryset = Tarea.objects.filter(identificador=self.request.user)
        etiqueta_tarea = self.request.GET.get('etiqueta_tarea')

        if etiqueta_tarea:
            queryset = queryset.filter(etiqueta_tarea=etiqueta_tarea)

        queryset = queryset.exclude(estados = 'meta cumplida')
        return queryset



def cambiarEstado(request, id):
    tarea = Tarea.objects.get(pk=id)
    if request.method == "POST":
        tarea.estados = 'meta cumplida'
        tarea.save()
        return redirect('home') 


def comentario(request, id):
    tarea = Tarea.objects.get(pk=id)

    if request.method == "POST":
        nuevo_comentario = request.POST.get('comentario')  
        tarea.comentario = nuevo_comentario  
        tarea.save() 
        return redirect('home')  

def tareasCompletadas(request):
    tareasCompletadas = Tarea.objects.filter(estados = 'meta cumplida')
    return render(request, 'tareas/layouts/partials/tareasCompletadas.html',{'tareasCompletadas': tareasCompletadas})

def excluirMetaCumplida(request):
    excluirTarea = Tarea.objects.exclude(estados = 'meta cumplida')
    return render(request, 'home', {'excluirTarea': excluirTarea } ) 