<template>
  <div class="product-grid">
    <div class="product-card" v-for="producto in productos" :key="producto.ID_HERRAMIENTA">
        <h3>{{ producto.NOMBRE }}</h3>
        <img
          :src="producto.IMAGEN"
          alt="Imagen del Producto"
          class="product-img"
        />
        <p>{{ producto.CATEGORIA }}</p>
        <p v-if="moneda == 'USD'">USD $ {{ producto.VALOR_EN_DOLARES }}</p>
        <p v-if="moneda == 'CLP'">CLP ${{ producto.VALOR }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProductList",
  props: {
    productos: {
      type: Array,
      required: true,
    },
    moneda:{
      type:String
    }
  },
};
</script>

<style scoped>
.product-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  padding: 16px;
}

.product-card {
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  text-align: center;
  transition: box-shadow 0.3s ease-in-out;
}

.product-card:hover {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.product-img {
  width: 100%;
  height: auto;
}

.product-card h3 {
  margin: 16px 0 8px;
  font-size: 1.2em;
}

.product-card p {
  margin: 4px 0;
  color: #555;
}

.product-card p:last-of-type {
  font-weight: bold;
  color: #000;
}
</style>
