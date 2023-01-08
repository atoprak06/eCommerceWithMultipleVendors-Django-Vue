<template>
  <div class="app bg-dark p-3 d-flex flex-column" style="min-height:100vh">
    <Navbar/>  
    <router-view/>
    <Footer class=" mt-auto"/>
  </div>
</template>

<script>
import Navbar from './components/Navbar'
import Footer from './components/Footer'
import { useTokenStore } from './stores/TokensStore'
import { mapStores } from 'pinia'
import axios from 'axios'

export default {  
  components:{
    Navbar,
    Footer
  },
  created(){        
    this.tokenStore.initializeToken
    const token = this.tokenStore.token              
    if(token){
        axios.defaults.headers.common['Authorization'] = 'Token ' + token
    }else{
        axios.defaults.headers.common['Authorization'] = ''
    }      
},
computed:{
  ...mapStores(useTokenStore)
},  
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

*{
  font-family: 'Poppins', sans-serif;
}
</style>
