
/*PARA PREGUNTAR "ESTA SEGURO DE ACTUALIZAR PACIENTE?"*/
/* AUSPICIO DE SWEET ALERT*/
function actualizarPaciente(){
    Swal.fire({
        "title": "Esta seguro?",
        "text": "Esta acción no se puede deshacer",
        "icon": "question",
        "showCancelButton": true,
        "cancelButtonText": "No, Cancelar",
        "confirmButtonText": "Si, Actualizar",
        "reverseButtons": true,
        "confirmButtonColor": "#dc3545"
    })

    .then(function(result){
         if(result.isConfirmed){
            window.location.href = "/actualizar-paciente/<id>/"
        }
    }) 
}

/*"/actualizar-paciente/"+id+"/"*/