import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import Home from "../views/Home.vue";
import LogIn from "../views/LogIn.vue";
import { useStore } from "../store/index"
import { ActionTypes } from "../store/actions";
import { use } from "chai";


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
    path: "/profile/:username?",
    name: "Profile",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Profile.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

// Creating a route guard to redirect if a user is not logged in
const store = useStore();

// Update the user
async function isAuthenticated(){
  const user = await store.dispatch(ActionTypes.UpdateUser);
  return (user == null) ? false : true;
}

router.beforeEach(async (to, from, next) => {
  if (to.name !== 'LogIn' && !(await isAuthenticated())) next({ name: 'LogIn' })
  else if(to.name == 'LogIn' && (await isAuthenticated())) next({ name: 'Home' })
  else next();
});

export default router;
