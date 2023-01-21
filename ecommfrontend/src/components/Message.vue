<template>
  <div class="alert w-100 mx-auto alert-success alert-dismissible fade show" role="alert" v-if="messageStore.display">
    <strong class="text-center">{{messageStore.message}}</strong>
    <button @click.prevent="messageStore.display=!messageStore.display" type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
</div>
</template>

<script>
import {useMessageStore} from '../stores/messageStore'
export default {
    setup(){
        const messageStore = useMessageStore()
        return {messageStore}
    }    
}
</script>

<style scoped>
  
</style>