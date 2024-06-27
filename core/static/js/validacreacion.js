
$(function(){ 
    $("#formulario").validate({ 
        rules:{
            idProducto: "required",
            nombreProducto:"required",
            marca: "required",
            modelo: "required",
            precio:"required",
            descripcion: "required",
            stock:"required",
            imagen: "required",
            categoria: "required",
        },
        messages:{
            idProducto:{
                required: "Ingrese el SKU del Producto"
            },
            nombreProducto:{
                required: "Ingrese el Nombre del producto"
            },
            marca:{
                required: "Ingrese la Marca del producto"
            },
            modelo:{
                required: "Ingrese el Modelo del producto"
            },
            precio: {
                required: "Ingrese el Precio del producto"
            },
            descripcion:{
                required: "Ingrese la Descripción del producto"
            },
            stock:{
                required: "Ingrese el Stock del producto"
            },
            imagen:{
                required: "Ingrese la Imagen del producto"
            },
            categoria:{
                required: "Ingrese la Categoria del producto"
            }
        }
    });
});
