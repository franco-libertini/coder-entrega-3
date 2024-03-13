from django import forms
from .models import *

class AutorForm(forms.Form):
    nombre = forms.CharField(max_length=100 , required=True)
    biografia = forms.CharField(widget=forms.Textarea, required=True)
    
class CategoriaForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    
class LibroForm(forms.Form):
    titulo = forms.CharField(max_length=100, required=True)
    autor = forms.ModelChoiceField(queryset=Autor.objects.all(), required=True)
    categorias = forms.ModelMultipleChoiceField(queryset=Categoria.objects.all(), required=True)
    descripcion = forms.CharField(widget=forms.Textarea, required=False)
    precio = forms.DecimalField(max_digits=6, decimal_places=2, required=True)
    stock = forms.IntegerField(required=True)
    disponible = forms.BooleanField(required=False)
    
class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    apellido = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    
class PedidoForm(forms.Form):
    libro = forms.ModelChoiceField(queryset=Libro.objects.all(), required=True)
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), required=True)
    cantidad = forms.IntegerField(required=True)