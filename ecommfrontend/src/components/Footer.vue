<template>
    <div class="footer container text-center">
        <div v-if="tokenStore.isAuthenticated">
            <h3 class="text-warning">Hello {{tokenStore.user.username}}</h3>
            <router-link :to="{name:'editprofile'}" class="text-decoration-none">Edit your profile</router-link>
        </div>
        <h2 class="text-white">eCommerce 2023</h2>
    </div>    
</template>

<script>
import {useTokenStore} from '../stores/TokensStore'
export default {
    name:'Footer',
    setup(){
        const tokenStore = useTokenStore()
        return{tokenStore}
    },    
}
</script>