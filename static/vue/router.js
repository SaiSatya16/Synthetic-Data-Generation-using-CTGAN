
import about from "./components/about.js";
import home from "./components/home.js";

const routes = [
    {
        path: "/",
        component: home,
        name: "home"
    },
    {
        path: "/about",
        component: about,
        name: "About"
    }
];


const router = new VueRouter({
    routes
});

export default router;