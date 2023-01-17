<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="/">Ecommerce</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item dropdown">
                         <a class="nav-link dropdown-toggle" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            Categories
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <li v-for="category in categories" :key="category.id">
                                <router-link class="dropdown-item" :to="{name:'categories',params:{title:category.title,id:category.id}}">{{category.title}}</router-link>
                            </li>                        
                        </ul>
                    </li> 
                    <li class="nav-item">
                        <router-link class="nav-link" :to="{name:'about'}">About</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" :to="{name:'contact'}">Contact Us</router-link>
                    </li>             
                </ul>
                <form @keyup.prevent="$emit('search',searchQuery)" class="d-flex">
                    <input @keydown.enter.prevent @click.prevent class="form-control me-2" type="text" v-model="searchQuery" placeholder="Search" aria-label="Search">
                </form>
                <ul v-if="!tokenStore.isAuthenticated" class="navbar-nav ms-auto my-2 mb-lg-0">
                    <li class="nav-item">
                        <router-link class="nav-link" :to="{name:'signin'}">Sign in</router-link>
                    </li>
                    <li class="nav-item d-none d-xxl-block d-xl-block d-lg-block">
                        <p class="nav-link text-white">|</p>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" :to="{name:'register'}">Register</router-link>
                    </li>              
                </ul>
                <ul v-else class="navbar-nav ms-auto my-2 mb-lg-0">
                    <li class="nav-item">
                        <router-link class="nav-link" :to="{name:'userpage'}">{{tokenStore.user.username}}</router-link>                        
                    </li>
                    <li>
                        <button @click.prevent="logout" class="btn btn-danger">logout</button>
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
import axios from 'axios'
export default {
    name:'Navbar',
    setup(){
        const tokenStore = useTokenStore()        
       return {tokenStore}         
    },
    data(){
        return {
            categories:[],
            searchQuery:''
        }
    },
    methods:{
        logout(){            
            this.tokenStore.removeToken
            window.location.reload()
        }
    },
    created(){
        axios.get('api/categories')
            .then(response=>this.categories=response.data)
    }
}
</script>
