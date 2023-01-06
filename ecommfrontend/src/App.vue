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

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

*{
  font-family: 'Poppins', sans-serif;
}
</style>
