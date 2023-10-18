from django.db import models



class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre 

class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.DateField()
    descripcion = models.TextField()
    organizador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    inscritos = models.ManyToManyField(Usuario, through='RegistroEvento', related_name='eventos_inscritos')
    
    def __str__(self):
        return self.nombre 


class RegistroEvento(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)