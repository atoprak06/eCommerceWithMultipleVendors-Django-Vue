import { defineStore } from 'pinia'
import axios from 'axios'

export const useTokenStore = defineStore('token', {
    state: () => ({ 
        user:{},
        token:'',
        isAuthenticated:false 
    }),
    getters: {
      initializeToken(state){
        if(localStorage.getItem('token')){
            state.token = localStorage.getItem('token')
            state.isAuthenticated= true
        }else{
            state.token = ''
            state.isAuthenticated=false
        }
      },      
      removeToken(state){
        axios.post('api/token/logout')
        state.token = ''
        state.isAuthenticated=false
        state.user={}
        localStorage.removeItem('token')
      },
      getUser(state){        
        axios
            .get('api/users/me')
            .then(response=>{
                state.user=response.data
            })
      }
    },
    actions: {      
      setToken(token){        
        this.token = 'Token ' + token        
        this.isAuthenticated=true
      },     
    },
  })