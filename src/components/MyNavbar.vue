<template>
    <header>
      <div class="start">
        <div class="marca">
          <RouterLink :to="{ name: 'home' }">
            <span class="first">FERRA</span><span class="second">MAX</span>
          </RouterLink>
        </div>
        <div id="buscador" class="m-auto">
            <span ><i class="bi bi-search"></i></span>
            <input
              type="search"
              name="text"
              id="search"
              @keyup.enter="navegar"
              v-model="text"
              placeholder="Ingrese el producto a buscar"
            />
        </div>
        <div class="cambio">
          <button @click="cambiarCambio">Tipo de cambio: {{ cambioActual }}</button>
        </div>
      </div>
      <nav>
        <div class="div-categoria">
          <button id="btn-categorias">
            <span><i class="bi bi-list"></i>Categorias</span>
            <span><i class="bi bi-arrow-bar-down"></i></span>
          </button>
          <div id="dropdown-content" class="dropdown-content">
            <RouterLink
              :to="{ name: 'store', query: { categoria: categoria.CATEGORIA } }"
              v-for="categoria in categorias"
              :key="categoria.ID_CATEGORIA"
            >{{ categoria.CATEGORIA }}</RouterLink>
          </div>
        </div>
        <ul class="navbar-1">
          <li>
            <RouterLink :to="{ name: 'store' }" :class="{ ' active-link': isActive('store') }"
              >Tienda</RouterLink
            >
          </li>
          <li>
            <RouterLink :to="{ name: 'login' }" :class="{ ' active-link': isActive('login') }"
              >Iniciar sesión</RouterLink
            >
          </li>
          <li>
            <RouterLink
              :to="{ name: 'register' }"
              :class="{ ' active-link': isActive('register') }"
              >Registrarse</RouterLink
            >
          </li>
        </ul>
        <div class="tools">
          <div>
            <RouterLink :to="{ name: 'cart' }" :class="{ 'active-link': isActive('cart') }"
              ><i class="bi bi-cart3"></i><span class="contador_carrito" v-if="carrito.length > 0">{{ carrito.length }}</span></RouterLink
          >
          </div>
        </div>
      </nav>
    </header>
  </template>
  
  <script setup>
  import { RouterLink } from 'vue-router';
  </script>
  
  <script>
  import {getCategories} from "@/api/categories";
  import Swal from 'sweetalert2';
  
  export default {
    data() {
      return {
        categorias: [],
        text: '',
      };
    },
    props: {
      cambioActual: {
        type: String,
      },
    },
    watch: {
      '$route.query': {
        handler() {
          this.text = this.$route.query.text;
        },
        immediate: true,
      },
    },
    created() {
      this.fetchData();
      this.text = this.$route.query.text;
    },
    computed: {
      isActive() {
        return (routeName) => {
          return this.$route.name === routeName;
        };
      },
      carrito() {
        return this.$store.getters.carrito;
      }
    },
    methods: {
      async fetchData() {
        try {
          this.categorias = await getCategories()
          console.log("testeo")
        } catch (error) {
          console.error('Error fetching data: ', error);
        }
      },
      navegar() {
        if (this.text.trim() !== '') {
          this.$router.push({ name: 'store', query: { text: this.text } });
        } else {
          this.$router.push({ name: 'store' });
        }
      },
      cambiarCambio() {
        if (this.cambioActual === 'USD') {
          this.$emit('cambiarMoneda', 'CLP');
          Swal.fire({
            text: 'Moneda cambiada a: CLP',
            width: '300px',
            position: 'top',
            timer: 2000,
            timerProgressBar: true,
            showConfirmButton: false,
            toast: true,
            icon: 'info',
          });
        } else {
          this.$emit('cambiarMoneda', 'USD');
          Swal.fire({
            text: 'Moneda cambiada a: USD',
            width: '300px',
            position: 'top',
            timer: 2000,
            timerProgressBar: true,
            showConfirmButton: false,
            toast: true,
            icon: 'info',
          });
        }
      },
    },
  };
  </script>
  
  <style scoped>
  header {
    margin: 0;
    padding: 0;
  }
  .start {
    height: 100px;
    padding: 0 50px;
    background-color: #f5f5f5;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
  }

  
  nav {
    height: 50px;
    padding: 0 50px;
    background-color: rgb(49, 49, 58);
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    width: 100%;

  }
  .marca {
    height: 50px;
    font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
    font-size: 40px;
    display: flex;
    cursor: pointer;
    transition: 0.5s;
  }
  .marca:hover {
    transform: scale(1.1);
  }
  .marca > a {
    text-decoration: none;
  }
  .first {
    background-color: #ffd333;
    color: rgb(37, 37, 46);
    padding: 0 10px;
  }
  .second {
    background-color: rgb(37, 37, 46);
    color: #ffd333;
    padding: 0 10px;
  }
  .div-categoria {
    height: 100%;
    position: relative;
    display: inline-block;
  }
  .dropdown-content {
    position: absolute;
    width: 100%;
    display: none;
    background-color: #ffd333;
    box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
    z-index: 1;
  }
  .dropdown-content a {
    color: black;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
  }
  .dropdown-content a:hover {
    background-color: antiquewhite;
  }
  .div-categoria:hover .dropdown-content {
    display: block;
  }
  #btn-categorias {
    height: 100%;
    width: 200px;
    padding: 0 10px;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    border: none;
    font-size: 20px;
    background-color: #ffd333;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .navbar-1 {
    padding: 0;
    margin: 0;
    display: flex;
    height: 100%;
    list-style-type: none;
    flex-wrap: wrap;
  }
  .navbar-1 li {
    padding: 0;
    margin: 0;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 150px;
  }
  .navbar-1 li a {
    padding: 0;
    margin: 0;
    height: 100%;
    width: 100%;
    text-decoration: none;
    color: #f5f5f5;
    text-align: center;
    align-content: center;
    border-bottom: none;
  }
  .navbar-1 li a:hover {
    color: #ffd333;
    border-bottom: #ffd333 5px solid;
    font-size: 1.2rem;
  }
  .tools {
    display: flex;
    height: 100%;
    margin-left: auto;
  }
  .tools > div {
    list-style-type: none;
    width: 70px;
    height: 100%;
    display: flex;
  }
  .tools > div a {
    width: 100%;
    height: 100%;
    text-decoration: none;
    color: #ffd333;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 1.5rem;
  }
  .tools > div a:hover {
    border-bottom: 5px #ffd333 solid;
  }
  #buscador {
    display: flex;
    align-items: stretch;
    width: 500px;
    margin: 10px 0;
  }
  #buscador span{
    border: 1px solid black;
    border-radius: 50px 0% 0% 50px;
    width: 50px;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #ffd333;
    color: #000;
    font-size: 1.2rem;
    transition: 0.2s all ease-in-out;
  }
  #buscador input {
    flex:1;
    width: 80%;
    padding: 10px;
    border: 1px solid black;
    border-left: none;
    border-radius: 0% 25px 25px 0%;
    transition: 0.2s all ease-in-out;
  }
  #buscador input:focus {
    outline: none;
    border: 2.5px solid #ffd333;
    box-sizing: border-box;
  }
  #buscador:focus-within span {
  background-color: rgb(37,37,46);
  color:#ffd333; 
  border-right: none; 
  font-weight: bold;
  font-size: 1.5rem;
}

