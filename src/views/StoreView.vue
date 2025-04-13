<template>
  <div class="store-view">
    <div class="container">
      <h1 v-if="text">Resultados de: {{ text }}</h1>
      <h1 v-else-if="categoria">Productos en la Categoría: {{ categoria }}</h1>
      <h1 v-else>Tienda</h1>
      <ProductList :productos="productosFiltrados" :moneda="moneda" @agregarCarrito="agregarAlCarrito"/>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ProductList from "@/components/ProductList.vue";
import { mapActions, mapGetters } from 'vuex';

export default {
  components:{
    ProductList
  },
  props: {
    moneda:{
      type:String
    }
  },
  data() {
    return {
      tools: [],
      categoria: "",
      text: "",
    };
  },
  computed: {
    productosFiltrados() {
      if (this.categoria) {
        return this.tools.filter((tool) => tool.CATEGORIA == this.categoria);
      } else if (this.text) {
        return this.tools.filter((tool) =>
          tool.NOMBRE.toUpperCase().includes(this.text.toUpperCase())
        );
      } else {
        return this.tools;
      }
    },
    ...mapGetters(['carrito'])
  },
  watch: {
    "$route.query": {
      handler() {
        this.categoria = this.$route.query.categoria;
        this.text = this.$route.query.text;
      },
      immediate: true,
    },
  },
  created() {
    this.fetchData();
    this.categoria = this.$route.query.categoria;
    this.text = this.$route.query.text;
  },
  methods: {
    async fetchData() {
      try {
        const response = await axios.get("http://127.0.0.1:5000/tools/");
        this.tools = response.data["TOOLS"];
      } catch (error) {
        console.error("Error fetching data: ", error);
      }
    },
    ...mapActions(['agregarAlCarrito']),
    }
  };
</script>
<style scoped>
.store-view {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.container {
  width: 90%;
  margin: 20px;

}
h1{
  font-size: 2em;
  color: #333;
  border: 1px solid #ccc;
  padding: 10px;  
}
</style>
