from django.contrib import admin
from django.urls import path, include
from . import views
from .views import CrearListaTarea, CrearTarea, EditarTarea, EiminarTarea


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.listarTarea, name='home'),
    path('crearTarea/', CrearTarea.as_view(), name='crearTarea'),
    path('editarTarea/<pk>/', EditarTarea.as_view(), name= 'editarTarea'),
    path('eliminarTarea/<pk>/', EiminarTarea.as_view(), name= 'eliminarTarea'),

]

