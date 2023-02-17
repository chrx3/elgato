let url = 'http://34.176.203.109:8000/Usuario/'

localStorage.setItem('login','false');
const usernameinput = document.getElementById("Username");
const passwordinput = document.getElementById("Password");
const boton = document.getElementById("boton");
const estado = localStorage.getItem('login');

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
                localStorage.setItem('login','true');
                window.location.href = 'gatito.html';
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