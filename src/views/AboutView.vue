<template>
  <div>
    <article v-for="tool in tools" :key="tool.ID_HERRAMIENTA" >
      {{ tool.NOMBRE }}
    </article>
  </div>
</template>
<script>
  import axios from 'axios';

  export default {
    data(){
      return{
        tools:[]
      };
    },
    mounted(){
      this.fetchData();
    },
    methods:{
      async fetchData(){
        try{
          const response = await
          axios.get('http://127.0.0.1:5000/tools/');
          this.tools = response.data['TOOLS'];
        } catch(error){
          console.error('Error fetching data: ', error)
        }
      }
    }
  }
</script>