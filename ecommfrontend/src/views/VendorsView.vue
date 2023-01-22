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
import { useToast } from "vue-toastification"
export default {
  data(){
    return {
      vendor:{},
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
  props:{searchQuery:''},
  components:{Product},
  watch:{  
    '$route.params.username':{
      handler: function(username){
        axios.get(`api/vendors/?username=${username}`)
            .then(response=>{ 
              if (response.data[0]){             
                this.vendor=response.data[0]
                this.productsHolder=this.vendor.products  
              }
              else{
                this.toast.error(`There is no ${username} called Vendor`)
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