from django.db import models
# Create your models here.
from django.db import models

class Usuario(models.Model):
    celular = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=1, blank=True, null=True)
    usuario_creacion = models.IntegerField(blank=True, null=True)
    id_creacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario_modificacion = models.IntegerField(blank=True, null=True)
    id_modificacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'USUARIOS'  # Nombre exacto de la tabla en la base de datos
        managed = False  # No dejes que Django gestione la tabla

    def __str__(self):
        return self.nombre



class Estado(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='estados')
    contenido = models.CharField(max_length=100, blank=True, null=True)
    usuario_creacion = models.IntegerField(blank=True, null=True)
    id_creacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario_modificacion = models.IntegerField(blank=True, null=True)
    id_modificacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ESTADOS'  # Nombre exacto de la tabla en la base de datos
        managed = False  # No dejes que Django gestione la tabla

    def __str__(self):
        return self.contenido
