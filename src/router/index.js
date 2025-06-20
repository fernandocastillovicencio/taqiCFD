import { createRouter, createWebHistory } from "vue-router";
import GeometryView from "../views/GeometryView.vue";
import SimulationView from "../views/SimulationView.vue";
import ResultsView from "../views/ResultsView.vue";
import AboutUs from "../views/AboutUs.vue";

const routes = [
  { path: "/", redirect: "/geometry" },
  { path: "/geometry", component: GeometryView },
  { path: "/simulation", component: SimulationView },
  { path: "/results", component: ResultsView },
  { path: "/about", component: AboutUs},
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
