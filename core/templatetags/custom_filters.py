#Este archivo lo que realiza es cambiar el formato de numeros a miles y millones, el cual se utiliza en la vista de la tienda
#para mostrar el precio de los productos, en este caso se utiliza para cambiar el formato de los precios de los productos
#Igualmente en settings.py se agrego el codigo de THOUSAND_SEPARATOR = '.' para que el separador de miles sea un punto
from django import template
from django.conf import settings

register = template.Library()

@register.filter
def format_price(value):
    return f"{value:,.0f}".replace(',', settings.THOUSAND_SEPARATOR) # Cambio de coma por punto