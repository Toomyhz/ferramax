<script setup>
import { RouterLink } from 'vue-router';
</script>
<script>
import axios from 'axios';

export default {
  data(){
    return{
      categorias:[]
    };
  },
  mounted(){
    this.fetchData();
  },
  methods:{
    async fetchData(){
      try{
        const response = await
        axios.get('http://127.0.0.1:5000/categories/');
        this.categorias = response.data['CATEGORIAS'];
      } catch(error){
        console.error('Error fetching data: ', error)
      }
    },
  }
}
</script>
<template>
    <header>
  <div class="start">
    <div class="marca">
      <RouterLink to="/"><span class="first">FERRA</span><span class="second">MAX</span></RouterLink>
    </div>
    <div id="buscador" class="m-auto">
      <form action="/store" method="GET">
        <span><i class="bi bi-search"></i></span><input type="search" name="text" id="search">
      </form>
    </div>
  </div>
  <nav>
    <div class="div-categoria">
      <button id="btn-categorias" onclick=""><span><i class="bi bi-list"></i>Categorias</span><span><i class="bi bi-arrow-bar-down"></i></span></button>
      <div id="dropdown-content" class="dropdown-content">
        <RouterLink :to="`/store/?categoria=${categoria.CATEGORIA}`"  v-for="categoria in categorias" :key = "categoria.ID_CATEGORIA" >{{ categoria.CATEGORIA }}</RouterLink>
      </div>
    </div>
    <ul class="navbar-1">
      <li><RouterLink to="/store">Tienda</RouterLink></li>
      <li><RouterLink to="/login">Iniciar sesión</RouterLink></li>
      <li><RouterLink to="/register">Registrarse</RouterLink></li>
    </ul>
    <div class="tools">
      <li>
        <RouterLink to="/cart"><i class="bi bi-cart3"></i></RouterLink>
      </li>
    </div>
  </nav>
</header>
</template>
<style scoped>
    
header{
    margin: 0;
    padding: 0;
}
.start{
    height: 100px;
    padding: 0 50px;
    background-color: #f5f5f5;
    display: flex;
    align-items: center;
}
nav{
    height: 50px;
    padding: 0 50px;
    background-color: rgb(49, 49, 58);
    display: flex;
    align-items: center;
}
.marca{
    height: 50px;
    font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
    font-size: 40px;
    align-content: center;
    display: flex;
    cursor:pointer;
    transition: 0.5s;
}
.marca:hover{
    transform: scale(1.2);
    
}
.marca>a{
    text-decoration: none;
}
.first{
    background-color: #ffd333;
    color: rgb(37,37,46);
    padding: 0 10px;
}
.second{
    background-color: rgb(37,37,46);
    color: #ffd333;
    padding: 0 10px;
}
.div-categoria{
    height: 100%;
    position: relative;
    display: inline-block;
}
.dropdown-content{
    position: relative;
    height:0;
    width: 100%;
    display: none;
    background-color: #ffd333;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    transition: 5s ;
    z-index: 1;
    visibility: hidden;
    
}
.dropdown-content a {
    color: black;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
    transition: 0.3s;
}
.dropdown-content a:hover {
    background-color: antiquewhite;
    
}
.div-categoria:hover .dropdown-content{
    display: block;
    height: auto;
    visibility: visible;
}
.div-categoria #btn-categorias>span:last-child{
    transition: 0.5s;
}
.div-categoria:hover #btn-categorias>span:last-child{
    transform: rotate(540deg);
}
#btn-categorias{
    height: 100%;
    width: 300px;
    padding: 0 20px;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    border: none;
    font-size: 20px;
    background-color: #ffd333;
    display: flex;
    justify-content: space-between;
    align-items: center;

}
.navbar-1{
    padding: 0;
    margin: 0;
    display: flex;
    height: 100%;
    list-style-type: none;
    li{
        padding: 0;
        margin: 0;
        height: 100%;
        width: 200px;
        display: flex;
        a{
            padding: 0;
            margin: 0;
            height: 100%;
            width: 100%;
            text-decoration: none;
            color: #f5f5f5;
            transition: 0.2s;
            text-align: center;
            align-content: center;
            border-bottom: none;
        };
        a:hover{
            color: #ffd333;
            border-bottom: #ffd333 5px solid;
            box-sizing: border-box;
            font-size: 1.2rem;
        }

    };    
}
.tools{
    display: flex;
    height: 100%;
    margin-left: auto;
}
.tools>li{
    list-style-type: none;
    width: 70px;
    height: 100%;
    display: flex;
    a{
        width: 70px;
        height: 100%;
        text-decoration: none;
        color: #ffd333;
        display: flex;
        justify-content: center;
        align-items: center;
        transition: 0.2s;
        font-size: 1.5rem;
    };
    a:hover{
        border-bottom: 5px #ffd333 solid;
        box-sizing: border-box;
        i{
            font-size:2rem;

        }
    }
}
#buscador{
    form{
        input{
            width: 400px;
            border: 1px solid black;
            transition:0.2s;
        }
    }
}
#search:focus{
    outline: none;
    border: 3px solid #ffd333;
    width: 450px;
}
.username{
    margin: 0;
    width: 100%;
    text-align: center;
    align-content: center;
    color: #ffd333;
    transition: 0.2s;
}
</style>