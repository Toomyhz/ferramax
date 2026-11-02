<template>
  <main>
    <MyCart :moneda="moneda" />
  </main>
</template>

<script setup>
import MyCart from "@/components/MyCart.vue";
defineProps({
  moneda: {
    type: String,
  },
});
</script>
