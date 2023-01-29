<template>
  <div class="vendors container-fluid d-flex align-items-center flex-column p-5">
    <h3 class="text-warning">Products by {{this.$route.params.username}}</h3>
    <div class="row d-flex">
      <div v-for="product in request.products" :key="product" class="col-lg-3 col-md-4 my-3 col-sm-6">
        <Product :product="product"/>
      </div>
    </div>
    <Paginate
        id="unit"
        v-model = "page"
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
import Paginate from "vuejs-paginate-next";
import { useRequestStore } from '../stores/RequestStore';

export default {
  data(){
    return {
      page:1,        
    }    
  },
  setup(){      
    const request = useRequestStore()   
    return {request}
    },
  props:{searchQuery:''},
  components:{Product,Paginate},
  watch:{  
    '$route.params.username':{
      handler:async function(){        
         await this.newPage(1)
      },
      deep:true,
      immediate:true,   
    },    
    searchQuery:{
      handler:async function(){
          this.page=1
          await this.request.getRequest(`api/products/?created_by__username=${this.$route.params.username}&product_state=active&title=${this.searchQuery}`)      } 
    }
  },
  methods:{
    async newPage(selected){
      await this.request.getRequest(`api/products/?created_by__username=${this.$route.params.username}&product_state=active&page=${selected}&title=${this.searchQuery}`)     
    }
  },
}
</script>