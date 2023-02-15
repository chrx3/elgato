let url = 'http://10.0.1.45:8000/usuario'


const obtenerUsuarios = async() =>{    
    try{
        const respuesta = await axios.get(url)

        console.log(respuesta.data);

    }catch(error){
        console.log(error);
    }
    
}

// axios.get(url)
// .then((res)=>{
//     var datos = res.data
//     var objetivo = document.getElementById('username');
//     for( i = 0; i < datos.length; i++){
//         objetivo.innerHTML = JSON.stringify(datos[i]['Username']); 

//     }
    
// }).catch((error)=>{
//     console.log(error)
// })

const usernameinput = document.getElementById("Username");
const passwordinput = document.getElementById("Password");
const boton = document.getElementById("boton");

//login
boton.addEventListener("click",(e)=>{
    const username = usernameinput.value;
    const password = passwordinput.value;

    axios.get(url,{


    })
    .then((res) =>{
        if( username == '' || password==''){
            e.preventDefault();
            alert('rellene los campos')
        }else{
            if(username == res.data[0]['Username'] && password == res.data[0]['Password']){
                alert('ingresado')  
            }else{
                e.preventDefault();
                alert('usuario o contraseña incorrecto')
            }
        }
        
    })
    .catch((error)=>{
        console.log(error)
    })
    
})





