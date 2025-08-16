<script setup lang="ts">
import { RouterLink } from 'vue-router';

</script>

<template>
  <nav>
    <h1>taqiCFD</h1>
    <div class="nav-links">
      <router-link to="/geometry">Geometry</router-link>
      <router-link to="/simulation">Simulation</router-link>
      <router-link to="/results">Results</router-link>
      <router-link to ="/about">Abouts Us</router-link>
    </div>
  </nav>
</template>

<style scoped>
nav {
  background: #121212;
  color: white;
  padding: 15px;
  text-align: center;
  box-shadow: 0 2px 10px rgba(0,0,0,0.5);
}

h1 {
  margin: 0;
  font-size: 2em;
  color: #61dafb;
}

.nav-links {
  margin-top: 10px;
  display: flex;
  justify-content: center;
  gap: 20px;
  flex-wrap: wrap;
}

.nav-links a {
  color: white;
  text-decoration: none;
  font-size: 1.1em;
  font-weight: 600;
  padding: 8px 14px;
  border-radius: 5px;
  transition: background 0.3s, transform 0.2s;
}

.nav-links a:hover {
  background: #1f4037;
  transform: scale(1.05);
}

.router-link-exact-active {
  background: #3a6351;
}

</style>
