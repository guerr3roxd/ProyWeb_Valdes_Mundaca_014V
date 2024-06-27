from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .models import Categoria, Producto, Boleta, detalle_boleta
from .forms import ProductoForm, RegistroUserForm
from core.compras import Carrito
from django.contrib import messages
from django.utils import timezone

def index(request):
    return render(request, 'index.html')

def contactanos(request):
    return render(request, 'contactanos.html')

def ideasdecortes(request):
    return render(request, 'ideasdecortes.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = RegistroUserForm()
    return render(request, 'registro.html', {'form': form})

def sobrenosotros(request):
    return render(request, 'sobrenosotros.html')

def servicios(request):
    return render(request, 'servicios.html')

@login_required
def productos(request):
    datos = Producto.objects.all()              #similar a select * from Producto
    return render(request, 'productos.html',{"datos":datos})

def crear(request):
    if request.method == 'POST':
        productoForm = ProductoForm(request.POST, request.FILES)
        if Producto.objects.filter(idProducto=request.POST.get('idProducto')).exists():
            messages.error(request, f"El producto con SKU {request.POST.get('idProducto')} ya existe.")
            return render(request, 'crear.html', {'productoForm': productoForm})
        if productoForm.is_valid():
            productoForm.save()
            return redirect('productos')
    else:
        productoForm = ProductoForm()
    return render(request, 'crear.html', {'productoForm': productoForm})

def detalle(request, id):
    producto = get_object_or_404(Producto, idProducto=id)   #buscamos un objeto por medio del id
    return render(request, 'detalle.html', {'producto': producto})


def modificar(request, id):
    producto = get_object_or_404(Producto, idProducto=id)
    if request.method=='POST':
        formulario = ProductoForm(request.POST, request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'El producto se ha modificado exitosamente.')
            return redirect('productos')
        else:
            messages.error(request, 'Hubo un error al modificar el producto. Revisa que hayas llenado correctamente los campos que deseas modificar.')
    else:
        formulario = ProductoForm(instance=producto)
    return render(request,'modificar.html', {'forModificar': formulario, 'Producto': producto})


def eliminar(request, id):
    producto = get_object_or_404(Producto, idProducto=id)   #buscamos un obj por medio del id
    if request.method=='POST':
        if 'elimina' in request.POST:
            producto.delete()           #eliminamos un objeto
            return redirect('productos')
    return render(request, 'eliminar.html', {'producto': producto})  

def cerrar(request):
    logout(request)
    return redirect('index')


def registrar(request):
    data={                          #parámetro que llega al template
        'form': RegistroUserForm()
    }
    if request.method=="POST":
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()       #crear un objeto en el backend
            user = authenticate(username=formulario.cleaned_data["username"], 
                    password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect('index') 
        data["form"]=formulario           
    return render(request, 'registration/registrar.html',data)





def agregar_producto(request, id):
    producto = get_object_or_404(Producto, idProducto=id)
    carrito = Carrito(request)

    resultado = carrito.agregar(producto)
    if resultado == "No hay suficiente stock":
        messages.error(request, f"Lo sentimos, no hay suficiente stock disponible del producto {producto.modelo}.")
    else:
        messages.success(request, f"Producto {producto.modelo} añadido al carrito exitosamente.")

    return redirect('tienda')


def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, idProducto=id)
    carrito = Carrito(request)
    
    if str(producto.idProducto) in carrito.carrito:
        cantidad = carrito.carrito[str(producto.idProducto)]['cantidad']
        producto.stock += cantidad  # Aumentar el stock en la cantidad eliminada
        producto.save()
        
        if cantidad > 1:
            carrito.restar(producto)
        else:
            del carrito.carrito[str(producto.idProducto)]
            messages.success(request, f"Producto {producto.modelo} eliminado con éxito.")
        
        carrito.guardar_carrito()
        
    return redirect('tienda')


def restar_producto(request, id):
    producto = get_object_or_404(Producto, idProducto=id)
    carrito = Carrito(request)
    
    if str(producto.idProducto) in carrito.carrito:
        cantidad = carrito.carrito[str(producto.idProducto)]['cantidad']
        
        if cantidad > 1:
            carrito.restar(producto)
            messages.success(request, f"Producto {producto.modelo} Restado con éxito.")
        else:
            del carrito.carrito[str(producto.idProducto)]
            producto.stock += 1  # Aumentar el stock en 1 unidad
            messages.success(request, f"Producto {producto.modelo} Eliminado con éxito.")
            producto.save()
        
        carrito.guardar_carrito()
        
    return redirect('tienda')



def limpiar_carrito(request):
    carrito_compra = Carrito(request)
    for producto_id, datos in carrito_compra.carrito.items():
        producto = get_object_or_404(Producto, idProducto=producto_id)
        producto.stock += datos['cantidad']
        producto.save()
        messages.success(request, f"Productos {producto.modelo} eliminados con éxito.")
    carrito_compra.limpiar()
    
    return redirect('tienda') 

def tienda(request):
    productos = Producto.objects.all()
    carrito = Carrito(request)
    total = carrito.total()
    datos = {
        'productos': productos,
        'total': total
    }
    return render(request, 'tienda.html', datos)

def generarBoleta(request):
    carrito = Carrito(request)
    # Verificar si el carrito está vacío
    if not carrito.carrito.items():
        messages.error(request, "No hay productos en el carrito. Por favor, agrega productos antes de finalizar la compra.")
        return redirect('tienda')
    # Obtener el total y el costo de envío
    total = carrito.total()
    envio = 3500
    # Crear la boleta
    boleta = Boleta.objects.create(
        total=total + envio,
        usuario=request.user
    )
    # Crear los detalles de la boleta
    for producto in carrito.carrito.values():
        if 'id_producto' in producto:
            detalle = detalle_boleta.objects.create(
                id_boleta=boleta,
                id_producto=get_object_or_404(Producto, idProducto=producto['id_producto']),
                cantidad=producto['cantidad'],
                subtotal=producto['subtotal'],
                envio=envio,
                imagen=get_object_or_404(Producto, idProducto=producto['id_producto']).imagen
            )
            print(detalle.imagen.url)
        else:
            pass
    
    # Vaciar el carrito
    carrito.limpiar()
    
    # Pasar los datos a la plantilla de detallecarrito
    context = {
        'fecha': boleta.fechaCompra,
        'productos': carrito.carrito.values(),
        'total': total,
        'envio': envio,
        'total_final': total + envio,
        'estado': boleta.estado,
        'usuario': boleta.usuario
    }
    
    return render(request, 'detallecarrito.html', context)



def format_price(value):
    return "{:,.0f}".format(value)


