from django.db import models
from ckeditor.fields import RichTextField

class Servs(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length= 30)
    profesion = models.CharField(null = True, max_length = 30)
    servicio_ofrecido = models.CharField(null = True,max_length = 30)
    email =  models.CharField(null = True, max_length = 200)
    descripcion = RichTextField(null = True)
    
    def __str__(self):
          
         return f'Nombre: {self.nombre} - Apellido: {self.apellido}  - Profesión:  {self.profesion} - Servicio ofrecido: {self.servicio_ofrecido} -  Email: {self.email}' 
        
    