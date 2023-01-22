<template>
  <div class="cart">
    <section class="h-100 h-custom">
      <div class="container py-5 h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
          <div class="col-12">
            <div class="card card-registration card-registration-2" style="border-radius: 15px;">
              <div class="card-body p-0">
                <div class="row g-0">
                  <div class="col-lg-8">
                    <div class="p-5">
                      <div class="d-flex justify-content-between align-items-center mb-5">
                        <h1 class="fw-bold mb-0 text-black">Shopping Cart</h1>
                        <h6 class="mb-0 text-muted">{{cartStore.getCartTotal}} items</h6>
                      </div>
                      <hr class="my-4">                     

                      
                      <div class="product" v-for="product in cartStore.cart" :key="product">
                        <div class="row mb-4 d-flex justify-content-between align-items-center">
                          <div class="col-md-2 col-lg-2 col-xl-2">
                            <img
                              :src="product.image_url"
                              class="img-fluid rounded-3" alt="Cotton T-shirt">
                          </div>
                          <div class="col-md-3 col-lg-3 col-xl-3">
                            <h6 class="text-muted">{{product.title}}</h6>
                            <h6 class="text-black mb-0">{{product.category}}</h6>
                          </div>
                          <div class="col-md-3 col-lg-3 col-xl-2 d-flex">
                            <button class="btn btn-link px-2"
                              @click.prevent="cartStore.removeProduct(product)">
                              <i class="fas fa-minus"></i>
                            </button>

                            <input id="form1" min="0" name="quantity" :value="product.quantity" type="number"
                              class="form-control form-control-sm" style="min-width:4rem"/>

                            <button class="btn btn-link px-2"
                              @click.prevent="cartStore.addToCart(product)">
                              <i class="fas fa-plus"></i>
                            </button>
                          </div>
                          <div class="col-md-3 col-lg-2 col-xl-2 offset-lg-1">
                            <h6 class="mb-0">${{product.priceTotal}}</h6>
                          </div>
                          <div class="col-md-1 col-lg-1 col-xl-1 text-end">
                            <i @click.prevent="cartStore.deleteProduct(product)" class="fas fa-times"></i>
                          </div>
                        </div>
                        <hr class="my-4">
                      </div>                    

                      <div class="pt-5">
                        <h6 class="mb-0">
                          <router-link class="text-decoration-none" :to="{name:'home'}">
                            <i class="fas fa-long-arrow-alt-left me-2"></i>Back to shop
                          </router-link> 
                        </h6>
                      </div>
                    </div>
                  </div>
                  <div class="col-lg-4 bg-grey">
                    <div class="p-5">
                      <h3 class="fw-bold mb-5 mt-2 pt-1">Summary</h3>
                      <hr class="my-4">

                      <div class="d-flex justify-content-between mb-4">
                        <h5 class="text-uppercase">items {{cartStore.getCartTotal}}</h5>
                        <h5>$ {{cartStore.getCartPriceTotal}}</h5>
                      </div>

                      <h5 class="text-uppercase mb-3">Shipping</h5>

                      <div class="mb-4 pb-2">
                        <select class="select">
                          <option value="1">Standard-Delivery- €5.00</option>
                          <option value="2">Two</option>
                          <option value="3">Three</option>
                          <option value="4">Four</option>
                        </select>
                      </div>

                      <h5 class="text-uppercase mb-3">Give code</h5>

                      <div class="mb-5">
                        <div class="form-outline">
                          <input type="text" id="form3Examplea2" class="form-control form-control-lg" />
                          <label class="form-label" for="form3Examplea2">Enter your code</label>
                        </div>
                      </div>

                      <hr class="my-4">

                      <div class="d-flex justify-content-between mb-5">
                        <h5 class="text-uppercase">Total price</h5>
                        <h5>$ {{cartStore.getCartPriceTotal}}</h5>
                      </div>
                      <button @click.prevent="buy" type="button" class="btn btn-dark btn-block btn-lg"
                        data-mdb-ripple-color="dark">Buy</button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>


<script>
import {useCartStore} from '../stores/CartStore'
import {useTokenStore} from '../stores/TokensStore'
import { useToast } from "vue-toastification"
import axios from 'axios'
export default {
  setup(){
    const cartStore = useCartStore()
    const tokenStore = useTokenStore()
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
    return {cartStore , tokenStore,options,toast}
  },
  data(){
    return{
      order :{}
    }
  },
  methods:{
    async buy(){
      if (this.cartStore.cart.length>0){
        let data = {customer:this.tokenStore.user,orderTotalPrice:this.cartStore.getCartPriceTotal,cartProducts:this.cartStore.cart}      
        await axios.post('api/order/',data)
              .then(response=>{
                if (response.status === 200){
                  this.cartStore.removeCart
                  this.toast.success('Order is success',this.options)
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
      else{this.toast.warning('Add products first',this.options)}     
    }
  }  
}
</script>

<style scoped>
  .fas{
    cursor: pointer;    
  }
</style>
