<template>
  <div>
    <h1 v-if="text">Resultados de: {{ text }} en {{ categoria }}</h1>
    <h1 v-else-if="categoria">Productos en la Categoría: {{ categoria }}</h1>
    <h1 v-else>Tienda</h1>
    <hr />
    <ProductList :productos="productosFiltrados"/>
    <hr />
  </div>
</template>

<script>
import axios from "axios";
import ProductList from "@/components/ProductList.vue";

export default {
  components:{
    ProductList
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
  },
};
</script>
