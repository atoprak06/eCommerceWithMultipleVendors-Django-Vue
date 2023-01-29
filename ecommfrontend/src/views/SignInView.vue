<template>
    <div class="signIn">
        <div class="container bg-dark d-flex flex-column align-items-center mt-5">
            <h3 class="text-white text-center">Sign In</h3>            
            <form class="mt-5" style="width:100%; max-width:30rem"> 
                <div class="mb-3">
                    <label for="username" class="form-label text-white">Username:</label>
                    <input v-model="username" type="text" class="form-control" id="username" aria-describedby="emailHelp">                    
                </div>
                <div class="mb-3">
                    <label for="password" class="form-label text-white">Password:</label>
                    <input v-model="password" type="password" class="form-control" id="password">
                </div>
                <div class="mb-3 form-check">
                    <input type="checkbox" class="form-check-input" id="rememberme">
                    <label class="form-check-label text-white" for="rememerme">Remember me</label>
                </div>               
                <div class="mb-3 text-end">
                    <router-link to="register" class="text-primary">Don't have an account?</router-link>
                </div>              
                <div class="d-flex justify-content-end">
                    <button @click.prevent='submit' type="submit" class="btn btn-primary">Submit</button>
                </div>
            </form>
        </div>
    </div>
    
</template>

<script >
import axios from 'axios'
import { useTokenStore } from '../stores/TokensStore'
import { mapStores } from 'pinia'
import { useToast } from "vue-toastification"
import { useRequestStore } from '../stores/RequestStore'

export default {
    name:'SignInView',     
    computed:{
        ...mapStores(useTokenStore)
    },   
    data(){
        return {
            username : '',
            password : '',
        }
    },
    setup(){          
        const toast = useToast()
        const request = useRequestStore()
        return {toast,request}
    },
    methods:{
        async submit(){            
            axios.defaults.headers.common['Authorization'] = ''
            localStorage.removeItem('token')
            const userlog={
                username:this.username,
                password:this.password
            }
            const response = await this.request.postRequest('api/token/login',userlog)
            if(response.status === 200){
                const token = response.data.auth_token                    
                this.tokenStore.setToken(token)                                     
                axios.defaults.headers.common['Authorization'] = this.tokenStore.token                    
                localStorage.setItem('token',token)
                this.tokenStore.getUser                     
                this.$router.push('/')
                this.toast.success('Logged successfully')
            }  
        }
    }
}
</script>