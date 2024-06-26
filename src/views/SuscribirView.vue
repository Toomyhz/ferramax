<template>
    <div class="container position-absolute top-50 start-50 translate-middle">
      <div class="form-container position-relative" id="form">
        <h2>Introduce tu gmail para ofertas únicas</h2>
        <form @submit.prevent="submitForm" method="post">
          <input v-model="form.email" placeholder="ejemplo@gmail.com" type="email" name="email" class="form-control " id="email-input" required>
          <button type="submit" class="btn btn-warning">Suscribete</button>
        </form>
      </div>
      <div class="text-container text-break">
        <h1 class="text-container-aviso">¡SUSCRÍBETE A FERRAMAX!</h1>
        <h4>
          Para esos clientes que quieren estar informados de todo lo que traiga Ferramax y sus descuentos únicos, ofrecemos la opción de suscripción, la cual no cuenta con costo alguno. Se te enviará de manera periódica información y descuentos únicos de nuestra compañía.
        </h4>
      </div>
    </div>
</template>
<script>
import axios from "axios";
import Swal from "sweetalert2";
  export default{
    data() {
      return{
        form:{
          email:''
        }
      };
    },
    methods:{
      async submitForm(){
        const response = await axios.post("http://127.0.0.1:5000/suscribe/",{
          email:this.form.email
        })
        var input = document.getElementById('email-input');
        if (response.data['email_valido']){
          input.classList.remove("is-invalid");
          Swal.fire({
                text:"Suscripción exitosa",
                width:"300px",
                position:"top",
                timer:2000,
                timerProgressBar:true,
                showConfirmButton:false,
                toast:true,
                icon:"success",
            });
        } else{
          input.classList.add("is-invalid");
          Swal.fire({
                text:response.data['error'],
                width:"300px",
                position:"top",
                timer:2000,
                timerProgressBar:true,
                showConfirmButton:false,
                toast:true,
                icon:"error",
            });
        }
      }
    }
  }
</script>  
<style>

.text-container{
    min-width: 200px;
    max-width: 700px;
}
.text-container> .text-container-aviso{
    background-color: #ffd333;
    margin-left: 10%;
    margin-right: 18%;
}
.container {
    display: flex;
    align-items: flex-start;
    gap: 20px; /* Espacio entre el formulario y el texto */
}
.form-container {
    border: 1px solid #ccc;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    min-width: 300px; /* Ancho mínimo */
    max-width: 600px; /* Ancho máximo */
    width: 100%;
    min-height: 250px;
    color: aliceblue;
    background-color:  rgb(37,37,46);
    position: relative;
}
button[type="submit"] {
    background-color: #ffd333;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    position: absolute;
    bottom: 20px;
    right: 20px;
}
button[type="submit"]:hover {
    background-color: rgb(161, 161, 45);
}
</style>