.cambio{
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    margin-left: auto;
  }
  .cambio button {
    background-color: #ffd333;
    border: none;
    padding: 10px 20px;
    border-radius: 4px;
    transition: background-color 0.3s ease-in-out;
    font-size: 1rem;
  }
  .cambio button:hover {
    background-color: #e6c32f;
  }
  .cambio button:active {
    background-color: #d4b52a;
}

  .active-link {
    color: #ffd333 !important;
    border-bottom: #ffd333 5px solid !important;
    font-size: 1.2rem;
  }
  
  .contador_carrito{
    height: 20px;
    width: 20px;
    display: flex;
    text-align:center;
    justify-content: center;
    font-size: 0.9rem;
    background-color: #ffd333;
    color: rgb(37, 37, 46);
    border-radius:50%
  }
  /* Responsive Styles */
  @media (max-width: 1050px) {
    .start {
      width: 100%;
      height: auto;
      flex-direction: column;
      align-items: center;
      padding:0;
    }
    .marca{
      font-size: 40px;
      margin: 10px 0 30px 0;
    }
    #buscador {
      width: 80%;
      margin: 20px;
      height: 35px;
    }
    #buscador input {
      width: 100%;
    }
    .cambio{
      position: relative;
      margin: 10px 0;
      display: flex
    }
    .cambio>button{
      margin: 0 10px;
      font-size: 1rem;
    }
    nav{
      flex-direction: column;
      align-items: center;
      padding: 0 20px;
    }
    .tools {
      margin-left: 0;
    }
  }
  @media (max-width: 768px) {
    .marca:hover {
    transform: none;
    }
    nav{
      padding: 0;
      align-items: normal;
    }
    .navbar-1{
      display:none;
    }
  }
  </style>
  