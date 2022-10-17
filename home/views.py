from re import template
from ssl import HAS_TLSv1_1
from xmlrpc.client import NOT_WELLFORMED_ERROR
from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader   
import random
from home.models import User
from django.shortcuts import render, redirect   
from home.forms import BusquedaPersonaFormulario, PersonaFormulario

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

def input_user(request):
    
    if request.method == 'POST':
        
        formulario = PersonaFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data  #atributo de los formualrios q una vez validados te da la info limpia q vamos a poder usar
               
            nombre = data['nombre']
            apellido = data['apellido']
            edad = data['edad']
            fecha_nacimiento = data.get('fecha_nacimiento', datetime.now())  #si viene una fecha la uso, sino usa el datetime.now
            
            
            persona = User(nombre=nombre, apellido=apellido, edad=edad, fecha_nacimiento=fecha_nacimiento)
            persona.save()
        
            return redirect ('view_user')   #si se guarda el ususario correctamente va a ver personas
    
    formulario = PersonaFormulario()
            
    return render(request, 'home/input_user.html', {'formulario': formulario})   