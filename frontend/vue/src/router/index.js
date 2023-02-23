import { createRouter, createWebHistory } from 'vue-router'
import IndexView from '../views/IndexView.vue'
import MenuView from '../views/MenuView.vue'
import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'
import CreateView from '../views/CreateView.vue'
import CartView from '../views/CartView.vue'
import SearchView from '../views/SearchView.vue'
import CartOrder from '../views/CartOrderView.vue'
import AppView from '../views/App.vue'


const routes = [
  {
    path: '/',
    name: 'index',
    component: IndexView
  },
  {
    path: '/menu',
    name: 'menu',
    component: MenuView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/create',
    name: 'create',
    component: CreateView
  },
  {
    path: '/cart',
    name: 'cart',
    component: CartView
  },
  {
    path: '/cartorder',
    name: 'cartorder',
    component: CartOrder
  },
  {
    path: '/search',
    name: 'search',
    component: SearchView
  },
  {
    path: '/app',
    name: 'app',
    component: AppView
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
