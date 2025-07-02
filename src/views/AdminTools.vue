<template>
  <div class="admin-container">
    <h1 class="admin-title">Administrar Herramientas</h1>

    <button
      v-if="!mostrarFormulario"
      class="btn btn-success"
      @click="mostrarFormulario = true"
    >
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
          <th>Imagen</th>
          <th>Nombre</th>
          <th>Precio</th>
          <th>Categoría</th>
          <th>Marca</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="h in herramientas" :key="h.id_herramienta">
          <td>
            <img
              :src="h.IMAGEN"
              alt="Imagen de herramienta"
              style="max-width: 80px; max-height: 80px"
            />
          </td>
          <td>{{ h.NOMBRE }}</td>
          <td>${{ h.VALOR }}</td>
          <td>{{ h.CATEGORIA }}</td>
          <td>{{ h.MARCA }}</td>
          <td class="acciones">
            <RouterLink
              :to="{ name: 'editTool', params: { id: h.ID_HERRAMIENTA } }"
            >
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
import { getTools } from "@/api/tools";
import { getBrandById } from "@/api/brands";

const herramientas = ref([]);
const mostrarFormulario = ref(false);
const herramientaEditando = ref(null);
const cargando = ref(false);

const cargarHerramientas = async () => {
  cargando.value = true;
  try {
    herramientas.value = await getTools();
    for (const herramienta of herramientas.value) {
      const marca = await getBrandById(herramienta.ID_MARCA);
      herramienta.MARCA = marca.MARCA;
    }
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
  background: linear-gradient(to right, #fdfbfb, #ebedee);
  min-height: 100vh;
  font-family: "Segoe UI", sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.admin-title {
  font-size: 26px;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 1.5rem;
  text-align: center;
}

.btn {
  padding: 0.5rem 1rem;
  font-size: 15px;
  font-weight: 600;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.btn-success {
  background-color: #2ecc71;
  color: white;
  margin-bottom: 1.5rem;
}

.btn-success:hover {
  background-color: #27ae60;
}

.btn-primary {
  background-color: #3498db;
  color: white;
}

.btn-primary:hover {
  background-color: #2980b9;
}

.btn-danger {
  background-color: #e74c3c;
  color: white;
}

.btn-danger:hover {
  background-color: #c0392b;
}

.admin-table {
  width: 100%;
  max-width: 1000px;
  border-collapse: collapse;
  background-color: white;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.07);
  border-radius: 8px;
  overflow: hidden;
}

.admin-table th,
.admin-table td {
  padding: 1rem;
  border-bottom: 1px solid #e0e0e0;
  text-align: left;
  font-size: 14px;
  color: #333;
}

.admin-table th {
  background-color: #f8f9fa;
  font-weight: 600;
  text-transform: uppercase;
  font-size: 13px;
  color: #555;
}

.acciones {
  display: flex;
  gap: 0.6rem;
}

.form-container {
  width: 100%;
  max-width: 800px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 10px;
  padding: 1.5rem;
  margin-bottom: 2rem;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
}

.loading {
  margin-top: 2rem;
  color: #666;
  font-style: italic;
  font-size: 15px;
}
</style>
