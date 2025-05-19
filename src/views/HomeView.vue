<template>
  <main class="home">
    <section class="firstSection">
      <div
        id="carouselExampleIndicators"
        class="carousel slide"
        data-ride="carousel"
      >
        <h2>Conoce nuestras marcas</h2>
        <p>
          Trabajamos con las mejores marcas para que recibas productos de
          calidad ¡garantizada!.
        </p>
        <ol class="carousel-indicators">
          <li
            data-target="#carouselExampleIndicators"
            data-slide-to="0"
            class="active"
          ></li>
          <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
          <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
        </ol>
        <div class="carousel-inner">
          <div class="carousel-item active">
            <RouterLink
            :to="{ name: 'store' }"
            >
            <img
            class="d-block w-100 carousel-image"
            src="../assets/images/Bauker_herramientas.png"
            alt="First slide"
            />
            </RouterLink>
          </div>
          <div class="carousel-item">
            <RouterLink
            :to="{ name: 'store' }"
            >
            <img
            class="d-block w-100 carousel-image"
            src="../assets/images/Bosch_herramientas.jpg"
            alt="Second slide"
            />
            </RouterLink>
          </div>
          <div class="carousel-item">
            <RouterLink
            :to="{ name: 'store' }"
            >
            <img
            class="d-block w-100 carousel-image"
            src="../assets/images/Makita_herramientas.jpg"
            alt="Third slide"
            />
            </RouterLink>
          </div>
        </div>
        <a
          class="carousel-control-prev custom-carousel-control"
          href="#carouselExampleIndicators"
          role="button"
          data-slide="prev"
        >
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="sr-only">Previous</span>
        </a>
        <a
          class="carousel-control-next custom-carousel-control"
          href="#carouselExampleIndicators"
          role="button"
          data-slide="next"
        >
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="sr-only">Next</span>
        </a>
      </div>
      <div class="second">
        <div class="suscribe">
          <h3>Suscríbete para recibir todas nuestras ofertas</h3>
          <RouterLink :to="{ name: 'suscribir' }" class="btn btn-warning"
            >Suscribir</RouterLink>
        </div>
        <div>
          <h3>Inicia sesión para recibir un descuento del 15%</h3>
          <RouterLink :to="{ name: 'login' }" class="btn btn-warning"
            >Iniciar sesión</RouterLink>
        </div>
      </div>
    </section>
    <div class="secondSection">
      <article>
        <i class="bi bi-check2-all"></i>
        <h5>Calidad de productos</h5>
      </article>
      <article>
        <i class="bi bi-truck"></i>
        <h5>Envíos gratis</h5>
      </article>
      <article>
        <i class="bi bi-arrow-left-right"></i>
        <h5>Garantía extendida</h5>
      </article>
      <article>
        <i class="bi bi-telephone-inbound"></i>
        <h5>Soporte las 24 horas</h5>
      </article>
    </div>
    <section class="brands">
      <div>
        <article v-for="brand in brands" :key="brand.id_marca">
          <RouterLink
            :to="{ name: 'store', query: { brands: brand.id_marca } }"
          >
            <img :src="`${brand.IMAGEN}`" alt="Brand image" />
          </RouterLink>
        </article>
      </div>
    </section>
  </main>
</template>

<script setup>
import { RouterLink } from "vue-router";
</script>

<script>
import { getBrands } from "@/api/brands";

export default {
  data() {
    return {
      brands: [],
    };
  },
  mounted() {
    this.fetchMarcaData();
  },
  methods: {
    async fetchMarcaData() {
      try {
        this.brands = await getBrands()
      } catch (error) {
        console.error("Error fetching data: ", error);
      }
    },
  },
};
</script>

<style scoped>
.home{
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.firstSection {
  width: 95%;
  margin: 50px auto;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.carousel {
  width: 100%;
  max-width: 600px;
}

.carousel-image {
  width: 100%;
  height: auto;
}

.custom-carousel-control {
  background-color: rgba(0, 0, 0, 0.5);
  border-radius: 50%;
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background-color 0.3s ease;
  position: absolute;
  top: 55%;
}

.custom-carousel-control:hover {
  background-color: rgba(0, 0, 0, 0.7);
}

.carousel-control-prev-icon,
.carousel-control-next-icon {
  width: 20px;
  height: 20px;
}

.second {
  width: 50%;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
}

.suscribe,
.second div {
  width: 100%;
  max-width: 400%;
  background-image: url("https://picsum.photos/seed/picsum/674/180");
  height: 180px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 25px;
  margin: 10px 0;
  border: 2px solid rgb(37, 37, 46);
  text-align: center;
}

.suscribe h3,
.second div h3 {
  font-size: 1rem;
}

.secondSection {
  display: flex;
  width: 100%;
  flex-wrap: wrap;
  justify-content: space-around;
  align-items: center;
  border-top: 25px solid rgb(37, 37, 46);
  border-bottom: 25px solid rgb(37, 37, 46);
  padding: 20px 0;
}

.secondSection article {
  width: 45%;
  max-width: 300px;
  margin: 10px 0;
  background-color: white;
  display: flex;
  align-items: center;
  justify-content: space-evenly;
  padding: 10px;
  border-radius: 20px;
  text-align: center;
}

.secondSection i {
  font-size: 2rem;
  color: #ffd333;
}

.brands {
  margin-top: 40px;
  display: flex;
  justify-content: center;
}

.brands div {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.brands article {
  margin: 10px;
}

.brands img {
  width: 100px;
  height: auto;
}

@media (min-width: 768px) {
  .firstSection {
    flex-direction: row;
    justify-content: space-between;
  }

  .carousel {
    max-width: 50%;
  }

  .second {
    width: 37%;
  }

  .suscribe h3,
  .second div h3 {
    font-size: 1.3rem;
  }
}

@media (max-width: 768px) {
  .suscribe h3,
  .second div h3 {
    font-size: 0.8rem;
  }
}
</style>
