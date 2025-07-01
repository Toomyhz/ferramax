<template>
  <div class="admin-container">
    <h1 class="admin-title">Administrar Herramientas</h1>

    <button class="btn btn-success" @click="mostrarFormulario = true">
      + Nueva herramienta
    </button>

    <div v-if="mostrarFormulario" class="form-container">
      <ToolForm
        :herramienta="herramientaEditando"
        @guardar="guardarHerramienta"
        @cancelar="mostrarFormulario = false"
      />
    </div>

    <div v-if="cargando" class="loading">Cargando herramientas...</div>

    <table v-else class="admin-table">
      <thead>
        <tr>
          <th>Nombre</th>
          <th>Precio</th>
          <th>Categoría</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="h in herramientas" :key="h.id_herramienta">
          <td>{{ h.nombre }}</td>
          <td>${{ h.valor }}</td>
          <td>{{ h.categoria }}</td>
          <td class="acciones">
            <RouterLink :to="{ name: 'editTool', params: { id: h.id_herramienta } }">
              <button class="btn btn-primary">Editar</button>
            </RouterLink>
            <button class="btn btn-danger" @click="eliminar(h.id_herramienta)">
              Eliminar
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import ToolForm from "@/components/ToolForm.vue";

const herramientas = ref([]);
const mostrarFormulario = ref(false);
const herramientaEditando = ref(null);
const cargando = ref(false);

const cargarHerramientas = async () => {
  cargando.value = true;
  try {
    const res = await axios.get("http://localhost:5000/tools/");
    herramientas.value = res.data.TOOLS.map(h => ({
      id_herramienta: h.ID_HERRAMIENTA || h.id_herramienta,
      nombre: h.NOMBRE || h.nombre,
      valor: h.VALOR || h.valor,
      categoria: h.CATEGORIA || h.categoria
    }));
  } catch (error) {
    console.error("Error cargando herramientas:", error);
    alert("Error cargando herramientas");
  } finally {
    cargando.value = false;
  }
};

const guardarHerramienta = async () => {
  mostrarFormulario.value = false;
  herramientaEditando.value = null;
  await cargarHerramientas();
};

const eliminar = async (id) => {
  if (confirm("¿Eliminar herramienta?")) {
    try {
      await axios.delete(`http://localhost:5000/tools/${id}`);
      await cargarHerramientas();
    } catch (error) {
      console.error("Error eliminando herramienta:", error);
      alert("No se pudo eliminar la herramienta");
    }
  }
};

onMounted(() => {
  cargarHerramientas();
});
</script>

<style scoped>
.admin-container {
  padding: 2rem;
  background-color: #f9f9f9;
  min-height: 100vh;
  font-family: Arial, sans-serif;
}

.admin-title {
  font-size: 24px;
  font-weight: bold;
  color: #333;
  margin-bottom: 1rem;
}

.btn {
  padding: 0.4rem 0.8rem;
  font-size: 14px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background 0.2s ease;
}

.btn-success {
  background-color: #28a745;
  color: white;
  margin-bottom: 1rem;
}

.btn-success:hover {
  background-color: #218838;
}

.btn-primary {
  background-color: #007bff;
  color: white;
}

.btn-primary:hover {
  background-color: #0069d9;
}

.btn-danger {
  background-color: #dc3545;
  color: white;
}

.btn-danger:hover {
  background-color: #c82333;
}

.admin-table {
  width: 100%;
  border-collapse: collapse;
  background-color: white;
  box-shadow: 0 2px 5px rgba(0,0,0,0.05);
  border: 1px solid #ddd;
}

.admin-table th,
.admin-table td {
  padding: 0.75rem;
  border: 1px solid #eee;
  text-align: left;
}

.admin-table th {
  background-color: #f0f0f0;
}

.acciones {
  display: flex;
  gap: 0.5rem;
}

.form-container {
  margin-bottom: 2rem;
  padding: 1rem;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.loading {
  margin-top: 1rem;
  color: #555;
}
</style>
