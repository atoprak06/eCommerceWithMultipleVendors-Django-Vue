<template>
    <div class="user-page container mt-5">        
        <h5 class="text-warning">My Products:</h5>
        <table class="table table-hover">
            <thead class="table-dark">
                <tr>
                    <th scope="col">id</th>
                    <th scope="col">Product Title</th>
                    <th scope="col">Product Price</th>
                    <th scope="col">Date Added</th>
                    <th scope="col">Status</th>
                    <th></th>
                </tr>
            </thead>
            <tbody class="table-dark">
                <tr>
                    <th scope="row">1</th>
                    <td>Product 1 </td>
                    <td>$25.33</td>
                    <td>12.10.2021</td>
                    <td class="text-success">Online</td>
                    <td><router-link to="#" class="btn btn-danger">Show/Edit</router-link></td>
                </tr>
                <tr>
                    <th scope="row">2</th>
                    <td>Product 2</td>
                    <td>$22.22</td>
                    <td>10.10.2021</td>
                    <td class="text-success">Online</td>
                    <td><router-link to="#" class="btn btn-danger">Show/Edit</router-link></td>
                </tr>
                <tr>
                    <th scope="row">3</th>
                    <td>Product 3</td>
                    <td>$124.55</td>
                    <td>08.10.2021</td>
                    <td class="text-danger">Offline</td>
                    <td><router-link to="#" class="btn btn-danger">Show/Edit</router-link></td>
                </tr>
            </tbody>
        </table>     
        <router-link class="btn btn-danger" to="/">Add new product</router-link>
        <hr>
        <h5 class="text-warning">Shopping History:</h5>
        <ul>
            <li class="d-flex justify-content-between mt-3">
                <p class="text-white">Product 1 is orderder by SomeUserName</p>
                <p class="text-white">8 hours ago</p>
            </li>
            <hr class="text-white m-0">
            <li class="d-flex justify-content-between mt-3">
                <p class="text-white">Product 2 is orderder by SomeUserName</p>
                <p class="text-white">12 hours ago</p>
            </li>
            <hr class="text-white m-0">
            <li class="d-flex justify-content-between mt-3">
                <p class="text-white">Product 3 is orderder by SomeUserName</p>
                <p class="text-white">23 hours ago</p>
            </li>
            <hr class="text-white m-0">
            
            
        </ul>
        

        <h5 class="text-success text-end">My Balance: $1244.66</h5>
    </div>
</template>

<script>
export default {
    name:'UserPageView'
}
</script>