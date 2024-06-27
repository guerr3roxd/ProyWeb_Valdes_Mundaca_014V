from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name="index"),
    path('productos/', views.productos, name="productos"),
    path('crear/', views.crear, name="crear"),
    path('contactanos/', views.contactanos, name='contactanos'),
    path('ideasdecortes/', views.ideasdecortes, name='ideasdecortes'),
    path('registro/', views.registro, name='registro'),
    path('servicios/', views.servicios, name='servicios'),
    path('sobrenosotros/', views.sobrenosotros, name='sobrenosotros'),
    path('tienda/', views.tienda, name='tienda'),
    path('logout/', views.cerrar, name="cerrar"),   
    
    
    
    path('detalle/<id>/', views.detalle, name="detalle"),
    path('modificar/<id>/', views.modificar, name="modificar"),
    path('eliminarProd/<id>/', views.eliminar, name="eliminarProd"),
    path('agregar/<id>', views.agregar_producto, name="agregar"),
    path('eliminar/<id>', views.eliminar_producto, name="eliminar"),
    path('restar/<id>', views.restar_producto, name="restar"),
    path('limpiar/', views.limpiar_carrito, name="limpiar"),
    path('generarBoleta/', views.generarBoleta,name="generarBoleta"),
]
