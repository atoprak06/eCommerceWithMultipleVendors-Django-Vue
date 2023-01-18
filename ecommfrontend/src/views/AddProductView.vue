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
            <div class="mb-3 d-flex justify-content-end">
                <button type="submit" class="btn btn-primary">Add New Product</button> 
            </div>                                           
        </form> 
    </div>     
</template>

<script>
import axios from 'axios'
export default {
    data(){
        return {
            product : {}
        }
    },
    methods:{
        submit(){
            axios.post('api/products/',this.product)                            
        }
    }    
}

</script>