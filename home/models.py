from django.db import models

class Servs(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length= 30)
    profesion = models.CharField(null = True, max_length = 30)
    servicio_ofrecido = models.CharField(null = True,max_length = 30)
    servicio_detalle = models.CharField(null = True,max_length = 200)
    email =  models.CharField(null = True, max_length = 200)
    
    def __str__(self):
          
         return f'Nombre: {self.nombre} - Apellido: {self.apellido}  - Profesión:  {self.profesion} - Servicio ofrecido: {self.servicio_ofrecido} - Descripción: {self.servicio_detalle} - Email: {self.email}'
        
    