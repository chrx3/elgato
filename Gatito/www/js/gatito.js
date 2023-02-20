url = 'http://34.176.38.39:8000/Photos/DALLE_2023-02-20_09.28.58_-_A_cata_sitting_on_a_chair.png'

const estado = localStorage.getItem('login')
if(estado == 'false'){
    const gano = document.createElement("h1");
    gano.innerText = 'Eso no se hace!';
    document.getElementById('gano').appendChild(gano);
    alert('pa` juera')
    alert('XD')
    window.location.replace('https://www.youtube.com/watch?v=dQw4w9WgXcQ');
}else{
    var config = { responseType: 'blob'}
    axios.get(url, config)
    .then(res =>{
    $("#img1").attr("src",window.URL.createObjectURL(res.data));
    const gano = document.createElement("h1");
    gano.innerText = 'Ganaste!';
    document.getElementById('gano').appendChild(gano);
    })
}



