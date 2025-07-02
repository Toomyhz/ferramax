<template>
  <Carousel v-bind="carouselConfig" class="my-carousel">
    <Slide v-for="(img, index) in images" :key="index">
      <RouterLink
        :to="{ name: 'store', query: { brands: img.id_marca } }"
        class="carousel-img-wrapper"
      >
        <img :src="img.src" :alt="img.alt" class="carousel-img" />
      </RouterLink>
    </Slide>
    <template #addons>
      <Navigation />
      <Pagination />
    </template>
  </Carousel>
  <main class="home">
    <section class="firstSection">
      <div class="cta-container">
        <div class="cta-box subscribe">
          <h3>Suscríbete para recibir todas nuestras ofertas</h3>
          <RouterLink :to="{ name: 'suscribir' }" class="btn btn-warning"
            >Suscribir</RouterLink
          >
        </div>
        <div class="cta-box login">
          <h3>Inicia sesión para recibir un descuento del 15%</h3>
          <RouterLink :to="{ name: 'login' }" class="btn btn-warning"
            >Iniciar sesión</RouterLink
          >
        </div>
      </div>
    </section>

    <h2 class="section-title">Conoce nuestras marcas</h2>
    <p class="section-subtitle">
      Trabajamos con las mejores marcas para que recibas productos de calidad
      ¡garantizada!
    </p>
    <section class="brandsSection">
      <article v-for="brand in brands" :key="brand.ID_MARCA" class="brand-item">
        <RouterLink :to="{ name: 'store', query: { brands: brand.ID_MARCA } }">
          <img
            v-if="brand.IMAGEN"
            :src="brand.IMAGEN"
            :alt="`Logo ${brand.MARCA}`"
          />
          <div v-else class="placeholder-logo">
            {{ brand.MARCA }}
          </div>
        </RouterLink>
      </article>
    </section>

    <section class="featuresSection">
      <article class="feature-item">
        <i class="bi bi-check2-all"></i>
        <h5>Calidad de productos</h5>
      </article>
      <article class="feature-item">
        <i class="bi bi-truck"></i>
        <h5>Envíos gratis</h5>
      </article>
      <article class="feature-item">
        <i class="bi bi-arrow-left-right"></i>
        <h5>Garantía extendida</h5>
      </article>
      <article class="feature-item">
        <i class="bi bi-telephone-inbound"></i>
        <h5>Soporte 24/7</h5>
      </article>
    </section>
  </main>
</template>

<script setup>
import { RouterLink } from "vue-router";
import { onMounted, reactive } from "vue";
import { getBrands } from "@/api/brands";
import { Carousel, Slide, Pagination, Navigation } from "vue3-carousel";
import "vue3-carousel/carousel.css";

const brands = reactive([]);

const carouselConfig = {
  itemsToShow: 1,
  wrapAround: true,
  autoplay: 4000,
  transition: 1200,
  mouseDrag: true,
  pauseAutoplayOnHover: true,
  breakpointMode: "carousel",
};

const images = [
  {
    src: "/src/assets/images/Bauker_herramientas.jpg",
    id_marca: 2,
    alt: "Bauker herramientas",
  },
  {
    src: "/src/assets/images/Bosch_herramientas.jpg",
    id_marca: 3,
    alt: "Bosch herramientas",
  },
  {
    src: "/src/assets/images/Makita_herramientas.jpg",
    id_marca: 6,
    alt: "Makita herramientas",
  },
  {
    src: "/src/assets/images/Stanley_herramientas.jpg",
    id_marca: 8,
    alt: "Stanley herramientas",
  },
];

onMounted(async () => {
  try {
    const data = await getBrands();
    brands.push(...data);
  } catch (error) {
    console.error("Error fetching brands:", error);
  }
});
</script>

<style scoped>
:root {
  background-color: #242424;
}

.home {
  width: 100%;
  max-width: 1600px;
  margin: 0 auto;
  padding: 1.5rem;
  font-family: "Poppins", sans-serif;
  color: #333;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.firstSection {
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  margin: 3.5rem 0;
  gap: 2.5rem;
  align-items: center;
}

