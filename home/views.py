from home.models import Servs
from django.shortcuts import render   

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def index(request):
    
    return render(request, 'home/index.html')

class ViewServs(ListView):
    model = Servs
    template_name =  'home/view_servs.html'
    
    
class InputServs(CreateView):
    model = Servs
    success_url = '/view_servs'
    template_name = 'home/input_servs.html'
    fields = [ 'nombre', 
              'apellido',
              'email',
              'profesion',
              'servicio_ofrecido',
              'servicio_detalle' ,
              ]
    
class EditServs(UpdateView):
    model = Servs
    success_url =   '/view_servs'                                   
    template_name =  'home/edit_servs.html'                    
    fields = [ 'nombre', 
              'apellido',
              'email',
              'profesion',
              'servicio_ofrecido',
              'servicio_detalle' ,
                ]

    
class DeleteServs(DeleteView):
    model = Servs
    success_url =   '/view_servs'                                
    template_name =  'home/delete_servs.html'                    



