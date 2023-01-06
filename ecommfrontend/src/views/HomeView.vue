<template>
  <div class="home">
    <div class="container-fluid bg-dark">
      <h3 class="text-warning text-center">New Products</h3>
      <div class="p-5 row d-flex">
        <div v-for="product in 8" :key="product" class="my-3 col-lg-3 col-md-4 col-sm-6">
          <Product/>
        </div>                 
      </div>
    </div>
    
  </div>
</template>

<script>

import Product from '../components/Product.vue'

export default {
  name: 'HomeView',
  components: { Product
   
  }
}
</script>