.section-title {
  font-size: 2.8rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  color: #222;
  text-align: center;
  width: 100%;
}

.section-subtitle {
  font-size: 1.3rem;
  font-weight: 400;
  margin-bottom: 1.8rem;
  text-align: center;
  width: 100%;
  color: #555;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

.carousel {
  height: 330px;
  max-width: 100%;
  --vc-nav-background: rgba(255, 255, 255, 0.7);
  --vc-nav-border-radius: 100%;
}

.carousel-img {
  width: 100%;
  height: 100%;
}

.carousel-img-wrapper {
  display: block;
  width: 100%;
  height: 100%;
}

.carousel-img-wrapper:focus,
.carousel-img-wrapper:visited {
  outline: none;
  text-decoration: none;
}

@media (max-width: 768px) {
  .carousel-img {
    height: 200px;
  }
}

.cta-container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  flex-wrap: wrap;
  gap: 2rem;
  width: 100%;
}

.cta-box {
  flex: 1 1 45%;
  max-width: 380px;
  max-height: 200px;
  background: linear-gradient(135deg, #ffb347 0%, #ffcc33 100%);
  padding: 2.4rem 2rem;
  border-radius: 12px;
  box-shadow: 0 8px 25px rgba(255, 183, 71, 0.4);
  text-align: center;
  color: #3e2e00;
  font-weight: 600;
  transition: box-shadow 0.3s ease;
}

.cta-box:hover {
  box-shadow: 0 10px 40px rgba(255, 183, 71, 0.7);
}

.btn-warning {
  background-color: #f5a623;
  color: #fff;
  padding: 0.7rem 1.5rem;
  border-radius: 8px;
  font-weight: 700;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
  margin-top: 1.3rem;
  display: inline-block;
  text-decoration: none;
  font-size: 1.05rem;
}

.btn-warning:hover {
  background-color: #d48806;
  color: #fff;
}

.featuresSection {
  width: 100%;
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  background-color: #222;
  padding: 2.5rem 0;
  border-radius: 12px;
  margin: 0.2rem 0;
  color: white;
  gap: 1.5rem;
}

.feature-item {
  flex: 1 1 230px;
  display: flex;
  align-items: center;
  gap: 1.2rem;
  background: #333;
  padding: 1.3rem 2.5rem;
  border-radius: 12px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.25);
  transition: background 0.3s ease;
  cursor: default;
}

.feature-item:hover {
  background: #444;
}

.feature-item i {
  font-size: 3rem;
  color: #ffca28;
}

.feature-item h5 {
  font-weight: 700;
  font-size: 1.4rem;
}

.brandsSection {
  width: 100%;
  display: flex;
  justify-content: flex-start;
  flex-wrap: nowrap;
  gap: 0.8rem;
  margin-bottom: 1.5rem;
  overflow-x: auto;
  padding-bottom: 1rem;
  -webkit-overflow-scrolling: touch;
  scroll-behavior: smooth;
}

.brand-item {
  flex: 0 0 auto;
  width: 160px;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 0 8px rgba(0, 0, 0, 0.15);
  cursor: pointer;
  background: white;
  padding: 0.7rem;
  transition: transform 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.brand-item:hover {
  transform: scale(1.15);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
}

.brand-item img {
  width: 140px;
  height: auto;
  display: block;
}

@media (max-width: 768px) {
  .firstSection {
    flex-direction: column;
    gap: 2.5rem;
  }

  .cta-container {
    max-width: 100%;
    flex-direction: row;
    justify-content: center;
  }

  .cta-box {
    flex: 1 1 45%;
    margin: 0 0.5rem;
    padding: 1.5rem 1.2rem;
  }

  .featuresSection {
    flex-direction: column;
    gap: 1.2rem;
  }

  .feature-item {
    flex: 1 1 auto;
    justify-content: center;
  }

  .brandsSection {
    gap: 1.2rem;
  }

  .brand-item img {
    width: 120px;
  }
}

.placeholder-logo {
  width: 140px;
  height: 80px;
  background-color: #eee;
  color: #333;
  font-weight: 600;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 6px;
  font-size: 1rem;
  text-align: center;
}
</style>
