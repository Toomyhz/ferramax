<script setup>
import { RouterView } from 'vue-router'
import MyNavbar from './components/MyNavbar.vue'
</script>
<script>
export default {
    data() {
        return {
            moneda:'USD'
        }
    },
    methods: {
        cambiarMoneda(moneda){
            this.moneda = moneda
        }
    }
}
</script>

<template>
    <MyNavbar :cambioActual=moneda @cambiarMoneda="cambiarMoneda"></MyNavbar>
    <RouterView :moneda="moneda"/>
</template>

<style scoped>
</style>
