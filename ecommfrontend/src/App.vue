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
  data(){
    return{errors:[]}
  },
  setup(){    
    const tokenStore = useTokenStore()    
    tokenStore.initializeToken
    const token = tokenStore.token              
    if(token){
        axios.defaults.headers.common['Authorization'] = 'Token ' + token
        axios
            .get('api/users/me')
            .then(response=>{
                tokenStore.user=response.data
            })
            .catch(error=> {
                if (error.response) {
                // The request was made and the server responded with a status code
                // that falls out of the range of 2xx
                    for(const property in error.response.data){
                        this.errors.push(`${property}:${error.response.data[property]}`)
                    }                                                
                } else if (error.request) {
                // The request was made but no response was received
                // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
                // http.ClientRequest in node.js
                console.log(error.request);                    
                } else {
                // Something happened in setting up the request that triggered an Error
                console.log('Error', error.message);
                }
                console.log(error.config);
            });
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
