<template>
    <div class="register">        
        <div class="container bg-dark d-flex flex-column align-items-center mt-5">
            <h3 class="text-white text-center">Register</h3>            
            <form class="mt-5" style="width:100%; max-width:30rem"> 
                <div class="mb-3">
                    <label for="username" class="form-label text-white">Username:</label>
                    <input type="text" v-model="username" class="form-control" id="username">                    
                </div>
                <div class="mb-3">
                    <label for="mail" class="form-label text-white">Email:</label>
                    <input type="mail" v-model="email" class="form-control" id="mail">                    
                </div>
                <div class="mb-3">
                    <label for="firstname" class="form-label text-white">First Name:</label>
                    <input type="text" v-model="first_name" class="form-control" id="firstname">                    
                </div>
                <div class="mb-3">
                    <label for="lastname" class="form-label text-white">Last Name:</label>
                    <input type="text" v-model="last_name" class="form-control" id="lastname">                    
                </div>
                <div class="mb-3">
                    <label for="country" class="form-label text-white">Country:</label>
                    <input type="text" v-model="user_country" class="form-control" id="country">                    
                </div>
                <div class="mb-3">
                    <label for="city" class="form-label text-white">City:</label>
                    <input type="text" v-model="user_city" class="form-control" id="city">                    
                </div>
                <div class="mb-3">
                    <label for="address" class="form-label text-white">Address:</label>
                    <input type="text" v-model="user_address" class="form-control" id="address">                    
                </div>
                <div class="mb-3">
                    <label for="age" class="form-label text-white">Age</label>
                    <input type="text" v-model="user_age" class="form-control" id="age">                    
                </div>
                <div class="mb-3">
                    <label for="password" class="form-label text-white">Password:</label>
                    <input type="password" v-model="password" class="form-control" id="password">
                </div>
                <div class="mb-3">
                    <label for="password2" class="form-label text-white">Confirm Password:</label>
                    <input type="password" v-model="re_password" class="form-control" id="password2">
                </div>
                 <div class="mb-3">                    
                    <input type="checkbox" v-model="is_vendor" class="form-check-input" id="is_vendor">
                    <label for="is_vendor" class="form-label text-white ms-3">Are you vendor?</label>
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
import { useToast } from "vue-toastification"
import { useRequestStore } from '../stores/RequestStore'

export default {
    name:'SignInView',
    data(){
        return {
            username:'',
            email:'',
            password:'',
            re_password:'',
            is_vendor:false,
            first_name:'',
            last_name:'',
            user_age:'',
            user_country: '',
            user_city: '',
            user_address: '',           
        }
    },
    setup(){         
        const toast = useToast()
        const request = useRequestStore()
        return {toast,request}
    },
    methods:{
        async submit(){            
            const user={
                username :this.username,
                email: this.email,
                password : this.password,
                re_password:this.re_password,
                is_vendor:this.is_vendor,
                first_name:this.first_name,
                last_name:this.last_name,
                user_age:this.user_age,
                user_country:this.user_country,
                user_city:this.user_city,
                user_address:this.user_address
            }
            const response = await this.request.postRequest('api/users/',user)
            if(response.status===201){                        
                this.$router.push('/sign-in')
                this.toast.success('Registered successfully')
            }
        }
    }
}
</script>