<template>
  <div class="app bg-dark p-3">
    <Navbar/>  
    <router-view/>
  </div>
</template>

<script>
import Navbar from './components/Navbar'
export default {
  components:{
    Navbar,
  }
}
</script>

