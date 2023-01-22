import { defineStore } from 'pinia'

export const useCartStore = defineStore('cart',{
    state:()=>({
        cart:[],
    }),
    getters:{
        initializeCart(state){
            if (localStorage.getItem('cart')){                
                state.cart = JSON.parse(localStorage.getItem('cart'))
            }else{
                localStorage.setItem('cart',state.cart)
            }
        },
        getCartTotal(state){
           return state.cart.reduce((n, {quantity}) => n + quantity, 0)            
        },
        getCartPriceTotal(state){
           return (state.cart.reduce((n, {priceTotal}) => n + priceTotal, 0)).toFixed(2)
        },
        removeCart(state){
            state.cart=[]
            localStorage.setItem('cart',JSON.stringify(state.cart))
        }   
    },
    actions:{
        addToCart(product){                      
            if(this.cart.filter(e => e.id === product.id).length>0){ 
                let index = this.cart.findIndex(prId => {return prId.id === product.id})                                        
                this.cart[index].quantity += 1
                localStorage.setItem('cart',JSON.stringify(this.cart))                       
            }else{                
                product.quantity = 1
                this.cart.push(product)
                localStorage.setItem('cart',JSON.stringify(this.cart))              
            }
            this.getProductPriceTotal(product)
        },
        removeProduct(product){
            let index = this.cart.findIndex(prId => {return prId.id === product.id})
            this.cart[index].quantity -= 1
            if(this.cart[index].quantity===0){
                this.cart.splice(index,1)               
            }
            localStorage.setItem('cart',JSON.stringify(this.cart))
            this.getProductPriceTotal(product)
        },
        getProductPriceTotal(product){
            let index = this.cart.findIndex(prId => {return prId.id === product.id})
            this.cart[index].priceTotal=this.cart[index].quantity * parseFloat(this.cart[index].price)
            localStorage.setItem('cart',JSON.stringify(this.cart))
        },
        deleteProduct(product){
            let index = this.cart.findIndex(prId => {return prId.id === product.id})
            this.cart.splice(index,1)
            localStorage.setItem('cart',JSON.stringify(this.cart))            
        }        
    }
})
