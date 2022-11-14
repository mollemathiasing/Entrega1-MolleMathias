from django import forms


    
class SearchServs(forms.Form):
    servicio_ofrecido = forms.CharField(max_length=30, required=False)
    profesion = forms.CharField(max_length=30, required=False)
    
  