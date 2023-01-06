import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignInView from '../views/SignInView.vue'
import RegisterView from '../views/RegisterView.vue'
import UserPageView from '../views/UserPageView.vue'
import CategoriesView from '../views/CategoriesView.vue'
import VendorsView from '../views/VendorsView.vue'
import ContactView from '../views/ContactView.vue'
import CartView from '../views/CartView.vue'



const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
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
    path: '/vendors',
    name: 'vendors',
    component: VendorsView
  },
  {
    path: '/categories',
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

export default router
