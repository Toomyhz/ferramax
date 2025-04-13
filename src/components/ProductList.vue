<template>
    <div class="product-grid container">
      <div class="product-card" v-for="producto in productos" :key="producto.ID_HERRAMIENTA">
        <h3>{{ producto.NOMBRE }}</h3>
        <img :src="producto.IMAGEN" alt="Imagen del Producto" class="product-img"/>
        <p>{{ producto.CATEGORIA }}</p>
        <p v-if="moneda == 'USD'">USD $ {{ producto.VALOR_EN_DOLARES }}</p>
        <p v-if="moneda == 'CLP'">CLP ${{ producto.VALOR }}</p>
        <button class="btn-add-cart" @click="agregarAlCarrito(producto)">Agregar a Carrito</button>
      </div>
    </div>
  </template>
  
  <script>
  import Swal from 'sweetalert2';
  export default {
    name: "ProductList",
    props: {
      productos: {
        type: Array,
        required: true,
      },
      moneda: {
        type: String
      }
    },
    methods: {
      agregarAlCarrito(producto) {
        this.$emit('agregarCarrito', producto);
        Swal.fire({
          text: 'Producto agregado al carrito',
          width: '300px',
          icon: 'success',
          position: 'top-end',
          toast: true,
          showConfirmButton:false,
          timer: 2000,
        });

      }
    }
  };
  </script>
  
  <style scoped>
  .product-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    padding: 16px;
  }
  
  .product-card {
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 8px;
    overflow: hidden;
    text-align: center;
    transition: box-shadow 0.3s ease-in-out;
  }
  
  .product-card:hover {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  }
  
  .product-img {
    width: 100%;
    height: auto;
  }
  
  .product-card h3 {
    margin: 16px 0 8px;
    font-size: 1.2em;
  }
  
  .product-card p {
    margin: 4px 0;
    color: #555;
  }
  
  .product-card p:last-of-type {
    font-weight: bold;
    color: #000;
  }
  .btn-add-cart {
    background-color: #ffd333;
    border: none;
    padding: 10px 20px;
    border-radius: 4px;
    transition: background-color 0.3s ease-in-out;
    margin:16px 0;
  }
  .btn-add-cart:hover {
    background-color: #e6c32f;
  }
  .btn-add-cart:active {
    background-color: #d4b52a;
  }
  @media screen and (max-width: 768px) {
    .product-grid {
      grid-template-columns: repeat(2, 1fr);
    }
    .product-card {
      margin: 0 auto;
    }
    
  }
  </style>
  