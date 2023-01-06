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

export default {
  components:{
    Navbar,
    Footer
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

*{
  font-family: 'Poppins', sans-serif;
}
</style>
