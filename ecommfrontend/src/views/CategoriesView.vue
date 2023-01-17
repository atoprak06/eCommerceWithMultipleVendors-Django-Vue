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
props:{
   searchQuery:'',
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
  },
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
      axios.get(`api/categories/${this.$route.params.id}/`)
        .then(response=>{
          this.products=response.data.products
        })
  }
},
components:{Product},
}  

</script>
