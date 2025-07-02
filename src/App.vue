<script setup>
import { RouterView } from "vue-router";
import MyNavbar from "./components/MyNavbar.vue";
</script>
<script>
export default {
  data() {
    return {
      moneda: "USD",
    };
  },
  methods: {
    cambiarMoneda(moneda) {
      this.moneda = moneda;
    },
  },
};
</script>

<template>
  <div class="layout">
    <MyNavbar :cambioActual="moneda" @cambiarMoneda="cambiarMoneda" />
    <main class="contenido">
      <RouterView :moneda="moneda" style="height: 100%" />
    </main>
  </div>
</template>
<style scoped>
.layout {
  display: flex;
  flex-direction: column;
  height: 100vh; /* Toda la altura de la pantalla */
}

main.contenido {
  flex: 1; /* Ocupa todo el espacio disponible */
  overflow-y: auto;
  padding: 1rem; /* Opcional */
  background-color: #f4f4f4;
}
</style>
