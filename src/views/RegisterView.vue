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
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f4f4f4;
  min-height: 90vh;
  padding: 0 1rem;
  font-family: "Segoe UI", sans-serif;
}

.container {
  width: 100%;
  max-width: 500px;
  background-color: white;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

h1 {
  font-size: 24px;
  font-weight: bold;
  color: #2c3e50;
  text-align: center;
  margin-bottom: 1.5rem;
}

form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

fieldset {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}

label {
  font-weight: 600;
  font-size: 14px;
  color: #333;
}

input {
  padding: 0.6rem 0.75rem;
  font-size: 14px;
  border-radius: 6px;
  border: 1px solid #ccc;
  outline: none;
  transition: border-color 0.3s;
}

input:focus {
  border-color: #3498db;
}

.btn {
  padding: 0.7rem 1.2rem;
  font-weight: bold;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.3s ease;
}

.btn-primary {
  background-color: #ffd333;
  color: #2c3e50;
}

.btn-primary:hover {
  background-color: #f1c40f;
}

.error,
.success {
  margin-top: 0.5rem;
  font-size: 14px;
  font-weight: 500;
}

.error {
  color: #e74c3c;
}

.success {
  color: #27ae60;
}

a {
  display: block;
  margin-top: 1.5rem;
  text-align: center;
  color: #3498db;
  text-decoration: none;
  font-size: 14px;
}

a:hover {
  text-decoration: underline;
}
</style>
