from django import forms

    
class SearchServs(forms.Form):
    nombre = forms.CharField(max_length = 30, required=False)
    apellido = forms.CharField(max_length = 30, required=False)
    email = forms.CharField(max_length = 30, required=False)
    profesion = forms.CharField(max_length = 30, required=False)
    servicio_ofrecido = forms.CharField(max_length = 30, required=False)
    servicio_detalle = forms.CharField(max_length = 30, required=False)
    
    
    
  