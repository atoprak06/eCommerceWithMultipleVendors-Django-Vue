<template>
  <div class="home">
    <div class="container-fluid bg-dark">
      <h3 class="text-warning text-center mt-3">New Products</h3>
      <div class="p-5 row d-flex">
        <div v-for="product in products" :key="product.id" class="my-3 col-lg-3 col-md-4 col-sm-6">
          <Product :product="product"/>
        </div>                 
      </div>
    </div>
    
  </div>
</template>

<script>
import axios from 'axios'
import Product from '../components/Product.vue'

export default {
  name: 'HomeView',
  components: { 
    Product   
  },
  data(){
    return {
      products:[]
    }
  },
  created(){
    axios 
        .get('api/products')
        .then(response=>{
          this.products=response.data
        })
  }

}
</script>
