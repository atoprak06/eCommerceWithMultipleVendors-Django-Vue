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
                <div v-if="errors">
                    <div class="my-2 text-center "   v-for="error in errors" :key="error">
                        <small class=" small text-white bg-danger p-1 rounded-1">{{error}}</small>
                    </div>
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

export default {
    name:'SignInView', 
    created(){        
        const token = localStorage.getItem('token')              
        if(token){
            axios.defaults.headers.common['Authorization'] = 'Token ' + token
        }else{
            axios.defaults.headers.common['Authorization'] = ''
        }
    },
    computed:{
        ...mapStores(useTokenStore)
    },   
    data(){
        return {
            username : '',
            password : '',
            errors : []
        }
    },
    methods:{
        submit(){            
            this.errors = []
            axios.defaults.headers.common['Authorization'] = ''
            localStorage.removeItem('token')
            const userlog={
                username:this.username,
                password:this.password
            }
            axios
                .post('api/token/login',userlog)
                .then(response=>{                    
                    const token = response.data.auth_token
                    console.log(token)
                    this.tokenStore.setToken
                    console.log(this.tokenStore.token)                 
                    axios.defaults.headers.common['Authorization'] = 'Token' + token
                    localStorage.setItem('token',token)
                    this.$router.push('/')

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


        }
    }
}
</script>