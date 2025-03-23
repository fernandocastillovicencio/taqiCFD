<template>
  <nav>
    <h1>taqiCFD</h1>
    <div class="nav-links">
      <router-link to="/geometry">Geometry</router-link>
      <router-link to="/simulation">Simulation</router-link>
      <router-link to="/results">Results</router-link>
    </div>
  </nav>
</template>

<style scoped>
nav {
  background: #42b983;
  color: white;
  padding: 10px;
  text-align: center;
  font-size: 1.5em;
}

.nav-links {
  margin-top: 10px;
  display: flex;
  justify-content: center;
  gap: 20px;
}

.nav-links a {
  color: white;
  text-decoration: none;
  font-size: 1.2em;
  font-weight: bold;
  padding: 10px;
  border-radius: 5px;
  transition: background 0.3s;
}

.nav-links a:hover {
  background: #3d9970;
}

.router-link-exact-active {
  background: #2d7a5f;
}
</style>
