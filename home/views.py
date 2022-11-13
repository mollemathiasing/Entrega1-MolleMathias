from home.models import Servs
from django.shortcuts import render
from home.forms import SearchServs
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def index(request):
    
    return render(request, 'home/index.html')

class ViewServs(ListView):
    model = Servs
    template_name =  'home/view_servs.html'
    
    #Buscador

      
    def get_queryset(self):
        servicio_ofrecido = self.request.GET.get('servicio_ofrecido', '')
        profesion = self.request.GET.get('profesion', '')
        if servicio_ofrecido or profesion:
            object_list = self.model.objects.filter(servicio_ofrecido__icontains=servicio_ofrecido)
            object_list = self.model.objects.filter(profesion__icontains=profesion)
        else: 
            object_list = self.model.objects.all()
               
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formulario"] = SearchServs()
        return context
    
class InputServs(CreateView):
    model = Servs
    success_url = '/view_servs'
    template_name = 'home/input_servs.html'
    fields = [ 'nombre', 
              'apellido',
              'email',
              'profesion',
              'servicio_ofrecido',
              'descripcion'
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
              'descripcion'
                             ]

    
class DeleteServs(DeleteView):
    model = Servs
    success_url =   '/view_servs'                                
    template_name =  'home/delete_servs.html' 
    
    
class ViewServ(DetailView):
    model = Servs                            
    template_name =  'home/view_serv.html'                    



