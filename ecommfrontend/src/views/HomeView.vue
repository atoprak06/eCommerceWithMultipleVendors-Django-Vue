<template>
  <div class="home">
    <div class="container-fluid mt-3 bg-dark d-flex flex-column align-items-center p-5">
      <h3 class="text-warning">Home</h3>
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
    
  </div>
</template>

<script>
import Product from '../components/Product.vue'
import { useRequestStore } from '../stores/RequestStore'
import Paginate from "vuejs-paginate-next"

export default {
  name: 'HomeView',
  components: { 
    Product,
    Paginate 
  },
  props:{
    searchQuery:'',
  },
  data(){
    return {    
      page:1,
    }
  },
  setup(){     
    const request = useRequestStore()
    return {request}
  },
  watch:{
    searchQuery:{      
      handler:async function(){ 
        this.page=1
        await this.request.getRequest(`api/products/?category=&product_state=active&title=${this.searchQuery}`)        
      }
    }
  },
  methods:{
    async newPage(selected=1){
      await this.request.getRequest(`api/products/?category=&product_state=active&page=${selected}&title=${this.searchQuery}`)
    }   
  },  
  async created(){
    await this.request.getRequest('api/products/?category=&product_state=active')        
  }
}
</script>
