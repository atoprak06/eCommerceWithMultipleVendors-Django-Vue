<template>
    <div class="product row d-flex justify-content-center pt-3 mx-auto mb-5" style="max-width:40rem; width:100%; height:auto">       
        <div class="col-12 mt-5 d-flex justify-content-center align-items-center ">    
            <div class="card p-3" style="width:100%; height:auto">                
                <div class="d-flex justify-content-between align-items-center row ">
                    <div class="col-6">                        
                        <h5 class="text-uppercase mb-0">{{product.title}}</h5>
                        <p class="main-heading mt-2">added by <router-link :to="{name:'vendors',params:{username:product.created_by}}" class="text-success">{{product.created_by}}</router-link>, <span class="text-danger">{{getTime(product.created_at)}}</span></p>
                        <p class="text-danger">${{product.price}}</p>                        
                        <small class="text-uppercase bg-dark text-white rounded-3 p-1">{{product.category}}</small>
                    </div>
                    <div class="image col-6">
                        <img :src="product.image_url" style="width:100%; max-height:18rem; object-fit:contain; height:auto;">
                    </div>
                </div>                               
                <p class="col-6">{{product.description}} </p>                
                <button @click.prevent="cartStore.addToCart(product); messageStore.showMessage('Added to Cart')" class="btn btn-danger">Add to cart</button>              
            </div>            
        </div>
        <form @submit.prevent="submit" v-if="tokenStore.user.username===product.created_by" class="d-flex flex-column col-6 justify-content-center m-3">
                <h3 class="text-warning">Edit your Product</h3>
                <div class="mb-3">
                    <label for="product_name" class="form-label text-white">Title:</label>
                    <input v-model="product.title" type="text" class="form-control" id="product_name">                    
                </div>
                <div class="mb-3">
                    <label for="product_category" class="form-label text-white">Category:</label>
                    <select v-model="product.category" class="form-select" id="product_category">
                        <option value="Watch">Watch</option>
                        <option value="Computer">Computer</option>
                    </select>                   
                </div>
                <div class="mb-3">
                    <label for="product_desc" class="form-label text-white">Description:</label>
                    <textarea v-model="product.description"  rows="4" class="form-control" id="product_desc"/>                    
                </div>
                <div class="mb-3">
                    <label for="product_price" class="form-label text-white">Price:</label>
                    <input v-model="product.price" type="number" step="0.01" rows="4" class="form-control" id="product_price"/>                    
                </div>
                <div class="mb-3">
                    <label for="product_status" class="form-label text-white">Status:</label>
                    <select v-model="product.product_state" class="form-control" id="product_status">
                        <option value="active">Active</option>
                        <option value="deactive">Deactive</option>

                    </select>                    
                </div>                                           
            <button type="submit" class="btn btn-primary" @click.prevent="messageStore.showMessage('Product Edited')">Edit</button>            
        </form>   
    </div>
</template>

<script>
import axios from 'axios'
import {useTokenStore} from '../stores/TokensStore'
import {useCartStore} from '../stores/CartStore'
import {useMessageStore} from '../stores/messageStore'

import moment from 'moment'
export default {
    data(){
        return {
            product:{},            
        }
    },
    setup(){
        const tokenStore = useTokenStore()
        const cartStore = useCartStore()
        const messageStore = useMessageStore()
        return {tokenStore,cartStore,messageStore}
    },
    mounted(){
        axios.get(`api/products/${ this.$route.params.id }`)
            .then(response=>{
                this.product = response.data
            })
    },
    methods:{
        submit(){
            axios.patch(`api/products/${ this.$route.params.id }/`,this.product)              
        },
        getTime(created_at){
            return moment(created_at).fromNow()
        }
    }
}
</script>