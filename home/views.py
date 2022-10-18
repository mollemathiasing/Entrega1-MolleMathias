from re import template
from ssl import HAS_TLSv1_1
from xmlrpc.client import NOT_WELLFORMED_ERROR
from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader   
from home.models import User
from django.shortcuts import render, redirect   
from home.forms import BusquedaPersonaFormulario, PersonaFormulario


def input_user(request):
    
    if request.method == 'POST':
        
        formulario = PersonaFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data 
            nombre = data['nombre']
            apellido = data['apellido']
            edad = data['edad']
            fecha_nacimiento = data['fecha_nacimiento']  
            if not fecha_nacimiento:
                fecha_nacimiento = datetime.now()
            
            
            persona = User(nombre=nombre, apellido=apellido, edad=edad, fecha_nacimiento=fecha_nacimiento)
            persona.save()
        
            return redirect ('view_user')   
    
    formulario = PersonaFormulario()
            
    return render(request, 'home/input_user.html', {'formulario': formulario})   


def view_user(request):
    
        
    nombre = request.GET.get('nombre', None)
    
    if nombre:
        personas = User.objects.filter(nombre__icontains=nombre)
    else:
        personas = User.objects.all()
    
    formulario = BusquedaPersonaFormulario()
    
    return render(request, 'home/view_user.html', {'personas': personas, 'formulario' : formulario})

def index(request):
    
    return render(request, 'home/index.html')