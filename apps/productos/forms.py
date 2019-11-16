from django import forms
from apps.productos.models import Productos

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = [
            'nombre',
            'unidades',
        ]
        label = {
            'nombre' : 'Nombre',
            'unidades': 'Unidades',
            
        }
        widget = {
            'nombre': forms.Textarea(attrs={'class':'form-control'}),
            'unidades': forms.TextInput(attrs={'class':'form-control'}),
            
            
        }

