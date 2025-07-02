<template>
  <div class="store-view">
    <div class="container">
      <h1 v-if="text">Resultados de: {{ text }}</h1>
      <h1 v-else-if="categoria">Productos en la Categoría: {{ categoria }}</h1>
      <h1 v-else-if="brandId">Productos de la Marca: {{ brandId }}</h1>
      <h1 v-else>Productos</h1>
      <ProductList
        :productos="productosFiltrados"
        :moneda="moneda"
        @agregarCarrito="agregarAlCarrito"
      />
    </div>
  </div>
</template>

<script>
import { getTools } from "@/api/tools";
import ProductList from "@/components/ProductList.vue";
import { mapActions, mapGetters } from "vuex";

export default {
  components: {
    ProductList,
  },
  props: {
    moneda: {
      type: String,
    },
  },
  data() {
    return {
      tools: [],
      categoria: "",
      text: "",
      brandId: null,
    };
  },
  computed: {
    productosFiltrados() {
      if (this.brandId) {
        return this.tools.filter((tool) => tool.ID_MARCA == this.brandId);
      } else if (this.categoria) {
        return this.tools.filter((tool) => tool.CATEGORIA === this.categoria);
      } else if (this.text) {
        return this.tools.filter((tool) =>
          tool.NOMBRE.toUpperCase().includes(this.text.toUpperCase())
        );
      } else {
        return this.tools;
      }
    },
    ...mapGetters(["carrito"]),
  },
  watch: {
    "$route.query": {
      handler() {
        this.categoria = this.$route.query.categoria;
        this.text = this.$route.query.text;
        this.brandId = this.$route.query.brands;
      },
      immediate: true,
    },
  },
  created() {
    this.fetchData();
    this.categoria = this.$route.query.categoria;
    this.text = this.$route.query.text;
    this.brandId = this.$route.query.brands;
  },
  methods: {
    async fetchData() {
      try {
        this.tools = await getTools();
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    },
    ...mapActions(["agregarAlCarrito"]),
  },
};
</script>

<style scoped>
.store-view {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  background: linear-gradient(to right, #fdfbfb, #ebedee);
  min-height: 100vh;
  padding-top: 40px;
}

.container {
  font-weight: bold;
  color: #333;
  width: 90%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  background-color: #ffffff;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
  border-radius: 12px;
}

h1 {
  font-size: 1.8em;
  color: #2c3e50;
  margin-bottom: 24px;
  padding-bottom: 10px;
  border-bottom: 2px solid #e0e0e0;
  text-align: center;
  font-weight: 600;
  letter-spacing: 0.5px;
}
</style>
