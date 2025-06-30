<template>
  <div class="p-4">
    <h1 class="text-xl font-bold mb-4">Editar Herramienta</h1>
    <ToolForm
      v-if="herramienta"
      :herramienta="herramienta"
      @guardar="volverALista"
      @cancelar="volverALista"
    />
    <p v-else>Cargando herramienta...</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import axios from "axios";
import ToolForm from "@/components/ToolForm.vue";

const route = useRoute();
const router = useRouter();
const herramienta = ref(null);

const cargarHerramienta = async () => {
  try {
    const res = await axios.get(
      `http://localhost:5000/tools/${route.params.id}`
    );
    herramienta.value = res.data[0]; // porque devuelve un array
  } catch (err) {
    alert("Error al cargar herramienta");
    router.push("/admin-tools");
  }
};

const volverALista = () => {
  router.push("/admin-tools");
};

onMounted(() => {
  cargarHerramienta();
});
</script>
