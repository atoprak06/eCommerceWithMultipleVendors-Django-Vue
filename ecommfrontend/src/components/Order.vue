<template>
    <div>
        <button class="btn" :class="[isActiveModal?'btn-warning':'btn-success']" @click.prevent="isActiveModal=!isActiveModal"><small v-if="isActiveModal">Hide Details</small> <small v-else>Show Details</small></button>
        <div class="order" v-if="isActiveModal">
            <table class="table table-hower">
                <thead class="table-dark">
                    <tr>
                        <th scope="col">Product</th>
                        <th scope="col">Product Price</th>
                        <th scope="col">Quantity</th>
                        <th scope="col">Total</th>                   
                    </tr>
                </thead>
                <tbody class="table-dark">
                    <tr v-for="product in order.products" :key="product">
                        <td><router-link class="text-decoration-none" :to="{name:'product',params:{slug:product.product.slug,id:product.product.id}}">{{product.product.title}}</router-link> </td>
                        <td>${{product.product.price}}</td>
                        <td>{{product.quantity}}</td>
                        <td>${{product.productTotalPrice}}</td>                   
                    </tr>
                </tbody>
            </table>       
        </div>
    </div>
 
</template>

<script>
import moment from 'moment'

export default {
    data(){
        return {
            isActiveModal:false
        }
    },
    props:{
        order:Object,        
    },      
    methods:{
        getTime(time){
            return moment(time).fromNow()
        },
       
    }
}
</script>