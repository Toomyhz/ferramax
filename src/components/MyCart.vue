<template>
  <div>
    <h2>Carrito de Compras</h2>
    <div v-if="carrito.length === 0">El carrito está vacío.</div>
    <ul v-else>
      <li v-for="producto in carrito" :key="producto.ID_HERRAMIENTA">
        <img
          :src="producto.IMAGEN"
          alt="Imagen del producto"
          class="producto-imagen"
        />
        <div class="producto-info">
          <span class="producto-nombre">{{ producto.NOMBRE }}</span>

          <span class="producto-precio" v-if="props.moneda == 'CLP'">{{
            formatearPrecio(producto.VALOR * producto.cantidad)
          }}</span>
          <span class="producto-precio" v-if="moneda == 'USD'"
            >${{
              Math.round(producto.VALOR_EN_DOLARES * producto.cantidad * 100) /
              100
            }}</span
          >
        </div>
        <div class="botones">
          <span class="cantidad">{{ producto.cantidad }} unidades</span>
          <button
            @click="borrarItems(producto.ID_HERRAMIENTA)"
            class="botones-manejo"
          >
            -
          </button>
          <button @click="removerDelCarrito(producto.ID_HERRAMIENTA)">
            Remover
          </button>
          <button @click="agregarProducto(producto)" class="botones-manejo">
            +
          </button>
        </div>
      </li>
    </ul>
    <div v-if="carrito.length > 0" class="total-carrito">
      <span v-if="moneda == 'CLP'"
        >Total: CLP $ {{ formatearPrecio(totalCarrito) }}</span
      >
      <span v-if="moneda == 'USD'"
        >Total: USD $ {{ Math.round(totalCarritoDolares * 100) / 100 }}</span
      >
    </div>
    <button v-if="carrito.length > 0" @click="vaciarCarrito">
      Vaciar Carrito
    </button>
    <PagoTransbank v-if="carrito.length > 0">Pagar</PagoTransbank>
  </div>
</template>
<script setup>
import { defineProps, computed } from "vue";
import PagoTransbank from "./PagoTransbank.vue";
import { useStore } from "vuex";
const store = useStore();
const props = defineProps({
  moneda: {
    type: String,
  },
});

const carrito = computed(() => store.getters.carrito);
const totalCarrito = computed(() => store.getters.totalCarrito);
const totalCarritoDolares = computed(() => store.getters.totalCarritoDolares);
const formatearPrecio = computed(() => store.getters.formatearPrecio);

function borrarItems(productoId) {
  store.dispatch("borrarItems", productoId);
}
function removerDelCarrito(productoId) {
  store.dispatch("removerDelCarrito", productoId);
}
function vaciarCarrito() {
  store.dispatch("vaciarCarrito");
}
function agregarProducto(producto) {
  store.dispatch("agregarAlCarrito", producto);
}
</script>

<style scoped>
div {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  border-radius: 5px;
  background-color: #f9f9f9;
}

h2 {
  text-align: center;
  color: #333;
  font-family: "Arial", sans-serif;
  margin-bottom: 20px;
}

div[v-if="carrito.length === 0"] {
  text-align: center;
  font-size: 1.2em;
  color: #777;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: flex;
  align-items: center;
  padding: 10px;
  border-bottom: 1px solid #ddd;
}

li:last-child {
  border-bottom: none;
}

.producto-imagen {
  width: 50px;
  height: 50px;
  object-fit: cover;
  margin-right: 10px;
}

.producto-info {
  flex: 1;
  font-size: 1em;
  color: #333;
  display: flex;
  flex-direction: column;
}

.producto-nombre {
  font-weight: bold;
  margin-bottom: 5px;
}

.producto-precio {
  font-size: 0.9em;
  color: #777;
}

.botones {
  display: flex;
  align-items: center;
  gap: 10px;
}

.cantidad {
  margin-right: 10px;
  font-size: 0.9em;
  color: #777;
}

button {
  background-color: rgb(37, 37, 46);
  color: white;
  border: none;
  border-radius: 3px;
  padding: 5px 10px;
  cursor: pointer;
  transition:
    background-color 0.3s,
    color 0.3s;
  font-size: 0.9em;
  min-width: 80px;
  text-align: center;
}

.botones-manejo {
  padding: 4px 7px;
  min-width: 30px;
  min-height: 31px;
  font-size: 0.9em;
}

button:hover {
  background-color: #ffd333;
  color: rgb(37, 37, 46);
}

button:focus {
  outline: none;
}

button[v-if="carrito.length > 0"] {
  display: block;
  width: 100%;
  margin-top: 20px;
  background-color: #3498db;
}

button[v-if="carrito.length > 0"]:hover {
  background-color: #2980b9;
}

.total-carrito {
  text-align: right;
  font-size: 1.2em;
  font-weight: bold;
  margin-top: 20px;
  color: #333;
}
</style>
