<template>
  <div class="vendors p-5 d-flex row">
    <div v-for="product in vendor.products" :key="product" class="col-lg-3 col-md-4 my-3 col-sm-6">
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
      vendor:{},
      productsHolder:[]
    }    
  },
  props:{searchQuery:''},
  components:{Product},
  watch:{  
    '$route.params.username':{
      handler: function(username){
        axios.get(`api/vendors/?username=${username}`)
            .then(response=>{            
              this.vendor=response.data[0]
              this.productsHolder=this.vendor.products      
            })          
      },
      deep:true,
      immediate:true,   
    },    
    searchQuery:{
      handler:function(){
        if(this.searchQuery === ''){
          this.vendor.products=this.productsHolder
        }
        else{            
         this.vendor.products = this.vendor.products.filter(this.checkQuery)
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
    }
  },
}
</script>