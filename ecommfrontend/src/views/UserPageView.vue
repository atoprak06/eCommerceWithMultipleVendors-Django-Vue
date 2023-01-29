<template>
    <div class="user-page table-responsive container mt-5"> 

        <div class="d-flex justify-content-center align-items-center gap-3">
            <h5 class="text-warning">My Products:</h5>
            <button v-if="userProducts.length>0" class="btn" :class="[isActive?'btn-warning':'btn-success']" @click.prevent="isActive=!isActive"><small v-if="isActive">Hide Products</small><small v-else>Show Products</small></button>            
        </div>
        <template v-if="userProducts.length>0">
            <table class="table table-hover" v-show="isActive">
                <thead class="table-dark">
                    <tr>
                        <th >Product id</th>
                        <th scope="col">Product Title</th>
                        <th scope="col">Product Price</th>
                        <th scope="col">Date Added</th>
                        <th scope="col">Status</th>
                        <th scope="col"></th>
                    </tr>
                </thead>
                <tbody class="table-dark">
                    <tr v-for="product in userProducts" :key="product.id">
                        <th scope="row">{{product.id}}</th>
                        <td> {{product.title}} </td>
                        <td>${{product.price}}</td>
                        <td>{{getTime(product.created_at)}}</td>
                        <td :class="[product.product_state==='active'?'text-success':'text-danger']">{{product.product_state}}</td>                    
                        <td><router-link :to="{name: 'product', params: { slug:product.slug, id: product.id }}" class="btn btn-danger">Show/Edit</router-link></td>
                    </tr>                         
                </tbody>           
            </table>
            <Paginate
                v-show="isActive"
                id="unit"                    
                :page-count="pageCountProducts"
                :page-range="5"
                :margin-pages="2"
                :initial-page="1"
                :prev-class="'ignore'"
                :next-class="'ignore'"
                :disabled-class="'ignore'"
                :click-handler="newPageProducts"
            />
        </template>
        <template v-else><h3 class="text-warning">You have no products yet!</h3></template>       
        <router-link class="btn btn-danger" :to="{name:'newproduct'}">Add new product</router-link>
        <hr>

        <div class="d-flex justify-content-center align-items-center gap-3">
            <h5 class="text-warning">My Orders:</h5>
            <button v-if="myOrders.length>0" class="btn" :class="[isActiveOrders?'btn-warning':'btn-success']" @click.prevent="isActiveOrders=!isActiveOrders"><small v-if="isActiveOrders">Hide Orders</small><small v-else>Show Orders</small></button>            
        </div>
        <template v-if="myOrders.length>0">
            <table class="table table-hower" v-show="isActiveOrders">
                <thead class="table-dark">
                    <tr>
                        <th scope="col">Order id</th>
                        <th scope="col">Date Ordered</th>
                        <th scope="col">Total</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody class="table-dark">
                    <template v-if="myOrders.length>0">
                        <tr v-for="order in myOrders" :key="order">
                            <td>{{order.id}}</td>
                            <td>{{getTime(order.created_at)}}</td>
                            <td class="text-danger">${{order.orderTotalPrice}}</td>
                            <td colspan="3"><Order :order="order"/></td>
                        </tr>
                    </template>                    
                    <tr>
                        <td class="text-end fs-4 text-danger" colspan="6">Sum: ${{ordersTotal}}</td>
                    </tr>
                </tbody>
            </table>
            <Paginate
                v-show="isActiveOrders"
                id="unit2"                    
                :page-count="pageCountOrders"
                :page-range="10"
                :margin-pages="3"
                :initial-page="1"
                :prev-class="'ignore'"
                :next-class="'ignore'"
                :disabled-class="'ignore'"
                :click-handler="newPageOrders"
            />
        </template>
        <template v-else><h3 class="text-warning">You have no orders yet!</h3></template>
        <hr>  

        <div class="d-flex justify-content-center align-items-center gap-3">
            <h5 class="text-warning">My Sold Products:</h5>
            <button v-if="soldProducts.length>0" class="btn" :class="[isActiveSoldProducts?'btn-warning':'btn-success']" @click.prevent="isActiveSoldProducts=!isActiveSoldProducts"><small v-if="isActiveSoldProducts">Hide Sold Products</small><small v-else>Show Sold Products</small></button>            
        </div>
        <template v-if="soldProducts.length>0" >
            <table class="table table-hower" v-show="isActiveSoldProducts">
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
                    <template v-if="soldProducts">
                        <tr v-for="product in soldProducts" :key="product">
                            <td>{{product.order.id}}</td>
                            <th><router-link class="text-decoration-none" :to="{name:'vendors',params:{username:product.order.customer}}"> {{product.order.customer}}</router-link></th>
                            <td><router-link class="text-decoration-none" :to="{name:'product',params:{slug:product.product.slug,id:product.product.id}}">{{product.product.title}}</router-link></td>
                            <td>{{product.quantity}}</td>
                            <td>{{getTime(product.created_at)}}</td>
                            <td class="text-success">${{product.productTotalPrice}}</td>
                        </tr>                       
                    </template>                    
                    <tr>
                        <td class="text-end fs-4 text-success" colspan="6">Sum: ${{productTotal}}</td>
                    </tr>
                </tbody>
            </table>
            <Paginate
                v-show="isActiveSoldProducts"
                id="unit3"                    
                :page-count="pageCountSoldProducts"
                :page-range="10"
                :margin-pages="3"
                :initial-page="1"
                :prev-class="'ignore'"
                :next-class="'ignore'"
                :disabled-class="'ignore'"
                :click-handler="newPageSoldProducts"
            />              
        </template>
        <template v-else><h3 class="text-warning">You have no sold products yet!</h3></template>
        <hr>
        
        <h5 class="fs-3" :class="[balance>=0 ? 'text-success' : 'text-danger', 'text-end']">My Balance: ${{balance}}</h5>
    </div>
