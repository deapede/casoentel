from django import forms
from apps.ventas.models import Ventas

class VentasForm(forms.ModelForm): 
    class Meta                   : 
        model                    = Ventas
        fields                   = [
            'fecha',
            'comentarios'
        ]
        label                    = {
            'fecha'              : 'Fecha',
            'comentarios'        : 'Comentarios',
            
        }
        widget                   = {
            'fecha'              : forms.DateInput(attrs  = {'class': 'form-control'}),
            'comentarios'        : forms.Textarea(attrs = {'class': 'form-control'}),
            
            
        }