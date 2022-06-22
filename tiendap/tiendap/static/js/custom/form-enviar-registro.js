function enviar(){

  
    let  nombres = document.getElementById("txt-nombres").value;
    let  apellidoPaterno = document.getElementById("txt-apellido-paterno").value;
    let  apellidoMaterno = document.getElementById("txt-apellido-materno").value;
    let  email = document.getElementById("txt-email").value;
   
    
    if(isEmpty(nombres) &&  isEmpty(apellidoPaterno) && 
    isEmpty(apellidoMaterno) &&isEmpty(email) 
    ){
        console.log('formulario completamente lleno');
        let etiqueta =  document.getElementById("txt-message");
        console.log(etiqueta);
        etiqueta.innerHTML = '<div style="margin-top:25px;" class="alert alert-success alert-dismissible fade show" role="alert">'+
                'Formulario enviado con éxito' +
                //'<button type="button" class="close" data-dismiss="alert" aria-label="Close">' +
                //'<span aria-hidden="true">\&times;</span></button>'
                '</div>';
        document.getElementById('frm-contacto').submit();
    }else{
        console.log('formulario con campos vacios');
        let etiqueta =  document.getElementById("txt-message");
        etiqueta.innerHTML = '<div style="margin-top:25px;" class="alert alert-danger alert-dismissible fade show" role="alert">'+
                'Error debe ingresar todos los campos' +
                //'<button type="button" class="close" data-dismiss="alert" aria-label="Close">' +
                //'<span aria-hidden="true">\&times;</span></button>'
                '</div>';       
    }
}

function isEmpty(element){
    if(element !== undefined && element !== '' ){
        return true;
    }else{
        return false;
    }
}