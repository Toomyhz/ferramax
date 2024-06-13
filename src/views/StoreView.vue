<template>
    <div>
        <h1 v-if="text">Resultados de: {{ text }}</h1>
        <h1 v-else-if="categoria">Productos en la Categoría: {{ categoria }}</h1>
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
                }else if (this.text){
                    var NewArray = []
                    for (const key in this.tools) {
                            const tool = this.tools[key];
                            if(tool['NOMBRE'].toUpperCase().includes(this.text.toUpperCase())){
                                NewArray.push(tool)
                            }
                    }
                    return NewArray
                }else{
                    return this.tools
                }
            }
        },
        watch: {
            '$route.query': {
                handler() {
                    this.categoria = this.$route.query.categoria;
                    this.text = this.$route.query.text;
                },
                immediate: true
            }
        },
        created(){
            this.fetchData();
            this.categoria = this.$route.query.categoria;
            this.text = this.$route.query.text
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