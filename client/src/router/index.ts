import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import Home from "../views/Home.vue";
import LogIn from "../views/LogIn.vue";
import { useStore } from "../store/index"
import { ActionTypes } from '../store/actions'

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/login",
    name: "LogIn",
    component: LogIn,
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

// Creating a route guard to redirect if a user is not logged in
const store = useStore();
store.dispatch(ActionTypes.UpdateUser)
const user = store.getters.user_data;
const isAuthenticated = (user == null) ? false : true;

router.beforeEach((to, from, next) => {
    if (to.name !== 'LogIn' && !isAuthenticated) next({ name: 'LogIn' })
    else if(to.name == 'LogIn' && isAuthenticated) next({ name: 'Home' })
    else next();
})

export default router;
