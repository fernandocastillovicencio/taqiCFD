<template>
  <div class="sobre-nos-container">
    <h1>Sobre Nós</h1>
    <SobreTabs />
  </div>
</template>

<script setup>
import SobreTabs from '@/components/SobreTabs.vue'
</script>

<style scoped>
.sobre-nos-container {
  background-color: #1e1e1e;
  color: #e0e0e0;
  min-height: 100vh;
  padding: 40px 20px;
  box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.6);
}

h1 {
  text-align: center;
  font-size: 2.5rem;
  color: #61dafb;
  margin-bottom: 30px;
}
</style>
