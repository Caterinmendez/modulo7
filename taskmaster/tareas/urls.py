from django.contrib import admin
from django.urls import path, include
from . import views
from .views import PostUpdateView, EiminarTarea, TareaListView


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', TareaListView.as_view(), name='home'),
    path('crearTarea/', views.crearTarea, name='crearTarea'),
    path('editarTarea/<pk>/', PostUpdateView.as_view(), name= 'editarTarea'),
    path('eliminarTarea/<pk>/', EiminarTarea.as_view(), name= 'eliminarTarea'),
    path('cambiarEstado/<id>/', views.cambiarEstado, name= 'cambiarEstado'),
    path('comentario/<id>/', views.comentario, name= 'comentario'),
    path('tareasCompletadas/', views.tareasCompletadas, name='tareasCompletadas'),
    path('excluiMetaCumplida/', views.excluirMetaCumplida, name= 'excluirMetaCumplida'),
]

