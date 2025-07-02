<template>
  <div class="login-view">
    <div class="container-xl">
      <h1>Inicio de sesión</h1>
      <div class="login-container">
        <div class="section login-data">
          <strong class="block-title">Clientes registrados</strong>
          <div>
            <p>
              Si ya tienes una cuenta, inicia sesión para acceder a tus datos y
              realizar compras de manera rápida y sencilla.
            </p>
            <form @submit="login">
              <fieldset>
                <strong>Correo electrónico</strong>
                <input
                  v-model="email"
                  type="email"
                  placeholder="Correo electrónico"
                  class="form-control"
                  required
                />
              </fieldset>

              <fieldset>
                <strong>Contraseña</strong>
                <input
                  v-model="contrasena"
                  id="password-field"
                  type="password"
                  placeholder="Contraseña"
                  class="form-control"
                  required
                />
              </fieldset>

              <fieldset class="checkbox-fieldset">
                <input
                  type="checkbox"
                  id="show-password"
                  @change="showPassword"
                />
                <label for="show-password">Mostrar contraseña</label>
              </fieldset>
              <fieldset>
                <button type="submit" class="btn btn-warning">
                  Iniciar sesión
                </button>
              </fieldset>
            </form>
          </div>
        </div>
        <div class="section register">
          <strong class="block-title">Clientes nuevos</strong>
          <p>
            Para disfrutar de todos los beneficios de Ferramax, como descuentos
            exclusivos y acceso a productos únicos, regístrate ahora.
          </p>
          <RouterLink :to="{ name: 'register' }" class="btn btn-register"
            >Registrarse</RouterLink
          >
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";

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

    // Guardar token y datos en localStorage
    localStorage.setItem("token", token);
    localStorage.setItem("email", correo);
    localStorage.setItem("user_id", user_id);

    // Redirigir
    router.push("/");
  } catch (err) {
    alert("Correo o contraseña inválidos.");
    console.error("Error de login", err);
  }
}
</script>

<style scoped>
.login-view {
  display: flex;
  justify-content: center;
  padding: 3rem 1rem;
  background-color: #f4f4f4;
  min-height: 100vh;
  font-family: "Segoe UI", sans-serif;
}

.container-xl {
  max-width: 900px;
  width: 100%;
  background-color: white;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

h1 {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 2rem;
  color: #2c3e50;
  text-align: center;
}

.login-container {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 2rem;
}

.section {
  flex: 1;
  min-width: 300px;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.block-title {
  font-size: 18px;
  font-weight: bold;
  color: #333;
  margin-bottom: 0.5rem;
}

.login-data {
  border: 1px solid #ddd;
  padding: 1.5rem;
  border-radius: 8px;
  background-color: #fafafa;
}

.login-data p {
  font-size: 14px;
  color: #555;
}

.register {
  background-color: #25252e;
  color: white;
  padding: 1.5rem;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.register p {
  font-size: 14px;
  color: #ccc;
  margin: 1rem 0;
}

form fieldset {
  display: flex;
  flex-direction: column;
  gap: 0.3rem;
  margin-bottom: 1rem;
}

form strong {
  font-size: 14px;
  color: #333;
}

.form-control {
  padding: 0.5rem 0.75rem;
  font-size: 14px;
  border: 1px solid #ccc;
  border-radius: 6px;
  outline: none;
  transition: border-color 0.3s;
}

.form-control:focus {
  border-color: #3498db;
}

.checkbox-fieldset {
  display: flex;
  align-items: center;
  font-size: 13px;
  gap: 0.5rem;
  margin-top: -0.5rem;
}

.btn {
  padding: 0.6rem 1.2rem;
  font-weight: 600;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
}

.btn-warning {
  background-color: #f1c40f;
  color: #2c3e50;
}

.btn-warning:hover {
  background-color: #e1b70f;
}

.btn-register {
  background-color: transparent;
  color: white;
  border: 1px solid #ffd333;
  align-self: flex-start;
  padding: 0.6rem 1.2rem;
  font-weight: bold;
  border-radius: 6px;
  transition: all 0.3s ease-in-out;
  text-align: center;
}

.btn-register:hover {
  background-color: #ffd333;
  color: black;
}
</style>
