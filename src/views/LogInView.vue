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
  display: block;
  margin: 0;
  padding: 0%;
  width: 100%;
  flex-direction: column;
  align-items: center;
}
h1 {
  font-size: 2em;
  color: #333;
  text-align: left;
  margin: 20px 0;
}
.login-container {
  display: flex;
  width: 100%;
  flex-direction: row;
  justify-content: space-between;
  text-align: center;
}
.section {
  display: flex;
  padding: 20px;
  flex-direction: column;
  width: 47%;
}
.login-data {
  border: 1px solid rgba(37, 37, 46, 0.34);
  border-radius: 5px;
  text-align: center;
}
.register {
  height: 220px;
  border-radius: 5px;
  background-color: rgb(37, 37, 46);
  text-align: center;
  box-shadow: #333 0px 0px wspx;
  color: white;
}
.block-title {
  font-size: 1.5em;
  margin-bottom: 10px;
}
.btn-register {
  width: 40%;
  color: white;
  border: 1px solid #ffd333;
  align-self: center;
}
.btn-register:hover {
  background-color: #ffd333;
  color: black;
  transition: all 0.3s ease-in-out;
}
.checkbox-fieldset {
  display: flex;
  justify-content: start;
  align-items: center;
  text-align: center;
}
.checkbox-fieldset input[type="checkbox"] {
  margin-right: 10px;
}
.checkbox-fieldset label {
  margin: 0;
  font-size: 0.9em;
  color: #333;
  align-self: center;
  text-align: center;
}
</style>
