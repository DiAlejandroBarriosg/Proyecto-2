/*<div class="col-lg-6">
<div class="card mb-4">
<iframe src="https://www.youtube.com/embed/rsTLyukvxGU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<div class="card-body">
<h5 class="card-title">Nombre publicación</h5>
<p class="card-text">Autor</p>
<p class="card-text">Categoria</p>
<a href="https://www.youtube.com/embed/rsTLyukvxGU" class="btn btn-primary">Ver video</a>
</div>
</div>
</div>*/

async function getPublicaciones(){

    const rawResponse = await fetch("http://localhost:4001/usuarios", {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })

    const response = await rawResponse.json()
    const arregloPublicaciones = response.data;
    console.log(arregloPublicaciones)

    let codigoHtml = ``

    for(let i=0; i<arregloPublicaciones.length; i++){
        codigoHtml += `\n<div class="col-lg-6">
        <div class="card mb-4">
        <iframe src="https://www.youtube.com/embed/2gO1v2GPMFk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        <div class="card-body">
        <h5 class="card-title">${arregloPublicaciones[i].correo}</h5>
        <p class="card-text">${arregloPublicaciones[i].nombre}</p>
        <p class="card-text">Categoria</p>
        <a href="https://www.youtube.com/embed/2gO1v2GPMFk" class="btn btn-primary">Ver video</a>
        </div>
        </div>
        </div>`
    }

    $('#publicaciones').append(codigoHtml)
}
