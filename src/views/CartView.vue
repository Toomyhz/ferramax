<template>
  <main>
      <MyCart :moneda="moneda" />
  </main>
</template>

<script setup >
import MyCart from "@/components/MyCart.vue";
</script>
<script>
export default {
  props: {
    moneda: {
      type: String,
    },
  },
}
</script>

