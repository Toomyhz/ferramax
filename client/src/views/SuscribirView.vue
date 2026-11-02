<template>
  <div class="suscribe-wrapper">
    <div class="form-container" id="form">
      <h2>Introduce tu correo para ofertas únicas</h2>

      <form @submit.prevent="submitForm" method="post">
        <input
          v-model="form.email"
          type="email"
          placeholder="ejemplo@gmail.com"
          name="email"
          class="form-control"
          id="email-input"
          required
        />
        <button type="submit" class="btn btn-warning">Suscribete</button>
      </form>
    </div>

    <div class="text-container">
      <h1 class="text-banner">¡SUSCRÍBETE A FERRAMAX!</h1>
      <p class="fs-5">
        Para esos clientes que quieren estar informados de todo lo que traiga
        Ferramax y sus descuentos únicos, ofrecemos la opción de suscripción, la
        cual no cuenta con costo alguno. Se te enviará de manera periódica
        información y descuentos únicos de nuestra compañía.
      </p>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Swal from "sweetalert2";

export default {
  data() {
    return {
      form: {
        email: "",
      },
    };
  },
  methods: {
    async submitForm() {
      const response = await axios.post("http://127.0.0.1:5000/suscribe/", {
        email: this.form.email,
      });
      var input = document.getElementById("email-input");
      if (response.data["email_valido"]) {
        input.classList.remove("is-invalid");
        Swal.fire({
          text: "Suscripción exitosa",
          width: "300px",
          position: "top",
          timer: 2000,
          timerProgressBar: true,
          showConfirmButton: false,
          toast: true,
          icon: "success",
        });
      } else {
        input.classList.add("is-invalid");
        Swal.fire({
          text: response.data["error"],
          width: "300px",
          position: "top",
          timer: 2000,
          timerProgressBar: true,
          showConfirmButton: false,
          toast: true,
          icon: "error",
        });
      }
    },
  },
};
</script>
<style scoped>
.suscribe-wrapper {
  min-height: 10vh;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 40px;
  padding: 24px;
  flex-wrap: wrap;
}

.form-container {
  background: #25252e;
  color: #fff;
  padding: 24px 32px 64px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.15);
  width: 320px;
  max-width: 100%;
  position: relative;
}

.form-title {
  margin-bottom: 16px;
  font-size: 1.25rem;
  text-align: center;
}

.btn-suscribe {
  background: #ffd333;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  position: absolute;
  right: 20px;
  bottom: 20px;
  transition: background 0.25s;
}

.btn-suscribe:hover {
  background: #e6c32f;
}
.btn-suscribe:active {
  background: #d4b52a;
}

.text-container {
  max-width: 500px;
  min-width: 250px;
}

.text-banner {
  background: #ffd333;
  padding: 4px 8px;
  font-size: 1.4rem;
  margin-bottom: 12px;
  text-align: center;
}
</style>
