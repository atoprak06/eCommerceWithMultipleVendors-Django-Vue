<template>
    <div class="container bg-dark d-flex flex-column align-items-center mt-5">
        <h3 class="text-white text-center">Edit your profile</h3>
        <form class="mt-5" style="width:100%; max-width:30rem"> 
            <div class="mb-3">
                <label for="email" class="form-label text-white">Email:</label>
                <input v-model="tokenStore.user.email" type="email" class="form-control" id="email">                    
            </div>
            <div class="mb-3">
                <label for="firstname" class="form-label text-white">Firstname:</label>
                <input v-model="tokenStore.user.first_name" type="text" class="form-control" id="firstname">                    
            </div>
            <div class="mb-3">
                <label for="lastname" class="form-label text-white">Lastname:</label>
                <input v-model="tokenStore.user.last_name" type="text" class="form-control" id="lastname">                    
            </div>
            <div class="mb-3">
                <label for="age" class="form-label text-white">Age:</label>
                <input v-model="tokenStore.user.user_age" type="number" min='18' max='100' class="form-control" id="age">                    
            </div>
            <div class="mb-3">
                <label for="country" class="form-label text-white">Country:</label>
                <input v-model="tokenStore.user.user_country" type="text" class="form-control" id="country">                    
            </div>
            <div class="mb-3">
                <label for="city" class="form-label text-white">City:</label>
                <input v-model="tokenStore.user.user_city" type="text" class="form-control" id="city">                    
            </div>
            <div class="mb-3">
                <label for="address" class="form-label text-white">Address:</label>
                <input v-model="tokenStore.user.user_address" type="text" class="form-control" id="address">                    
            </div>
            <div class="mb-3">
                <label for="gender" class="form-label text-white">Gender:</label>
                <select v-model="tokenStore.user.user_gender" class="form-select" id="gender">
                    <option selected>{{tokenStore.user.user_gender}}</option>
                    <option v-if="tokenStore.user.user_gender!='male'" value="male">male</option>
                    <option v-if="tokenStore.user.user_gender!='female'" value="female">female</option>
                    <option v-if="tokenStore.user.user_gender!='other'" value="other">other</option>
                </select>                    
            </div>
            <div class="mb-3 form-check">
                <input v-model="tokenStore.user.is_vendor" type="checkbox" class="form-check-input" id="vendor">
                <label class="form-check-label text-white" for="vendor">Vendor Status</label>
            </div>                                   
            <div class="d-flex justify-content-end">
                <button @click.prevent="submit" type="submit" class="btn btn-primary">Edit</button>
            </div>            
        </form>
    </div>
    
</template>

<script>
import {useTokenStore} from '../stores/TokensStore'
import { useToast } from "vue-toastification"
import { useRequestStore } from '../stores/RequestStore'
export default {
    setup(){
        const tokenStore = useTokenStore()        
        const request= useRequestStore()
        const toast = useToast()       
        return {tokenStore,toast,request}
    },   
    methods:{
        async submit(){
            const response = await this.request.patchRequest('api/users/me/',this.tokenStore.user)
            if (response.status === 200){
                this.toast.success('Profile Edited successfully')
            }  
        }
    }  
}
</script>