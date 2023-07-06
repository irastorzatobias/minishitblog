from django import forms
from .models import Entrada


class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['titulo', 'contenido', 'categorias']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-input'}),
            'contenido': forms.Textarea(attrs={'class': 'form-input'}),
            'categorias': forms.SelectMultiple(attrs={'class': 'form-input'}),
        }
