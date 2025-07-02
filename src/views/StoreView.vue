<template>
  <div class="store-view">
    <div class="container">
      <h1 v-if="text">Resultados de: {{ text }}</h1>
      <h1 v-else-if="categoria">Productos en la Categoría: {{ categoria }}</h1>
      <h1 v-else-if="brandId">Productos de la Marca: {{ brandId }}</h1>
      <h1 v-else>Productos</h1>
      <ProductList
        :productos="productosFiltrados"
        :moneda="props.moneda"
        @agregarCarrito="agregarAlCarrito"
      />
    </div>
  </div>
</template>
<script setup>
import { ref, computed, watch, onMounted } from "vue";
import { useRoute } from "vue-router";
import { useStore } from "vuex";
import ProductList from "@/components/ProductList.vue";
import { getTools } from "@/api/tools";

const props = defineProps({
  moneda: String,
});

const route = useRoute();
const store = useStore();

const tools = ref([]);
const categoria = ref(route.query.categoria || "");
const text = ref(route.query.text || "");
const brandId = ref(route.query.brands || null);

const productosFiltrados = computed(() => {
  if (brandId.value) {
    return tools.value.filter((tool) => tool.ID_MARCA == brandId.value);
  } else if (categoria.value) {
    return tools.value.filter((tool) => tool.CATEGORIA === categoria.value);
  } else if (text.value) {
    return tools.value.filter((tool) =>
      tool.NOMBRE.toUpperCase().includes(text.value.toUpperCase())
    );
  } else {
    return tools.value;
  }
});

const fetchData = async () => {
  try {
    tools.value = await getTools();
  } catch (error) {
    console.error("Error fetching data:", error);
  }
};

onMounted(fetchData);

watch(
  () => route.query,
  (query) => {
    categoria.value = query.categoria;
    text.value = query.text;
    brandId.value = query.brands;
  },
  { immediate: true }
);

const agregarAlCarrito = (producto) => {
  store.dispatch("agregarAlCarrito", producto);
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
