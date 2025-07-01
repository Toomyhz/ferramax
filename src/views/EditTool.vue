<template>
  <div class="edit-tool-page">
    <div class="edit-tool-card">
      <h1 class="edit-title">Editar Herramienta</h1>

      <div v-if="loading" class="edit-status loading">
        ⏳ Cargando herramienta...
      </div>

      <div v-else-if="herramienta">
        <ToolForm
          :herramienta="herramienta"
          @guardar="volverALista"
          @cancelar="volverALista"
        />
      </div>

      <div v-else class="edit-status error">
        No se encontró la herramienta.
      </div>
    </div>
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
const loading = ref(true);

const cargarHerramienta = async () => {
  loading.value = true;
  try {
    const res = await axios.get(`http://localhost:5000/tools/${route.params.id}`);
    herramienta.value = Array.isArray(res.data) ? res.data[0] : res.data;
  } catch (err) {
    console.error("Error al cargar herramienta:", err);
    alert("Error al cargar herramienta.");
    router.push("/admin-tools");
  } finally {
    loading.value = false;
  }
};

const volverALista = () => {
  router.push("/admin-tools");
};

onMounted(() => {
  cargarHerramienta();
});
</script>

<style scoped>
.edit-tool-page {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  background-color: #eef2f5;
  min-height: 100vh;
  padding: 3rem 1rem;
}

.edit-tool-card {
  background-color: #fff;
  padding: 2rem;
  max-width: 700px;
  width: 100%;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  border: 1px solid #ddd;
}

.edit-title {
  font-size: 24px;
  font-weight: bold;
  color: #2c3e50;
  margin-bottom: 1.5rem;
  text-align: center;
}

.edit-status {
  padding: 1rem;
  font-size: 16px;
  text-align: center;
  border-radius: 6px;
  margin-top: 1rem;
}

.edit-status.loading {
  background-color: #f0f8ff;
  color: #007bff;
}

.edit-status.error {
  background-color: #ffe6e6;
  color: #c0392b;
}
</style>
