<template>
  <div class="p-4">
    <h1>Administrar Herramientas</h1>
    <button @click="mostrarFormulario = true">+ Nueva herramienta</button>

    <ToolForm
      v-if="mostrarFormulario"
      :herramienta="herramientaEditando"
      @guardar="guardarHerramienta"
      @cancelar="mostrarFormulario = false"
    />

    <table>
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
          <td>{{ h.NOMBRE }}</td>
          <td>{{ h.VALOR }}</td>
          <td>{{ h.CATEGORIA }}</td>
          <td>
            <RouterLink
              :to="{ name: 'editTool', params: { id: h.ID_HERRAMIENTA } }"
            >
              <button class="btn btn-primary text-white px-2 py-1 rounded">
                Editar
              </button>
            </RouterLink>
            <button
              class="btn btn-danger text-white px-2 py-1 rounded"
              @click="eliminar(h.id_herramienta)"
            >
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

const cargarHerramientas = async () => {
  const res = await axios.get("http://localhost:5000/tools/");
  herramientas.value = res.data.TOOLS;
};

const guardarHerramienta = async () => {
  mostrarFormulario.value = false;
  herramientaEditando.value = null;
  await cargarHerramientas();
};

const editar = (h) => {
  herramientaEditando.value = { ...h };
  mostrarFormulario.value = true;
};

const eliminar = async (id) => {
  if (confirm("¿Eliminar herramienta?")) {
    await axios.delete(`http://localhost:5000/tools/${id}`);
    await cargarHerramientas();
  }
};

onMounted(() => {
  cargarHerramientas();
});
</script>
