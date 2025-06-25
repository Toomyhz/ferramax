<template>
  <div class="register-view">
    <div class="container">
      <h1>Registro de usuario</h1>
      <form @submit.prevent="registrarUsuario">
        <fieldset>
          <label>Correo electrónico</label>
          <input type="email" v-model="email" required />
        </fieldset>

        <fieldset>
          <label>Contraseña</label>
          <input type="password" v-model="contrasena" required />
        </fieldset>

        <button type="submit" class="btn btn-primary">Registrarse</button>
        <p v-if="mensaje" :class="{ error: error, success: !error }">
          {{ mensaje }}
        </p>
      </form>

      <router-link to="/login">¿Ya tienes cuenta? Inicia sesión</router-link>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";

const email = ref("");
const contrasena = ref("");
const mensaje = ref("");
const error = ref(false);
const router = useRouter();

async function registrarUsuario() {
  try {
    const response = await axios.post("http://localhost:5000/users/register/", {
      email: email.value,
      contrasena: contrasena.value,
    });

    mensaje.value = "¡Registro exitoso! Puedes iniciar sesión.";
    error.value = false;

    // Redirigir luego de 2 segundos
    setTimeout(() => {
      router.push("/login");
    }, 2000);
  } catch (err) {
    mensaje.value = err.response?.data?.error || "Error al registrar";
    error.value = true;
  }
}
</script>

<style scoped>
.register-view {
  padding: 20px;
  max-width: 500px;
  margin: auto;
}
fieldset {
  display: flex;
  flex-direction: column;
  margin-bottom: 15px;
}
label {
  font-weight: bold;
  margin-bottom: 5px;
}
input {
  padding: 10px;
  font-size: 1em;
}
button {
  background-color: #ffd333;
  border: none;
  padding: 10px;
  cursor: pointer;
}
.error {
  color: red;
}
.success {
  color: green;
}
</style>
