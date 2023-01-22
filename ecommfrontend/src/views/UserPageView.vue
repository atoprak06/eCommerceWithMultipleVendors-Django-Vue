<template>
    <div class="user-page table-responsive container mt-5"> 
        <div class="d-flex justify-content-center align-items-center gap-3">
            <h5 class="text-warning">My Products:</h5>
            <button class="btn" :class="[isActive?'btn-warning':'btn-success']" @click.prevent="isActive=!isActive"><small v-if="isActive">Hide Products</small><small v-else>Show Products</small></button>            
        </div>
        <table class="table table-hover" :class="[isActive?'':'d-none']">
            <thead class="table-dark">
                <tr>
                    <th scope="col">Product id</th>
                    <th scope="col">Product Title</th>
                    <th scope="col">Product Price</th>
                    <th scope="col">Date Added</th>
                    <th scope="col">Status</th>
                    <th></th>
                </tr>
            </thead>
            <tbody class="table-dark">
                <tr v-for="product in userProducts" :key="product.id">
                    <th scope="row">{{product.id}}</th>
                    <td>{{product.title}} </td>
                    <td>${{product.price}}</td>
                    <td>{{getTime(product.created_at)}}</td>
                    <td v-if="product.product_state==='active'" class="text-success">{{product.product_state}}</td>
                    <td v-if="product.product_state==='deactive'" class="text-danger">{{product.product_state}}</td>
                    <td><router-link :to="{name: 'product', params: { slug:product.slug, id: product.id }}" class="btn btn-danger">Show/Edit</router-link></td>
                </tr>
            </tbody>
        </table>     
        <router-link class="btn btn-danger" :to="{name:'newproduct'}">Add new product</router-link>
        <hr>
        <h5 class="text-warning">Your Orders:</h5>
        <table class="table table-hower">
            <thead class="table-dark">
                <tr>
                    <th scope="col">Order id</th>
                    <th scope="col">Date Ordered</th>
                    <th scope="col">Total</th>
                    <th></th>
                </tr>
            </thead>
            <tbody class="table-dark">
                <tr v-for="order in myOrders" :key="order">
                    <td>{{order.id}}</td>
                    <td>{{getTime(order.created_at)}}</td>
                    <td class="text-danger">${{order.orderTotalPrice}}</td>
                    <td colspan="3"><Order :order="order"/></td>
                </tr>
                <tr>
                    <td class="text-end fs-4 text-danger" colspan="6">Sum: ${{ordersTotal}}</td>
                </tr>
            </tbody>
        </table>
        <h5 class="text-warning">Sold Products:</h5>
        <table class="table table-hower">
            <thead class="table-dark">
                <tr>
                    <th scope="col">Order id</th>
                    <th scope="col">Ordered By</th>
                    <th scope="col">Product</th>
                    <th scope="col">Quantity</th>
                    <th scope="col">Date Ordered</th>
                    <th scope="col">Total</th>
                </tr>
            </thead>
            <tbody class="table-dark">
                <tr v-for="product in soldProducts" :key="product">
                    <td>{{product.order.id}}</td>
                    <th><router-link class="text-decoration-none" :to="{name:'vendors',params:{username:product.order.customer}}"> {{product.order.customer}}</router-link></th>
                    <td><router-link class="text-decoration-none" :to="{name:'product',params:{slug:product.product.slug,id:product.product.id}}">{{product.product.title}}</router-link></td>
                    <td>{{product.quantity}}</td>
                    <td>{{getTime(product.created_at)}}</td>
                    <td class="text-success">${{product.productTotalPrice}}</td>
                </tr>
                <tr>
                    <td class="text-end fs-4 text-success" colspan="6">Sum: ${{productTotal}}</td>
                </tr>
            </tbody>
        </table>
        <h5 class="fs-3" :class="[balance>=0 ? 'text-success' : 'text-danger', 'text-end']">My Balance: ${{balance}}</h5>
    </div>
</template>

<script>
import axios from 'axios'
import moment from 'moment'
import Order from '../components/Order.vue'
import { useToast } from "vue-toastification"

export default {
    name:'UserPageView',
    data(){
        return {
            userProducts:[],
            myOrders:[],
            soldProducts:[],
            balance:0,
            isActive:false,           
            ordersTotal : 0,
            productTotal : 0
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
    components:{
        Order
    },
    methods:{
        getTime(time){
            return moment(time).fromNow()
        }       
    },  
    async created(){
        await axios.get('api/products/my_products')
             .then(response=>{     
                this.userProducts=response.data
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
        await axios.get('api/order')
             .then(response=>{
                this.myOrders = response.data                
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
        await axios.get('api/order/orderedProducts/')
             .then(response=>{
                this.soldProducts=response.data
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
        this.ordersTotal = 0
        this.productTotal = 0
        this.myOrders.forEach(order => {                              
            this.ordersTotal += order.orderTotalPrice                
        });
        this.soldProducts.forEach(product=>{
            this.productTotal += product.productTotalPrice
        })
        this.balance = this.productTotal - this.ordersTotal
    }
}
</script>