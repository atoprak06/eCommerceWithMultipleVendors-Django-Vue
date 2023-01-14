<template>    
    <div class="card p-1" style="width: 18rem;">
        <img :src="product.image_url" class="mx-auto" style="width:15rem; height:20rem; object-fit:contain;">
        <div class="card-body">
            <h5 class="card-title d-flex justify-content-between">
            <span class="text-dark">{{product.title}}</span>    
            <span class="text-danger">${{product.price}}</span>
            </h5>              
            <a href="/" class="text-decoration-none"><small class="small bg-dark text-white rounded-3 p-1">{{product.category}}</small> </a>             
            <p class="card-text mt-3">{{product.description}}</p>
            <router-link :to="{name:'product',params:{id:product.id,slug:product.slug}}" class="btn btn-primary">Go to Product</router-link>
            <hr>
            <a href="/" class="text-decoration-none"><p class="small rounded-3 text-dark fw-bold text-center p-1 m-0">Added by {{product.created_by}}</p></a>
        </div>
    </div>
</template>
    
<script>
export default {
    name:'Product',
    props:{
        product:{}
    }
}
</script>