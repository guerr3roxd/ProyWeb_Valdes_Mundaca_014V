from django import forms 
from django.forms import ModelForm
from django.forms import widgets
from django.forms.widgets import Widget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Categoria, Producto

class ProductoForm(forms.ModelForm):
    class Meta: 
        model=Producto
        fields=['idProducto', 'nombreProducto', 'marca', 'modelo', 'precio', 'descripcion', 'stock', 'imagen', 'categoria']
        labels={
            'idProducto': 'SKU',
            'nombreProducto': 'Nombre del Producto',
            'marca': 'Marca',
            'modelo': 'Modelo',
            'precio': 'Precio',
            'descripcion': 'Descripcion',
            'stock': 'Cantidad en stock',
            'imagen': 'Imagen',
            'categoria': 'Categoria'
        }
        widgets={
            'idProducto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el SKU del producto'
                }
            ),
            'nombreProducto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre del producto'
                }
            ),
            'marca': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la marca del producto'
                }
            ),
            'modelo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el modelo del producto'
                }
            ),
            'precio': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el precio del producto (SOLO NUMEROS): EJ:390000'
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la descripcion del producto'
                }
            ),
            'stock': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la cantidad en stock del producto'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la imagen del producto'
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la categoria del producto'
                }
            )
            
        }


class RegistroUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'username', 'first_name', 'last_name', 'email', 'password1', 'password2']