$(function(){
    $.validator.addMethod("lettersOnly", function(value, element) {
        return this.optional(element) || /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$/.test(value);
    }, "Solo se permiten letras");

    $("#datos-cli").validate({
        rules:{
            nom:{
                required:true,
                lettersOnly: true
            },
            ape:{
                required:true,
                lettersOnly: true
            },
            correo:{
                required:true,
                email:true
            },
            telefono:{
                required:true,
                number:true
            },
            fecha:{
                required:true
            }
        },
        messages:{
            nom:{
                required:'Ingrese su nombre',
                lettersOnly: 'Solo se permiten letras',
                minlength:'Caracteres insuficientes..'
            },
            ape:{
                required:'Ingrese su apellido',
                lettersOnly: 'Solo se permiten letras',
                minlength:'Caracteres insuficientes..'
            },
            correo:{
                required:'Ingrese su correo electrónico',
                minlength:'Formato de correo inválido..'
            },
            telefono:{
                required:'Ingrese su número de teléfono',
                number:'Teléfono inválido',
                minlength:'Digitos insuficientes',
                maxlength:'Teléfono inválido'
            },
            fecha:{
                required:'Seleccione su fecha',
                min:'Fecha de ingreso no válida'
            }
        }
    });
});

function setMinMaxDate() {
    let today = new Date();
    let minDate = new Date();
    minDate.setDate(today.getDate());  // mínimo 1 semana desde hoy
    let maxDate = new Date(minDate);
    maxDate.setMonth(maxDate.getMonth() + 3);  // máximo 3 meses después del mínimo

    let minDateStr = minDate.toISOString().split('T')[0];
    let maxDateStr = maxDate.toISOString().split('T')[0];

    let fechaInput = document.getElementById('fecha');
    fechaInput.setAttribute('min', minDateStr);
    fechaInput.setAttribute('max', maxDateStr);
}


document.addEventListener('DOMContentLoaded', (event) => {
    setMinMaxDate();
});