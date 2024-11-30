const apiUrl="http://127.0.0.1:8000/"




const createUser=async(evento)=>{
    evento.preventDefault()


    const firstName=document.getElementById("first-name").value
    const lastName=document.getElementById("last-name").value
    const dateOfBirth=document.getElementById("date-of-birth").value
    const response=await fetch(`${apiUrl}/users/new-user/`,{
        method: "POST",headers: {"Content-Type":"application/json"},
        body: JSON.stringify({first_name:firstName, last_name:lastName,date_of_birth:dateOfBirth})
    })
    if(response.ok){
        alert("Usuário criado com sucesso");
        //carregarUsuarios() Função carregar usuários


    }
}

const carregarUsuarios=async()=>{

    const response=await fetch(`${apiUrl}/users/`)
    const users=await response.json()
    console.log(users)
    const userList = document.getElementById("user-list")
    console.log(userList)
    userList.innerHTML=""
    console.log(users)
    users.forEach(user => {
        const userItem =document.createElement("li")
        userItem.textContent=`Olá ${user.first_name}`
        
        userList.appendChild(userItem)
        //criar tabela dinamica aqui, colocar demais itens
        
    });
}

carregarUsuarios()


