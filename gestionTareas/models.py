from django.db import models

# Create your models here.

class tarea(models.Model):
    Descripcion = models.CharField(max_length=128,default='0')
    Fecha_Creacion = models.CharField(max_length=128,default='0')
    Fecha_Entrega = models.CharField(max_length=128,default='0')
    Usuario = models.CharField(max_length=128,default='0')
    Estado = models.CharField(max_length=128,default='Programada')
    
class usuarios(models.Model):
    nombre = models.CharField(max_length=128,default='')
    apellido = models.CharField(max_length=128,default='')
    psw_usuario = models.CharField(max_length=128,default='')
    codigo_usuario = models.CharField(max_length=128,default='')

