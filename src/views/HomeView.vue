<script>
import axios from 'axios';

export default {
  data(){
    return{
      brands:[]
    };
  },
  mounted(){
    this.fetchData();
  },
  methods:{
    async fetchData(){
      try{
        const response = await
        axios.get('http://127.0.0.1:5000/marcas/');
        this.brands = response.data['MARCAS'];
      } catch(error){
        console.error('Error fetching data: ', error)
      }
    },
  }
}
</script>

<template>
  <main>
    <section class="firstSection">
      <div class="first">
        <h2>Conoce nuestras marcas</h2>
        <p>Trabajamos con las mejores marcas para que recibas productos de calidad garantizada.</p>
      </div>
      <div class="second">
        <div class="suscribe">
          <h3>Suscribete para recibir todas nuestras ofertas</h3>
          <button>Suscribir</button>
        </div>
        <div>
          <h3>Inicia sesión para recibir un descuento del 15%</h3>
          <button>Iniciar sesión</button>
        </div>
      </div>
    </section>
    <div class="secondSection">
      <article><i class="bi bi-check2-all"></i><h5>Calidad de productos</h5></article>
      <article><i class="bi bi-truck"></i><h5>Envios gratis</h5></article>
      <article><i class="bi bi-arrow-left-right"></i><h5>Garantía extendida</h5></article>
      <article><i class="bi bi-telephone-inbound"></i><h5>Soporte las 24 horas</h5></article>
    </div>
    <section class="brands">
      <div>
        <article v-for="brand in brands" :key="brand.id_marca">
        <img :src="`${brand.IMAGEN}`" alt="Algo">
        </article>
      </div>
    </section>
  </main>
</template>
<style scoped>
.firstSection{
  width: 95%;
  height: 400px;
  display: flex;
  margin: 40px auto;
  justify-content: space-between;
  .first{
    width:60%;
    background-color: aqua;
    p{
      font-size: 25px;
    }
    }
    .second{
      width:37%;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      div{
        background-image: url("https://picsum.photos/seed/picsum/674/180");
        height: 45%;
        width: 100%;
        align-items: center;
        display: flex;
        flex-direction: column;
        padding: 25px;
        border:10px solid rgb(37,37,46);
        h3{
          width:80%;
          text-align: center;
        };
        button{
          background-color: #ffd333;
          margin: auto;
        }
      }
  }
}
.secondSection{
  display:flex;
  height: 200px;
  justify-content: space-evenly;
  align-items: center;
  border-top: 25px solid rgb(37,37,46);
  border-bottom: 25px solid rgb(37,37,46);
  article{
    width:300px;
    height:60%;
    background-color: white;
    display: flex;
    align-items: center;
    justify-content: space-evenly;
    i{
      font-size: 2rem;
      color:#ffd333;
    };
    border-radius: 20px;
  }
}
.brands{
  div{
    display:flex;
    article{
      img{
        width: 70%
      }
    }
  }
}
</style>