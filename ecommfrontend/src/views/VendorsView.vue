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
      vendor:{}
    }
  },
  components:{Product},
  watch:{  
    '$route.params.username':{
      handler: function(username){
        axios.get(`api/vendors/?username=${username}`)
            .then(response=>{            
              this.vendor=response.data[0]          
            })
      },
      deep:true,
      immediate:true
    }
  }
}
</script>