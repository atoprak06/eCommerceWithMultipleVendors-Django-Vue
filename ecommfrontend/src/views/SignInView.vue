<template>
    <div class="signIn">
        <div class="container bg-dark d-flex flex-column align-items-center mt-5">
            <h3 class="text-white text-center">Sign In</h3>            
            <form class="mt-5" style="width:100%; max-width:30rem"> 
                <div class="mb-3">
                    <label for="username" class="form-label text-white">Username:</label>
                    <input type="text" class="form-control" id="username" aria-describedby="emailHelp">                    
                </div>
                <div class="mb-3">
                    <label for="password" class="form-label text-white">Password:</label>
                    <input type="password" class="form-control" id="password">
                </div>
                <div class="mb-3 form-check">
                    <input type="checkbox" class="form-check-input" id="rememberme">
                    <label class="form-check-label text-white" for="rememerme">Remember me</label>
                </div>
                <div class="mb-3 text-end">
                    <router-link to="/" class="text-primary">Don't have an account?</router-link>
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