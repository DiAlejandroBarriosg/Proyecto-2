const txtCorreo = document.getElementById('txtCorreo')
const txtPassword = document.getElementById('txtPassword')
const textGenero = document.getElementById('textGenero')
const textNombreUsuario = document.getElementById('textNombreUsuario')
const txtNombre = document.getElementById('txtNombre')

async function crear(){
    // value: Retorna el valor asociado a la etiqueta
    let correo = document.getElementById("correo").value
    let password = document.getElementById("password").value
    let nombre = document.getElementById("nombre").value
    let genero = document.getElementById("genero").value
    let nombreusuario = document.getElementById("nombre_usuario").value


    /* 
        await: es un operador que "espera" por una Promise.
        Promise: es un valor que puede tardar un cierto tiempo en computarse.
        fetch: forma nativa de JavaScript de poder realizar peticiones http, esta puede tener
        varios parametros asociados 
            -> method: tipo de metodo de la peticion http, si se omite por defecto es get
            -> headers: estos son regularmente asociados con el tiepo de body que se esta enviando
            -> body: cuerpo de la peticion
        
        JSON.stringify: convierte el objeto JSON en una notación de texto para su transmision en
        la web
    */
    let peticion = await fetch("http://localhost:4001/usuario", {
        method: "put",
        headers: {"Content-Type": 'application/json'},
        body: JSON.stringify({
            correo: correo,
            password: password,
            nombre: nombre,
            Genero: genero,
            Nombre_usuario: nombreusuario
        })
    })
    let respuesta = await peticion.json()
    alert(respuesta.mensaje)

    document.getElementById("correo").value = ""
    document.getElementById("password").value = ""
    document.getElementById("nombre").value = ""
    document.getElementById("genero").value = ""
    document.getElementById("nombre_usuario").value = ""

}
