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
export default {
    setup(){        
        const options = {
            position: "top-center",
            timeout: 5000,
            closeOnClick: true,
            pauseOnFocusLoss: true,
            pauseOnHover: true,
            draggable: true,
            draggablePercent: 0.6,
            showCloseButtonOnHover: false,
            hideProgressBar: true,
            closeButton: "button",
            icon: true,
            rtl: false
        }       
    const toast = useToast() 
    return {options,toast}
    },
    data(){
        return {
            product : {},           
        }
    },
    methods:{
        async submit(){

           await axios.post('api/products/',this.product,{headers: {'Content-Type': 'multipart/form-data'}})
                .then(response=>{
                    console.log(response)
                    if (response.status === 201){                            
                        this.toast.success('New Product Added',this.options)
                    } 
                }) 
                .catch(error=> {
                    if (error.response) { 
                        // The request was made and the server responded with a status code
                        // that falls out of the range of 2xx                  
                        let errorType = `${error.response.status}  ${error.response.statusText}`
                        this.toast.error(errorType,this.options)                       
                    } else if (error.request) { 
                        // The request was made but no response was received
                        // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
                        // http.ClientRequest in node.js                   
                        this.toast.error(error.request,this.options);                    
                    } else {                       
                        // Something happened in setting up the request that triggered an Error
                        this.toast.error(error.message,this.options);
                    }                   
                });                           
        },
        uploadImg(e){            
            const target = e.target;
            if(target&&target.files){                
                this.product.image_url=target.files[0]                
            }            
        }
    }    
}

</script>