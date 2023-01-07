<template>
    <div class="register">        
        <div class="container bg-dark d-flex flex-column align-items-center mt-5">
            <h3 class="text-white text-center">Register</h3>            
            <form class="mt-5" style="width:100%; max-width:30rem"> 
                <div class="mb-3">
                    <label for="username" class="form-label text-white">Username:</label>
                    <input type="text" v-model="username" class="form-control" id="username" aria-describedby="emailHelp">                    
                </div>
                <div class="mb-3">
                    <label for="mail" class="form-label text-white">Email:</label>
                    <input type="mail" v-model="email" class="form-control" id="mail" aria-describedby="emailHelp">                    
                </div>
                <div class="mb-3">
                    <label for="password" class="form-label text-white">Password:</label>
                    <input type="password" v-model="password" class="form-control" id="password">
                </div>
                <div class="mb-3">
                    <label for="password2" class="form-label text-white">Confirm Password:</label>
                    <input type="password" v-model="re_password" class="form-control" id="password2">
                </div>
                <div v-if="errors">
                    <div class="my-2 text-center "   v-for="error in errors" :key="error">
                        <small class=" small text-white bg-danger p-1 rounded-1">{{error}}</small>
                    </div>
                </div>                
                <div class="mb-3 text-end">
                    <router-link to="sign-in" class="text-primary">Already have an account?</router-link>
                </div>              
                <div class="d-flex justify-content-end">
                    <button @click.prevent="submit" type="submit" class="btn btn-primary">Submit</button>
                </div>
            </form>
        </div>
    </div>
    
</template>

<script>
import axios from 'axios'
export default {
    name:'SignInView',
    data(){
        return {
            username:'',
            email:'',
            password:'',
            re_password:'',
            errors:[]
        }
    },
    methods:{
        submit(){
            this.errors = []
            const user={
                username :this.username,
                email: this.email,
                password : this.password,
                re_password:this.re_password
            }            
            axios
                .post('api/users/',user)
                .then(response=>{
                    console.log(response)
                    this.$router.push('/sign-in')                    
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