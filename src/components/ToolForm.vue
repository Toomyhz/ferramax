<template>
  <form @submit.prevent="enviarFormulario" class="form-container">
    <!-- Nombre -->
    <div class="form-group">
      <label>Nombre</label>
      <input
        v-model="form.nombre"
        required
        class="form-input"
        :class="{ changed: cambio('nombre') }"
      />
      <p v-if="cambio('nombre')" class="form-note">
        Nombre anterior:
        <span class="italic">{{ props.herramienta.NOMBRE }}</span>
      </p>
    </div>

    <!-- Valor -->
    <div class="form-group">
      <label>Valor (CLP)</label>
      <input
        v-model.number="form.valor"
        type="number"
        required
        class="form-input"
        :class="{ changed: cambio('valor') }"
      />
      <p v-if="cambio('valor')" class="form-note">
        Valor anterior:
        <span class="line-through">{{ props.herramienta.VALOR }}</span>
      </p>
    </div>

    <!-- Cantidad -->
    <div class="form-group">
      <label>Cantidad</label>
      <input
        v-model.number="form.cantidad"
        type="number"
        required
        class="form-input"
        :class="{ changed: cambio('cantidad') }"
      />
      <p v-if="cambio('cantidad')" class="form-note">
        Cantidad anterior:
        <span class="highlight">{{ props.herramienta.CANTIDAD }}</span>
      </p>
    </div>

    <!-- Categoría -->
    <div class="form-group">
      <label>Categoría</label>
      <select
        v-model.number="form.id_categoria"
        required
        class="form-input"
        :class="{ changed: cambio('id_categoria') }"
      >
        <option
          v-for="cat in categorias"
          :key="cat.ID_CATEGORIA"
          :value="cat.ID_CATEGORIA"
        >
          {{ cat.CATEGORIA }}
        </option>
      </select>
      <p v-if="cambio('id_categoria')" class="form-note">
        Categoría anterior:
        {{ obtenerNombreCategoria(props.herramienta.ID_CATEGORIA) }}
      </p>
    </div>

    <!-- Marca -->
    <div class="form-group">
      <label>Marca</label>
      <select
        v-model.number="form.id_marca"
        required
        class="form-input"
        :class="{ changed: cambio('id_marca') }"
      >
        <option v-for="m in marcas" :key="m.ID_MARCA" :value="m.ID_MARCA">
          {{ m.MARCA }}
        </option>
      </select>
      <p v-if="cambio('id_marca')" class="form-note">
        Marca anterior: {{ obtenerNombreMarca(props.herramienta.ID_MARCA) }}
      </p>
    </div>

    <!-- Imagen -->
    <div class="form-group">
      <label>Imagen (URL)</label>
      <input
        v-model="form.imagen"
        type="text"
        required
        class="form-input"
        :class="{ changed: cambio('imagen') }"
      />
      <p v-if="cambio('imagen')" class="form-note">
        URL anterior: <span class="italic">{{ props.herramienta.IMAGEN }}</span>
      </p>
    </div>

    <!-- Botones -->
    <div class="form-actions">
      <button type="button" @click="$emit('cancelar')" class="btn cancel">
        Cancelar
      </button>
      <button type="submit" class="btn save">Guardar</button>
    </div>
  </form>
</template>

<script setup>
import { reactive, onMounted } from "vue";
import axios from "axios";

const props = defineProps({
  herramienta: Object,
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
    form.nombre = props.herramienta.NOMBRE;
    form.valor = props.herramienta.VALOR;
    form.cantidad = props.herramienta.CANTIDAD;
    form.imagen = props.herramienta.imagen;
    form.id_categoria = props.herramienta.ID_CATEGORIA;
    form.id_marca = props.herramienta.ID_MARCA;
  }
};

const cambio = (campo) => {
  if (!props.herramienta) return false;
  return form[campo] !== props.herramienta[campo.toUpperCase()];
};

const enviarFormulario = async () => {
  try {
    if (props.herramienta) {
      await axios.put(
        `http://localhost:5000/tools/${props.herramienta.ID_HERRAMIENTA}`,
        form
      );
    } else {
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
.form-container {
  background-color: #fff;
  max-width: 700px;
  margin: 2rem auto;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.06);
  border: 1px solid #ddd;
}

.form-title {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 1.5rem;
  color: #2c3e50;
  text-align: center;
}

.form-group {
  margin-bottom: 1.25rem;
}

.form-group label {
  display: block;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.form-input {
  width: 100%;
  padding: 0.6rem;
  font-size: 14px;
  border-radius: 6px;
  border: 1px solid #ccc;
  outline: none;
  transition: border-color 0.2s;
}

.form-input:focus {
  border-color: #3498db;
}

.changed {
  border-color: #f1c40f;
  background-color: #fff9db;
}

.form-note {
  margin-top: 0.4rem;
  font-size: 13px;
  color: #666;
}

.highlight {
  color: #c0392b;
}

.form-actions {
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
  margin-top: 2rem;
}

.btn {
  padding: 0.6rem 1.2rem;
  font-weight: bold;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.btn.cancel {
  background-color: #bdc3c7;
  color: #2c3e50;
}

.btn.cancel:hover {
  background-color: #95a5a6;
}

.btn.save {
  background-color: #2ecc71;
  color: white;
}

.btn.save:hover {
  background-color: #27ae60;
}
</style>
