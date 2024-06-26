<template>
  <div>
    <button @click="iniciarPago">Pagar</button>
  </div>
</template>

<script>
export default {
  methods: {
    iniciarPago() {
      this.$store.dispatch("iniciarPago")
    },
  },
};
</script>

<style scoped>
button {
  background-color: #3498db;
  color: white;
  border: none;
  border-radius: 3px;
  padding: 10px 20px;
  cursor: pointer;
  font-size: 1em;
}

button:hover {
  background-color: #2980b9;
}
</style>
