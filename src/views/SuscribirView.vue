<template>
    <div class="container position-absolute top-50 start-50 translate-middle">
      <div class="form-container position-relative" id="form">
        <h2>Introduce tu gmail para ofertas únicas</h2>
        <form @submit.prevent="submitForm">
          <input 
            placeholder="ejemplo@gmail.com" 
            type="email" 
            v-model="email" 
            required 
            pattern="[a-zA-Z0-9._%+-]+@gmail\.com" 
            title="Por favor, introduce un correo de Gmail válido.">
          <input class="" type="submit" value="Enviar">
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
input[type="email"] {
    width: 100%;
    padding: 10px;
    margin: 10px 0;
    border: 1px solid #ccc;
    border-radius: 5px;
}
input[type="submit"] {
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
input[type="submit"]:hover {
    background-color: rgb(161, 161, 45);
}
</style>