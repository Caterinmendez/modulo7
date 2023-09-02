from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Etiqueta(models.Model):
    tipo = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.tipo

class Tarea(models.Model):
    ESTADOS = [
        ('iniciado', 'iniciado'),
        ('casi-casi', 'casi-casi'),
        ('meta cumplida', 'meta cumplida')
]

    titulo = models.CharField(max_length=50, blank=False, null=False)
    descripcion = models.TextField(blank=True, null=True)
    vencimiento = models.DateField()
    estados = models.CharField(max_length=20, choices=ESTADOS, default='iniciado')
    identificador = models.ForeignKey(User, on_delete=models.CASCADE)
    etiqueta_tarea = models.ForeignKey(Etiqueta, default=1, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.titulo} > {self.identificador}'
