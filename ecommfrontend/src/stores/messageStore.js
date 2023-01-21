import { defineStore } from 'pinia'

export const useMessageStore = defineStore('message',{
    state:()=>({        
        message:'',
        display:false
    }),   
    actions:{
        showMessage(message){         
            this.message=message
            this.display = true            
        },       
    }
})
