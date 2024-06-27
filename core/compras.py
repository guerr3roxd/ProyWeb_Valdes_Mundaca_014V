
class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito=carrito 
    
    def agregar(self, producto):
        if producto.idProducto not in self.carrito.keys():
            if producto.stock > 0:
                self.carrito[producto.idProducto] = {
                    "producto_id": producto.idProducto,
                    "nombre": producto.nombreProducto,
                    "marca": producto.marca,
                    "modelo": producto.modelo,
                    "stock": producto.stock,
                    "precio": str(producto.precio),
                    "cantidad": 1,
                    "subtotal": producto.precio
                }
                producto.stock -= 1
                producto.save()
            else:
                return "No hay suficiente stock"
        else:
            if producto.stock > 0:
                item = self.carrito[producto.idProducto]
                item["cantidad"] += 1
                item["subtotal"] += producto.precio
                producto.stock -= 1
                producto.save()
            else:
                return "No hay suficiente stock"
        self.guardar_carrito()
        return "Producto agregado exitosamente"




    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified=True

    def eliminar(self, producto):
        id = producto.idProducto
        if id in self.carrito: 
            del self.carrito[id]
            self.guardar_carrito()
    
    def restar(self, producto):
        for key, value in self.carrito.items():
            if key == str(producto.idProducto):
                if value["cantidad"] > 1:
                    value["cantidad"] -= 1
                    value["subtotal"] -= producto.precio
                    producto.stock += 1
                    producto.save()
                else:
                    del self.carrito[key]
                break
        self.guardar_carrito()
     
    def limpiar(self):
        self.session["carrito"]={}
        self.session.modified=True 
        
    def total(self):
        total = 0
        for key, value in self.carrito.items():
            precio = value['precio'].replace('CLP', '').strip()
            total += int(precio) * value['cantidad']
        return total

        
