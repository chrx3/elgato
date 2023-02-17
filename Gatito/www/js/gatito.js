url = 'http://34.176.203.109:8000/Photos/download_MqFUNMy.jpg'

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



