<template>
  <div class="categories d-flex row p-5">
    <div v-for="product in products" :key="product.id" class="my-3 col-lg-3 col-md-4 col-sm-6">
       <Product :product="product"/>
    </div>    
  </div>
</template>

<script>
import axios from 'axios'
import Product from '../components/Product.vue'
export default {
data(){
  return {
    products:[], 
  }
},
watch:{  
  '$route.params.id':{
    handler: function(id){
      axios.get(`api/categories/${id}/`)
        .then(response=>{
          this.products=response.data.products
        })
    },
    deep:true,
    immediate:true
  }
},
components:{Product},
}  

</script>
