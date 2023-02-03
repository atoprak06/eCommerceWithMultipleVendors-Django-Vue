<template>
    <div class="new_product d-flex flex-column align-items-center mt-5">
        <h3 class="text-center text-warning">New Product</h3>
        <form @submit.prevent="submit" class="text-center d-flex flex-column col-6 justify-content-center m-3">
            <div class="mb-3">
                <label for="product_name" class="form-label text-white">Title:</label>
                <input v-model="product.title" type="text" class="form-control" id="product_name">                    
            </div>
            <div class="mb-3">
                <label for="product_category" class="form-label text-white">Category:</label>
                <select v-model="product.category" class="form-select" id="product_category">
                    <option v-for="category in categories" :value="category.title" :key="category.id">{{category.title}}</option>                    
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
            <div class="mb-3">
                <label for="product_image" class="form-label text-white">Image:</label>
                <input @change="uploadImg($event)" type="file" id="product_image" class="form-control">
            </div>
            <div class="mb-3 d-flex justify-content-end">
                <button type="submit" class="btn btn-primary">Add New Product</button> 
            </div>                                           
        </form> 
    </div>     
</template>

<script>
import axios from 'axios'
import { useToast } from "vue-toastification"
import { useRequestStore } from '../stores/RequestStore'
export default {
    setup(){ 
    const toast = useToast()
    const request = useRequestStore()
    return {toast,request}
    },
    data(){
        return {
            product : {},
            categories:[]      
        }
    },
    methods:{
        async submit(){
            await axios.post('api/products/',this.product,{headers: {'Content-Type': 'multipart/form-data'}})
                        .then(response => {                            
                            if (response.status === 201){                            
                                this.toast.success('New Product Added')
                            } 
                        })
        },
        uploadImg(e){            
            const target = e.target;
            if(target&&target.files){                
                this.product.image_url=target.files[0]                
            }            
        }
    },
    async created(){
        const response = await this.request.getRequestResponse('api/categories/')        
        this.categories = response.data['results']
    }
}

</script>