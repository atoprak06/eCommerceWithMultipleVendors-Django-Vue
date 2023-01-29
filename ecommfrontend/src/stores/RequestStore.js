import { defineStore } from 'pinia'
import axios from 'axios'
import { useToast } from 'vue-toastification';

const toast = useToast()
const options = {
    position: "top-center",
    timeout: 5000,
    closeOnClick: true,
    pauseOnFocusLoss: true,
    pauseOnHover: true,
    draggable: true,
    draggablePercent: 0.6,
    showCloseButtonOnHover: false,
    hideProgressBar: true,
    closeButton: "button",
    icon: true,
    rtl: false
}       

export const useRequestStore  = defineStore('request',{
    state : () => ({
        products : [],
        pageCount : 1,
        // product : {}      
    }),
    actions : {
        async getRequest(query){
            await axios.get(query)
                .then(response => {                    
                    if(response.status===200 || response.status===201){
                        if (response.data.results){
                            this.pageCount = Math.ceil(response.data['count']/16) 
                            this.products = response.data.results
                        }
                        // else{    
                        //     this.product = response.data
                        // }
                    }                           
                })                      
                .catch(error=> { 
                    if (error.response) {                         
                        // The request was made and the server responded with a status code
                        // that falls out of the range of 2xx                  
                        let errorType = `${error.response.status}  ${error.response.statusText}`
                        toast.error(errorType,options)                       
                    } else if (error.request) { 
                        // The request was made but no response was received
                        // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
                        // http.ClientRequest in node.js                   
                        toast.error(error.request,options);                    
                    } else {                       
                        // Something happened in setting up the request that triggered an Error
                        toast.error(error.message,options);
                    }                   
                });   
        },
        async postRequest(query,data){
            return await axios.post(query,data)
                        .catch(error=> { 
                            if (error.response) {                         
                                // The request was made and the server responded with a status code
                                // that falls out of the range of 2xx                  
                                let errorType = `${error.response.status}  ${error.response.statusText}`
                                toast.error(errorType,options)                       
                            } else if (error.request) { 
                                // The request was made but no response was received
                                // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
                                // http.ClientRequest in node.js                   
                                toast.error(error.request,options);                    
                            } else {                       
                                // Something happened in setting up the request that triggered an Error
                                toast.error(error.message,options);
                            }                   
                        }); 
        },
        async patchRequest(query,data){
            return await axios.patch(query,data)
                        .catch(error=> { 
                            if (error.response) {                         
                                // The request was made and the server responded with a status code
                                // that falls out of the range of 2xx                  
                                let errorType = `${error.response.status}  ${error.response.statusText}`
                                toast.error(errorType,options)                       
                            } else if (error.request) { 
                                // The request was made but no response was received
                                // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
                                // http.ClientRequest in node.js                   
                                toast.error(error.request,options);                    
                            } else {                       
                                // Something happened in setting up the request that triggered an Error
                                toast.error(error.message,options);
                            }                   
                        }); 
        },
        async getRequestResponse(query){
            return await axios.get(query)              
                .catch(error=> { 
                    if (error.response) {                         
                        // The request was made and the server responded with a status code
                        // that falls out of the range of 2xx                  
                        let errorType = `${error.response.status}  ${error.response.statusText}`
                        toast.error(errorType,options)                       
                    } else if (error.request) { 
                        // The request was made but no response was received
                        // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
                        // http.ClientRequest in node.js                   
                        toast.error(error.request,options);                    
                    } else {                       
                        // Something happened in setting up the request that triggered an Error
                        toast.error(error.message,options);
                    }                   
                });   
        }
    },

})