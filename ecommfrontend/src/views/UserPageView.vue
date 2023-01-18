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
        <ul>
            <li class="d-flex justify-content-between mt-3">
                <p class="text-white">Product 1 is orderder by SomeUserName</p>
                <p class="text-white">8 hours ago</p>
            </li>
            <hr class="text-white m-0">
            <li class="d-flex justify-content-between mt-3">
                <p class="text-white">Product 2 is orderder by SomeUserName</p>
                <p class="text-white">12 hours ago</p>
            </li>
            <hr class="text-white m-0">
            <li class="d-flex justify-content-between mt-3">
                <p class="text-white">Product 3 is orderder by SomeUserName</p>
                <p class="text-white">23 hours ago</p>
            </li>
            <hr class="text-white m-0">
        </ul>
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
            userProducts:[]
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
    }
}
</script>