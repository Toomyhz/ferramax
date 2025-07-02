<template>
  <main>
    <MyCart :moneda="moneda" />
  </main>
</template>

<script setup>
import MyCart from "@/components/MyCart.vue";
import { defineProps } from "vue";
defineProps({
  moneda: {
    type: String,
  },
});
</script>
