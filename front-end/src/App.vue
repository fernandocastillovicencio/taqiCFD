<template>
  <div id="app" class="min-h-screen flex flex-col bg-slate-50">
    <Navbar />
    <main class="flex-1">
      <router-view />
    </main>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue'

export default {
  name: 'App',
  components: {
    Navbar
  }
}
</script>
