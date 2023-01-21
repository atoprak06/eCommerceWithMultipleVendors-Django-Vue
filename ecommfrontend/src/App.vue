<template>
  <div class="app bg-dark d-flex flex-column mx-auto" style="min-height:100vh">
    <Navbar @search="search"/>
    <router-view :searchQuery="searchQuery"/>
    <Message class="position-fixed row"/>
    <Footer class="mt-auto"/>
  </div>
</template>

<script>
import Navbar from './components/Navbar'
import Footer from './components/Footer'
import Message from './components/Message.vue'

import { useTokenStore } from './stores/TokensStore'
import axios from 'axios'

export default {  
  components:{
    Navbar,
    Footer,
    Message
  },
  data(){
    return{
      errors:[],
      searchQuery:''
    }
  },
  methods:{
    search(searchQuery){
      this.searchQuery=searchQuery
    }
  },
  setup(){    
    const tokenStore = useTokenStore()    
    tokenStore.initializeToken    
    const token = tokenStore.token              
    if(token){
        axios.defaults.headers.common['Authorization'] = 'Token ' + token
        tokenStore.getUser
    }else{
        axios.defaults.headers.common['Authorization'] = ''
        tokenStore.user={}
    }      
  }, 
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

*{
  font-family: 'Poppins', sans-serif;
}
</style>
