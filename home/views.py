from home.models import User
from django.shortcuts import render, redirect   
# from home.forms import BusquedaPersonaFormulario, PersonaFormulario

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def index(request):
    
    return render(request, 'home/index.html')

class ViewUser(ListView):
    model = User
    template_name =  'home/view_user.html'

class InputUser(CreateView):
    model = User
    success_url = '/view_user'
    template_name = 'home/input_user.html'
    fields = [ 'nombre', 'apellido', 'edad', 'fecha_nacimiento', 'profesion']
    





# def view_user(request):
    
        
#     nombre = request.GET.get('nombre', None)
    
#     if nombre:
#         personas = User.objects.filter(nombre__icontains=nombre)
#     else:
#         personas = User.objects.all()
    
#     formulario = BusquedaPersonaFormulario()
    
#     return render(request, 'home/view_user.html', {'personas': personas, 'formulario' : formulario})

