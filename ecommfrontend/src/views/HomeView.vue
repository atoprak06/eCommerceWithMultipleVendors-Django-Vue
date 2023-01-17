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
  props:{
    searchQuery:'',
  },
  data(){
    return {
      products:[]
    }
  },
  watch:{
    searchQuery:{
      handler:function(){
        if(this.searchQuery === ''){
          this.getProducts()
        }
        else{
         this.products = this.products.filter(this.checkQuery)
        }        
      }
    }
  },
  methods:{
    checkQuery(product){
      if (product.title.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
       product.created_by.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
       product.category.toLowerCase().includes(this.searchQuery.toLowerCase()) ){
        return product
      }      
    },
    getProducts(){
      axios 
        .get('api/products')
        .then(response=>{
          this.products=response.data
        })
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
