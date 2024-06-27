from django.utils import timezone
from django.db import models
from distutils.command.upload import upload
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
    nombreCategoria =  models.CharField(max_length=50, verbose_name='Nombre de Categoria')

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    idProducto = models.CharField(primary_key=True, max_length=15, verbose_name='SKU')
    nombreProducto = models.CharField(max_length=50, verbose_name='Nombre del Producto', blank=False)
    marca = models.CharField(max_length=100, verbose_name='Marca', blank=False)
    modelo = models.CharField(max_length=200, verbose_name='Modelo', blank=False)
    precio = models.IntegerField(blank=True, null=True, verbose_name="Precio", validators=[MaxValueValidator(9999999999)])
    descripcion = models.CharField(max_length=2000, verbose_name='Descripcion de Producto', default='Sin descripción')
    stock = models.IntegerField(default=0, verbose_name='Cantidad en stock', validators=[MinValueValidator(0)])
    imagen = models.ImageField(upload_to="imagenes", null=True, verbose_name='Imagen')
    categoria = models.ForeignKey('Categoria', default=1, on_delete=models.CASCADE, verbose_name='Categoria')
    def __str__(self):
        return f'{self.skuProducto} -> {self.nombreProducto}'



class Boleta(models.Model):
    id_boleta = models.AutoField(primary_key=True)
    total = models.BigIntegerField()
    fechaCompra = models.DateTimeField(blank=False, null=False, default=timezone.now)
    estado = models.CharField(max_length=50, default='Procesando Pedido')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.id_boleta)



class detalle_boleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    idProducto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()
    

    def __str__(self):
        return str(self.id_detalle_boleta)



