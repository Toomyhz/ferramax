<template>
  <div class="login-view">
    <div class="container">
      <h1>Inicio de sesión</h1>
      <form @submit="login">
        <fieldset>
          <label>Correo electrónico</label>
          <input
            v-model="email"
            type="email"
            placeholder="Correo electrónico"
            required
          />
        </fieldset>
        <fieldset>
          <label>Contraseña</label>
          <input
            v-model="contrasena"
            id="password-field"
            type="password"
            placeholder="Contraseña"
            required
          />
        </fieldset>

        <fieldset class="checkbox-fieldset">
          <input type="checkbox" id="show-password" @change="showPassword" />
          <label for="show-password">Mostrar contraseña</label>
        </fieldset>
        <fieldset>
          <button type="submit" class="btn btn-warning">Iniciar sesión</button>
        </fieldset>
      </form>
      <router-link to="/register">Crea tu cuenta aquí</router-link>
    </div>
  </div>
</template>
<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";
import { useStore } from "vuex";
import Swal from "sweetalert2";

const store = useStore();
const email = ref("");
const contrasena = ref("");
const router = useRouter();

function showPassword() {
  const checkbox = document.getElementById("show-password");
  const passwordField = document.getElementById("password-field");
  passwordField.type = checkbox.checked ? "text" : "password";
}

async function login(e) {
  e.preventDefault(); // Evita que se recargue la página

  try {
    const response = await axios.post("http://localhost:5000/users/login/", {
      email: email.value,
      contrasena: contrasena.value,
    });

    const { token, email: correo, user_id } = response.data;

    // ✅ Notificar al store (esto sí activa la reactividad)
    store.commit("setUser", {
      token,
      email: correo,
      user_id,
    });

    Swal.fire({
      icon: "success",
      title: "¡Bienvenido!",
      text: `Has iniciado sesión como ${correo}`,
      timer: 2000,
      showConfirmButton: false,
      toast: true,
      position: "top-end",
    });

    // ✅ Redirigir (esto ayuda a que la navbar se reevalúe también)
    router.push({ name: "home" });
  } catch (err) {
    Swal.fire({
      icon: "error",
      title: "Error de inicio de sesión",
      text: "Correo o contraseña inválidos.",
      timer: 2000,
      showConfirmButton: false,
      toast: true,
      position: "top",
    });
    console.error("Error de login", err);
  }
}
</script>

<style scoped>
.login-view {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f4f4f4;
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
.checkbox-fieldset {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
</style>
