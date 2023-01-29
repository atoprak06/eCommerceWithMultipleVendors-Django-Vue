<template>
    <div class="product row d-flex justify-content-center pt-3 mx-auto mb-5" style="max-width:40rem; width:100%; height:auto">       
        <div class="col-12 mt-5 d-flex justify-content-center align-items-center ">    
            <div class="card p-3" style="width:100%; height:auto">                
                <div class="d-flex justify-content-between align-items-center row ">
                    <div class="col-6">                        
                        <h5 class="text-uppercase mb-0">{{product.title}}</h5>
                        <p class="main-heading mt-2">added by <router-link :to="{name:'vendors',params:{username:product.created_by}}" class="text-success">{{product.created_by}}</router-link>, <span class="text-danger">{{getTime(product.created_at)}}</span></p>
                        <p class="text-danger">${{product.price}}</p>                        
                        <small class="text-uppercase bg-dark text-white rounded-3 p-1">{{product.category}}</small>
                    </div>
                    <div class="image col-6">
                        <img :src="[preview!==null?preview:product.image_url]" style="width:100%; max-height:18rem; object-fit:contain; height:auto;">
                    </div>
                </div>                               
                <p class="col-6">{{product.description}} </p>                
                <button @click.prevent="cartStore.addToCart(product);toast.success('Product Added to Cart',options)" class="btn btn-danger">Add to cart</button>              
            </div>            
        </div>        
        <div v-if="tokenStore.isAuthenticated" class="card my-5 p-3 d-flex flex-column col-12">
            <h5>Add a comment</h5>
            <form @submit.prevent="submitComment">
                <textarea v-model="submitText" rows="4" class="form-control"/>
                <label for="rate" class="mt-3">Rate Product</label>
                <select class="form-select" v-model="rateStar" id="rate">
                    <option value="0">None</option>
                    <option value="1">Very Bad</option>
                    <option value="2">Bad</option>
                    <option value="3">Not Bad</option>
                    <option value="4">Good</option>
                    <option value="5">Very Good</option>
                </select> 
                <button class="btn btn-primary float-end mt-3">Post</button>                                              
            </form>
        </div>
               
        <div v-if="comments.length>0" class="row mt-5 d-flex flex-column justify-content-center align-items-center">
            <h3 class="text-white col-12 text-center">Comments</h3>
           
            <div class="card my-3" v-for="comment in comments" :key="comment">
                <div class="d-flex justify-content-between mt-3 col-12">
                    <div class="d-flex gap-3">
                        <h3 class="lead fs-4">{{comment.user}}</h3>
                        <p>{{getTime(comment.created_at)}}</p>
                    </div>
                    <div class="d-flex">
                        <i v-for="star in comment.star" :key="star" class="text-warning fa fa-star rating-color"></i>
                        <template v-if="comment.star>=0">
                            <i v-for="left in 5-comment.star" :key="left" class="text-secondary fa fa-star rating-color"></i>
                        </template>                                            
                    </div> 
                </div>
                <hr>
                <p class="col-12">{{comment.comment}}</p>                
            </div>
            <Paginate
                id="unit"                
                :page-count="pageCount"
                :page-range="10"
                :margin-pages="3"
                :initial-page="1"
                :prev-class="'ignore'"
                :next-class="'ignore'"
                :disabled-class="'ignore'"
                :click-handler="getComments"
                
            />
            
        </div>
        <form @submit.prevent="submit" v-if="tokenStore.user.username===product.created_by" class="d-flex flex-column col-6 justify-content-center m-3">
                <h3 class="text-warning">Edit your Product</h3>
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
                        <option value="deactive">Deactivate</option>

                    </select>                    
                </div>
                <div class="mb-3">
                    <label for="product_image" class="form-label text-white">Image:</label>
                    <input @change="uploadImg($event)" type="file" id="product_image" class="form-control">
                </div>                                           
            <button type="submit" class="btn btn-primary">Edit</button>            
        </form>   
    </div>
</template>

<script>
import axios from 'axios'
import {useTokenStore} from '../stores/TokensStore'
import {useCartStore} from '../stores/CartStore'
import { useToast } from "vue-toastification"
import moment from 'moment'
import Paginate from "vuejs-paginate-next"
import { useRequestStore } from '../stores/RequestStore'


export default {
    data(){
        return {
            product:{},
            preview:null,
            comments:[],
            pageCount:1,
            rateStar:0,
            submitText:'',
        }
    },
    setup(){
        const tokenStore = useTokenStore()
        const cartStore = useCartStore()        
        const toast = useToast()
        const request = useRequestStore()
       
        return {tokenStore,cartStore,toast,request}
    },
    async mounted(){
        const response = await this.request.getRequestResponse(`api/products/${ this.$route.params.id }`)
        if(response.status === 200 || response.status === 201){
            this.product = response.data
        }       
        await this.getComments(1)        
    },
    methods:{
        async submitComment(){
            let data = {}            
            data.comment = this.submitText
            data.star = this.rateStar 
            const response = await this.request.postRequest(`api/products/${this.$route.params.id}/comments/`,data)
            if(response.status === 200 || response.status === 201){
                this.toast.success('You commented on the product')
            }
            await this.getComments(1)
        },
        async submit(){
            await axios.patch(`api/products/${ this.$route.params.id }/`,this.product,{headers: {'Content-Type': 'multipart/form-data'}})
                .then(response=>{
                    if (response.status === 200){
                        this.toast.success('Product Edited successfully')                        
                    }                 
                })
                .catch(error=> {
                    if (error.response) { 
                        // The request was made and the server responded with a status code
                        // that falls out of the range of 2xx                  
                        let errorType = `${error.response.status}  ${error.response.statusText}`
                        this.toast.error(errorType)                       
                    } else if (error.request) { 
                        // The request was made but no response was received
                        // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
                        // http.ClientRequest in node.js                   
                        this.toast.error(error.request);                    
                    } else {                       
                        // Something happened in setting up the request that triggered an Error
                        this.toast.error(error.message);
                    }                   
                });           
        },
        async getComments(selected=1){
            const response = await this.request.getRequestResponse(`api/products/${this.$route.params.id}/comments/?page=${selected}`)
            if(response.status === 200 || response.status === 201){
                this.pageCount = Math.ceil(response.data['count']/16)
                this.comments = response.data['results']
            }           
        },
        getTime(created_at){            
            return moment(created_at).fromNow()
        },        
        uploadImg(e){
            const target = e.target;
            if (target.files){                
                var reader = new FileReader();
                reader.onload = (a) => {                    
                    this.preview = a.target.result;
                }
                reader.readAsDataURL(target.files[0])
            }            
            if(target&&target.files){                          
                this.product.image_url=target.files[0]             
            }            
        }
    },
    components:{
        Paginate
    }
}
</script>