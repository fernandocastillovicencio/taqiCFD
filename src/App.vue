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
    <router-view />
  </div>
</template>

<script setup>
</script>

<style scoped>
/* Estilizando o cabeçalho */
header {
  background: #2d8259; /* Cor do fundo */
  color: white;
  padding: 2px;
  text-align: center;
  font-size: 1.2em;
  font-weight: bold;
}

/* Estilizando a barra de navegação */
nav {
  display: flex;
  justify-content: space-around;
  background: #42b983;
  padding: 15px 0;
}

/* Estilo dos links */
nav a {
  color: white;
  text-decoration: none;
  font-size: 1.5em;
  font-weight: bold;
  flex: 1;
  text-align: center;
  padding: 10px 0;
}

/* Adiciona uma linha embaixo do link ativo */
nav a.router-link-exact-active {
  border-bottom: 4px solid white;
}
</style>
