import { defineStore } from 'pinia'

export const useTokenStore = defineStore('token', {
    state: () => ({ 
        user:{
            username:''
        },
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
      setToken(state,token){
        state.token = 'Token' + token
        state.isAuthenticated=true
      },
      removeToken(state){
        state.token = '',
        state.isAuthenticated=false
      }
    },
    actions: {
      
     
    },
  })