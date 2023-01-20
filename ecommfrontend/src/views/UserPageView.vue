<template>
    <div class="user-page table-responsive container mt-5">        
        <h5 class="text-warning">My Products:</h5>
        <table class="table table-hover">
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
        <h5 class="text-warning">Shopping History:</h5>
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
                    <td>${{order.orderTotalPrice}}</td>
                    <td><button class="btn btn-primary">Details</button></td>
                </tr>
            </tbody>
        </table>
        <h5 class="text-warning">Sold Products:</h5>
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
                    <td>${{order.orderTotalPrice}}</td>
                    <td><button class="btn btn-primary">Details</button></td>
                </tr>
            </tbody>
        </table>
        <h5 class="text-success text-end">My Balance: $1244.66</h5>
    </div>
</template>

<script>
import axios from 'axios'
import moment from 'moment';
export default {
    name:'UserPageView',
    data(){
        return {
            userProducts:[],
            myOrders:[],
            soldProducts:[]
        }
    },
    methods:{
        getTime(time){
            return moment(time).fromNow()
        }
    },  
    created(){
        axios.get('api/products/my_products')
             .then(response=>{                
                this.userProducts=response.data
             })
        axios.get('api/order')
             .then(response=>{
                this.myOrders = response.data
             })
        axios.get('api/order/orderedProducts/')
             .then(response=>{
                console.log(response.data)
             })
    }
}
</script>