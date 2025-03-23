<template>
  <div class="app-container">
    <header>
      <h1>taqiCFD</h1>
    </header>
    <nav>
      <router-link to="/geometry">Geometry</router-link>
      <router-link to="/simulation">Simulation</router-link>
      <router-link to="/results">Results</router-link>
    </nav>
    <main>
      <router-view />
    </main>
  </div>
</template>

<script setup>
</script>