</template>

<script>
import axios from 'axios'
import moment from 'moment'
import Order from '../components/Order.vue'
import { useToast } from "vue-toastification"
import Paginate from "vuejs-paginate-next"
import { useRequestStore } from '../stores/RequestStore'


export default {
    name:'UserPageView',
    data(){
        return {
            userProducts:[],
            myOrders:[],
            soldProducts:[],
            balance:0,
            isActive:true,
            isActiveOrders:true,
            isActiveSoldProducts:true, 
            ordersTotal : 0,
            productTotal : 0,
            pageCountProducts:1,
            pageCountOrders:1,
            pageCountSoldProducts:1,
        }
    },
    setup(){ 
    const toast = useToast()
    const request = useRequestStore()
    return {toast,request}
    },
    components:{
        Order,Paginate
    },
    methods:{
        getTime(time){
            return moment(time).fromNow()
        },
        async newPageOrders(selected=1){
            const response = await this.request.getRequestResponse(`api/order/?page=${selected}`)
            if(response.status === 200 || response.status === 201){
                this.pageCountOrders = Math.ceil(response.data['count']/16)
                this.myOrders = response.data['results']
            }
        },
        async newPageProducts(selected=1){
            const response = await this.request.getRequestResponse(`api/products/my_products/?page=${selected}`)
            if(response.status === 200 || response.status === 201){
                this.pageCountProducts = Math.ceil(response.data['count']/16)
                this.userProducts = response.data['results']
            }                  
        },
        async newPageSoldProducts(selected=1){
            const response = await this.request.getRequestResponse(`api/order/orderedProducts/?page=${selected}`)
            if(response.status === 200 || response.status === 201){
                this.pageCountSoldProducts = Math.ceil(response.data['count']/16)
                this.soldProducts = response.data['results']
            }
        }
    },  
    created(){
        this.newPageProducts()
        this.newPageOrders()
        this.newPageSoldProducts()

        this.ordersTotal = 0
        this.productTotal = 0
        if(this.myOrders.length>0){
            this.myOrders.forEach(order => {                              
                this.ordersTotal += order.orderTotalPrice                
            });
        }
        if(this.soldProducts.length>0){
            this.soldProducts.forEach(product=>{
                this.productTotal += product.productTotalPrice
            })
        }
        this.balance = this.productTotal - this.ordersTotal
    }
}
</script>