<template>
  <form
    @submit.prevent="enviarFormulario"
    class="max-w-xl mx-auto bg-white p-6 rounded-xl shadow"
  >
    <h2 class="text-lg font-bold mb-4">
      {{ props.herramienta ? "Editar herramienta" : "Agregar herramienta" }}
    </h2>

    <!-- Nombre -->
    <div class="mb-4">
      <label class="block text-sm font-medium">Nombre</label>
      <input
        v-model="form.NOMBRE"
        required
        class="input"
        :class="{ 'border-yellow-500': cambio('nombre') }"
      />
      <p v-if="cambio('nombre')" class="text-xs text-gray-500 mt-1">
        Nombre anterior:
        <span class="italic">{{ props.herramienta.NOMBRE }}</span>
      </p>
    </div>

    <!-- Valor -->
    <div class="mb-4">
      <label class="block text-sm font-medium">Valor (CLP)</label>
      <input
        v-model.number="form.VALOR"
        type="number"
        required
        class="input"
        :class="{ 'border-yellow-500': cambio('valor') }"
      />
      <p v-if="cambio('valor')" class="text-xs text-gray-500 mt-1">
        Valor anterior:
        <span class="line-through text-red-500">{{
          props.herramienta.VALOR
        }}</span>
      </p>
    </div>

    <!-- Cantidad -->
    <div class="mb-4">
      <label class="block text-sm font-medium">Cantidad</label>
      <input
        v-model.number="form.CANTIDAD"
        type="number"
        required
        class="input"
        :class="{ 'border-yellow-500': cambio('cantidad') }"
      />
      <p v-if="cambio('cantidad')" class="text-xs text-gray-500 mt-1">
        Cantidad anterior:
        <span class="text-red-500">{{ props.herramienta.CANTIDAD }}</span>
      </p>
    </div>

    <!-- Categoría -->
    <div class="mb-4">
      <label class="block text-sm font-medium">Categoría</label>
      <select
        v-model.number="form.ID_CATEGORIA"
        required
        class="input"
        :class="{ 'border-yellow-500': cambio('id_categoria') }"
      >
        <option
          v-for="cat in categorias"
          :key="cat.ID_CATEGORIA"
          :value="cat.ID_CATEGORIA"
        >
          {{ cat.CATEGORIA }}
        </option>
      </select>
      <p v-if="cambio('id_categoria')" class="text-xs text-gray-500 mt-1">
        Categoría anterior:
        {{ obtenerNombreCategoria(props.herramienta.ID_CATEGORIA) }}
      </p>
    </div>

    <!-- Marca -->
    <div class="mb-4">
      <label class="block text-sm font-medium">Marca</label>
      <select
        v-model.number="form.ID_MARCA"
        required
        class="input"
        :class="{ 'border-yellow-500': cambio('id_marca') }"
      >
        <option v-for="m in marcas" :key="m.ID_MARCA" :value="m.ID_MARCA">
          {{ m.MARCA }}
        </option>
      </select>
      <p v-if="cambio('id_marca')" class="text-xs text-gray-500 mt-1">
        Marca anterior: {{ obtenerNombreMarca(props.herramienta.ID_MARCA) }}
      </p>
    </div>

    <!-- Imagen -->
    <div class="mb-4">
      <label class="block text-sm font-medium">Imagen (URL)</label>
      <input
        v-model="form.imagen"
        type="text"
        required
        class="input"
        :class="{ 'border-yellow-500': cambio('imagen') }"
      />
      <p v-if="cambio('imagen')" class="text-xs text-gray-500 mt-1">
        URL anterior: <span class="italic">{{ props.herramienta.imagen }}</span>
      </p>
    </div>

    <!-- Botones -->
    <div class="flex justify-end gap-3 mt-6">
      <button
        type="button"
        @click="$emit('cancelar')"
        class="btn bg-gray-300 hover:bg-gray-400"
      >
        Cancelar
      </button>
      <button
        type="submit"
        class="btn bg-blue-600 text-white hover:bg-blue-700"
      >
        Guardar
      </button>
    </div>
  </form>
</template>

<script setup>
import { reactive, onMounted } from "vue";
import axios from "axios";

const props = defineProps({
  herramienta: Object, // puede ser null si es creación
});
const emit = defineEmits(["guardar", "cancelar"]);

const form = reactive({
  nombre: "",
  valor: 0,
  cantidad: 1,
  imagen: "",
  id_categoria: null,
  id_marca: null,
});

const categorias = reactive([]);
const marcas = reactive([]);

const cargarDatos = async () => {
  const [catRes, marcaRes] = await Promise.all([
    axios.get("http://localhost:5000/categories/"),
    axios.get("http://localhost:5000/marcas/"),
  ]);
  categorias.push(...catRes.data.CATEGORIAS);
  marcas.push(...marcaRes.data.MARCAS);

  if (props.herramienta) {
    Object.assign(form, props.herramienta);
  }
};

const cambio = (campo) => {
  return props.herramienta && form[campo] !== props.herramienta[campo];
};

const enviarFormulario = async () => {
  try {
    if (props.herramienta) {
      // Editar
      await axios.put(
        `http://localhost:5000/tools/${props.herramienta.ID_HERRAMIENTA}`,
        form
      );
    } else {
      // Crear
      await axios.post("http://localhost:5000/tools/", form);
    }

    emit("guardar");
  } catch (error) {
    alert("Error al guardar: " + error.message);
  }
};

onMounted(() => {
  cargarDatos();
});

const obtenerNombreMarca = (id) => {
  const marca = marcas.find((m) => m.ID_MARCA === id);
  return marca ? marca.MARCA : "Desconocida";
};

const obtenerNombreCategoria = (id) => {
  const categoria = categorias.find((c) => c.ID_CATEGORIA === id);
  return categoria ? categoria.CATEGORIA : "Desconocida";
};
</script>

<style scoped>
.input {
  @apply w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400;
}
.btn {
  @apply px-4 py-2 rounded font-semibold;
}
</style>
