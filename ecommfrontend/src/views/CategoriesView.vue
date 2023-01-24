<template>
  <div class="categories container-fluid d-flex align-items-center flex-column p-5">
    <h3 class="text-warning">Category: {{this.$route.params.title}}</h3>
    <div class="row d-flex">
       <div v-for="product in products" :key="product.id" class="my-3 col-lg-3 col-md-4 col-sm-6">
          <Product :product="product"/>
       </div>
    </div>
    <Paginate
        id="unit"
        v-model="page"
        :page-count="pageCount"
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
import axios from 'axios'
import Product from '../components/Product.vue'
import { useToast } from "vue-toastification"
import Paginate from "vuejs-paginate-next";

export default {
data(){
  return {
    products:[],    
    pageCount:1,
    page:1
  }
},
setup(){   
  const options = {
    position: "top-center",
    timeout: 5000,
    closeOnClick: true,
    pauseOnFocusLoss: true,
    pauseOnHover: true,
    draggable: true,
    draggablePercent: 0.6,
    showCloseButtonOnHover: false,
    hideProgressBar: true,
    closeButton: "button",
    icon: true,
    rtl: false
  }       
  const toast = useToast()
  return {options,toast}
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
         await axios.get(`api/products/?category=${this.$route.params.id}&product_state=active&title=${this.searchQuery}`)
            .then(response=>{              
              if (response.status === 200){
                this.pageCount=Math.ceil(response.data['count']/16)
                this.products=response.data.results                  
              }         
            })
            .catch(error=> { 
              if (error.response) { 
                  // The request was made and the server responded with a status code
                  // that falls out of the range of 2xx                  
                  let errorType = `${error.response.status}  ${error.response.statusText}`
                  this.toast.error(errorType,this.options)                       
              } else if (error.request) { 
                  // The request was made but no response was received
                  // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
                  // http.ClientRequest in node.js                   
                  this.toast.error(error.request,this.options);                    
              } else {                       
                  // Something happened in setting up the request that triggered an Error
                  this.toast.error(error.message,this.options);
              }                   
          });        
    }
  }
},
methods:{  
    async newPage(selected){
      await axios 
        .get(`api/products/?category=${this.$route.params.id}&product_state=active&page=${selected}&title=${this.searchQuery}`)
        .then(response=>{          
          if (response.status === 200){
            this.pageCount=Math.ceil(response.data['count']/16)
            this.products=response.data.results            
          }         
        })
        .catch(error=> {
          if (error.response) { 
              // The request was made and the server responded with a status code
              // that falls out of the range of 2xx                  
              let errorType = `${error.response.status}  ${error.response.statusText}`
              this.toast.error(errorType,this.options)                       
          } else if (error.request) { 
              // The request was made but no response was received
              // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
              // http.ClientRequest in node.js                   
              this.toast.error(error.request,this.options);                    
          } else {                       
              // Something happened in setting up the request that triggered an Error
              this.toast.error(error.message,this.options);
          }                   
        });
  }    
},
components:{
  Product,
  Paginate,
}
}  

</script>
