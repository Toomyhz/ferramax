<script setup>
</script>

<template>
  <main>
    <section class="start">
      <div class="first">
        Imagen grande
      </div>
      <div class="second">
        <div>Arriba</div>
        <div>Abajo</div>
      </div>
    </section>
  </main>
</template>
<style scoped>
.start{
  width: 90%;
  height: 450px;
  display: flex;
  margin: 50px auto;
  justify-content: space-between;
  .first{
    width:60%;
    background-color: aqua;
    }
    .second{
      width:35%;
      background-color: yellow;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      div{
        background-color: blue;
        height: 40%;
        width: 100%;
      }
  }
}
</style>