<template>
    <div class="register">
        <div class="container bg-dark d-flex flex-column align-items-center mt-5">
            <h3 class="text-white text-center">Register</h3>            
            <form class="mt-5" style="width:100%; max-width:30rem"> 
                <div class="mb-3">
                    <label for="username" class="form-label text-white">Username:</label>
                    <input type="text" class="form-control" id="username" aria-describedby="emailHelp">                    
                </div>
                <div class="mb-3">
                    <label for="mail" class="form-label text-white">Email:</label>
                    <input type="mail" class="form-control" id="mail" aria-describedby="emailHelp">                    
                </div>
                <div class="mb-3">
                    <label for="password" class="form-label text-white">Password:</label>
                    <input type="password" class="form-control" id="password">
                </div>
                <div class="mb-3">
                    <label for="password2" class="form-label text-white">Confirm Password:</label>
                    <input type="password2" class="form-control" id="password">
                </div>
                
                <div class="mb-3 text-end">
                    <router-link to="sign-in" class="text-primary">Already have an account?</router-link>
                </div>              
                <div class="d-flex justify-content-end">
                    <button type="submit" class="btn btn-primary">Submit</button>
                </div>
            </form>
        </div>
    </div>
    
</template>

<script>
export default {
    name:'SignInView'
}
</script>