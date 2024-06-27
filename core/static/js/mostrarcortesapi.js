//implementación de Fetch para consumo de Api Rest

function mostrarCortes(){
    let url='http://localhost:3300/cortes';
    fetch(url)
    .then(response => response.json())
    .then(data => corteData(data))
    .catch(error => console.log(error))



    const corteData = (data) => {
        console.log(data)
        let body = ""

        for(i=0; i<data.length; i++)
        {
            body += `<tr>
                <td>${data[i].nombreCorte}</td>
                <td><img src="${staticUrl}${data[i].imagenCorte}" alt="${data[i].nombreCorte}" /></td>
                <td>${data[i].descripcionCorte}</td>
                </tr>`
        }//for 
        document.getElementById('cortes').innerHTML=body;

    }//mostrarData

}
