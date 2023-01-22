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
import { useToast } from "vue-toastification"

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
      products:[],
      productsHolder:[]
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
  watch:{
    searchQuery:{
      handler:function(){
        if(this.searchQuery === ''){
          this.products = this.productsHolder
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
    }
  },
  created(){
    axios 
        .get('api/products')
        .then(response=>{
          if (response.status === 200){
            this.products=response.data
            this.productsHolder=this.products
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
</script>
