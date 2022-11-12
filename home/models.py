from django.db import models

class User(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length= 30)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField(null = True)
    profesion = models.CharField(null = True, max_length = 30)
    # servicio_ofrecido = models.CharField(max_length = 30)
    # servicio_detalle = models.CharField(max_length = 200)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.edad} {self.fecha_nacimiento} '
    