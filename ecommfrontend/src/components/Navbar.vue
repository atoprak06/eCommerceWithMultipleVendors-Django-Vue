<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <router-link class="navbar-brand" to="/">Ecommerce</router-link>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <router-link class="nav-link" to="categories">Categories</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" to="vendors">Vendors</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" to="about">About</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" to="contact">Contact Us</router-link>
                    </li>             
                </ul>
                <form class="d-flex">
                    <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                    <button class="btn btn-outline-success" type="submit">Search</button>
                </form>
                <ul v-if="!isAuthenticated" class="navbar-nav ms-auto my-2 mb-lg-0">
                    <li class="nav-item">
                        <router-link class="nav-link" to="sign-in">Sign in</router-link>
                    </li>
                    <li class="nav-item d-none d-xxl-block d-xl-block d-lg-block">
                        <p class="nav-link text-white">|</p>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" to="register">Register</router-link>
                    </li>              
                </ul>
                <ul v-else-if="isAuthenticated" class="navbar-nav ms-auto my-2 mb-lg-0">
                    <li class="nav-item">
                        <router-link class="nav-link" to="/">{{user.username}}</router-link>
                        
                    </li>
                </ul>
                <router-link to="cart">                    
                    <i class="fa-solid fa-cart-shopping text-white fs-3 ms-3 position-relative">
                        <span style="margin-left:-5px; margin-top:-12px" class=" rounded-circle bg-danger position-absolute small p-1 fs-6">2</span>
                    </i>
                </router-link>

            </div>
        </div>
    </nav>
</template>

<script>
import {useTokenStore} from '../stores/TokensStore'
import {mapState} from 'pinia'
import axios from 'axios'
export default {
    name:'Navbar',
    computed:{
        ...mapState(useTokenStore,['isAuthenticated','user']),              
    },
    data(){
        return {
            errors:[],
            user:{}
        }
    },
    created(){
        this.errors = []
            axios
                .get('api/users/me')
                .then(response=>{
                    this.user=response.data
                })
                .catch(error=> {
                    if (error.response) {
                    // The request was made and the server responded with a status code
                    // that falls out of the range of 2xx
                        for(const property in error.response.data){
                            this.errors.push(`${property}:${error.response.data[property]}`)
                        }                                                
                    } else if (error.request) {
                    // The request was made but no response was received
                    // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
                    // http.ClientRequest in node.js
                    console.log(error.request);                    
                    } else {
                    // Something happened in setting up the request that triggered an Error
                    console.log('Error', error.message);
                    }
                    console.log(error.config);
                });
    },
    methods:{
        getUser(){
            
        }
    }
    
}
</script>