def total_carrito(request):
    total = 0
    if 'carrito' in request.session:
        for key, value in request.session['carrito'].items():
            precio = value['precio'].replace('CLP', '').strip()
            total += int(precio) * value['cantidad']
    return {'total_carrito': total}