
/*PARA PREGUNTAR "ESTA SEGURO DE ELIMINAR Paciente?"*/
/*COn gentil auspicio de SWEET ALERT*/ 
function eliminarPaciente(id){
    Swal.fire({
        "title": "Esta seguro?",
        "text": "Esta acción no se puede deshacer",
        "icon": "question",
        "showCancelButton": true,
        "cancelButtonText": "No, Cancelar",
        "confirmButtonText": "Si, eliminar",
        "reverseButtons": true,
        "confirmButtonColor": "#dc3545"
    })

    .then(function(result){
         if(result.isConfirmed){
            window.location.href = "/eliminar-paciente/"+id+"/"
        }
    }) 
}
