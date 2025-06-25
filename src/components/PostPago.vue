<template>
  <div class="postpago">
    <div v-if="estado === 'cargando'">⏳ Confirmando pago...</div>
    <div v-else-if="estado === 'exito'">
      <h2>✅ ¡Pago exitoso!</h2>
      <p>Gracias por tu compra. Número de orden: {{ orden }}</p>
      <router-link to="/">Volver al inicio</router-link>
    </div>
    <div v-else-if="estado === 'fallo'">
      <h2>❌ Pago fallido</h2>
      <p>No pudimos procesar tu pago. Intenta nuevamente o contáctanos.</p>
      <router-link to="/cart">Volver al carrito</router-link>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      estado: 'cargando',
      orden: null,
    };
  },
  async mounted() {
    const params = new URLSearchParams(window.location.search);
    const token = params.get("token_ws");

    if (!token) {
      this.estado = 'fallo';
      return;
    }

    try {
      const response = await fetch("http://localhost:5000/api/transaction_return/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ token_ws: token }),
      });
      const data = await response.json();

      if (data.status === "AUTHORIZED") {
        this.orden = data.buy_order;
        this.estado = 'exito';
        this.$store.dispatch("vaciarCarrito");
      } else {
        this.estado = 'fallo';
      }
    } catch (error) {
      this.estado = 'fallo';
    }
  },
};
</script>
