<template>
    <div>
        <h1 v-if="categoria">Productos en la Categoría: {{ categoria }}</h1>
        <h1 v-else>Tienda</h1>
      <article v-for="tool in productosFiltrados" :key="tool.ID_HERRAMIENTA" >
        {{ tool.NOMBRE }}
        {{ tool.CATEGORIA }}
      </article>
    </div>
</template>
  <script>
    import axios from 'axios';
  
    export default {

        data(){
            return{
                tools:[],
                categoria: "",
                text:""
            };
        },
        computed:{
            productosFiltrados(){
                if (this.categoria) {
                    var tools_filter = this.tools.filter(tool => tool.CATEGORIA == this.categoria);
                    return tools_filter
                }else{
                    return this.tools
                }
            }
        },
        watch: {
            '$route.query': {
                handler() {
                    this.categoria = this.$route.query.categoria;
                },
                immediate: true
            }
        },
        created(){
            this.fetchData();
            this.categoria = this.$route.query.categoria;
            this.text = this.$route.query.text
            console.log(this.text)
        },
        methods:{
            async fetchData(){
                try{
                    const response = await
                    axios.get('http://127.0.0.1:5000/tools/');
                    this.tools = response.data['TOOLS'];
                } catch(error) {
                    console.error('Error fetching data: ', error)
                }
            },
      }
    }
  </script>