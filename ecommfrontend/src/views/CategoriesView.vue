<template>
  <div class="categories container-fluid d-flex align-items-center flex-column p-5">
    <h3 class="text-warning">Category: {{this.$route.params.title}}</h3>
    <div class="row d-flex">
       <div v-for="product in request.products" :key="product.id" class="my-3 col-lg-3 col-md-4 col-sm-6">
          <Product :product="product"/>
       </div>
    </div>
    <Paginate
        id="unit"
        v-model="page"
        :page-count="request.pageCount"
        :page-range="10"
        :margin-pages="3"
        :initial-page="1"
        :prev-class="'ignore'"
        :next-class="'ignore'"
        :disabled-class="'ignore'"
        :click-handler="newPage"
        
    />    
  </div>
</template>

<script>
import Product from '../components/Product.vue'
import { useRequestStore} from '../stores/RequestStore'
import Paginate from "vuejs-paginate-next";

export default {
data(){
  return {   
    page:1
  }
},
setup(){   
  const request = useRequestStore()
  return {request}
},
props:{
   searchQuery:'',
},
watch:{  
  '$route.params.id':{
    handler: async function(){      
      await this.newPage(1)      
    },
    deep:true,
    immediate:true
  },
  searchQuery:{
      handler:async function(){
        this.page=1
        await this.request.getRequest(`api/products/?category=${this.$route.params.id}&product_state=active&title=${this.searchQuery}`)
    }
  }
},
methods:{  
    async newPage(selected){
      await this.request.getRequest(`api/products/?category=${this.$route.params.id}&product_state=active&page=${selected}&title=${this.searchQuery}`)     
  }    
},
components:{
  Product,
  Paginate,
}
}  

</script>
