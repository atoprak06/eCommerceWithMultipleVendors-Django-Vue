import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignInView from '../views/SignInView.vue'
import RegisterView from '../views/RegisterView.vue'
import UserPageView from '../views/UserPageView.vue'
import CategoriesView from '../views/CategoriesView.vue'
import VendorsView from '../views/VendorsView.vue'
import ContactView from '../views/ContactView.vue'
import CartView from '../views/CartView.vue'
import EditProfileView from '../views/EditProfileView'
import ProductView from '../views/ProductView'
import AddProductView from '../views/AddProductView'


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/new-product',
    name: 'newproduct',
    component: AddProductView
  },
  {
    path: '/product/:slug/:id',
    name: 'product',
    component: ProductView
  },
  {
    path: '/edit-profile',
    name: 'editprofile',
    component: EditProfileView
  },
  {
    path: '/cart',
    name: 'cart',
    component: CartView
  },
  {
    path: '/contact',
    name: 'contact',
    component: ContactView
  },
  {
    path: '/vendors/:username?',
    name: 'vendors',
    component: VendorsView
  },
  {
    path: '/categories/:title/:id',
    name: 'categories',
    component: CategoriesView
  },
  {
    path: '/user-page',
    name: 'userpage',
    component: UserPageView
  },
  {
    path: '/sign-in',
    name: 'signin',
    component: SignInView
  },
  {
    path: '/register',
    name: 'register',
    component: RegisterView
  },
  {
    path: '/about',
    name: 'about',   
    component: () => import('../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

import { useTokenStore } from '@/stores/TokensStore'
import { useToast } from "vue-toastification"


router.beforeEach(async (to, from) => {
  const tokenStore = useTokenStore()
  const toast = useToast()
  if (
    // make sure the user is authenticated
    !tokenStore.isAuthenticated &&
    // ❗️ Avoid an infinite redirect
    (to.name === 'userpage' || 
    to.name === 'newproduct' ||
    to.name === 'editprofile'
    )

  ) {
    // redirect the user to the login page
    toast.warning('Sign in first')
    return { name: 'signin' }
  }
})

export default router
