<template>
  <nav class="bg-blue-600 shadow-lg">
    <div class="container mx-auto px-4">
      <div class="flex justify-between items-center py-4">
        <div class="flex items-center space-x-4">
          <h1 class="text-2xl font-bold text-white">taqiCFD</h1>
          <span class="text-blue-200 text-sm">Fast CFD Predictions</span>
        </div>
        
        <div class="hidden md:flex space-x-6">
          <router-link 
            to="/" 
            class="text-white hover:text-blue-200 px-3 py-2 rounded-md transition-colors"
            active-class="bg-blue-700"
          >
            Home
          </router-link>
          <router-link 
            to="/geometry" 
            class="text-white hover:text-blue-200 px-3 py-2 rounded-md transition-colors"
            active-class="bg-blue-700"
          >
            Geometria
          </router-link>
          <router-link 
            to="/simulation" 
            class="text-white hover:text-blue-200 px-3 py-2 rounded-md transition-colors"
            active-class="bg-blue-700"
          >
            Simulação
          </router-link>
          <router-link 
            to="/results" 
            class="text-white hover:text-blue-200 px-3 py-2 rounded-md transition-colors"
            active-class="bg-blue-700"
          >
            Resultados
          </router-link>
          <router-link 
            to="/about" 
            class="text-white hover:text-blue-200 px-3 py-2 rounded-md transition-colors"
            active-class="bg-blue-700"
          >
            Sobre
          </router-link>
        </div>

        <button 
          @click="toggleMobileMenu"
          class="md:hidden text-white focus:outline-none"
        >
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
          </svg>
        </button>
      </div>

      <!-- Mobile menu -->
      <div v-show="mobileMenuOpen" class="md:hidden pb-4">
        <router-link 
          to="/" 
          class="block text-white hover:text-blue-200 px-3 py-2"
          @click="closeMobileMenu"
        >
          Home
        </router-link>
        <router-link 
          to="/geometry" 
          class="block text-white hover:text-blue-200 px-3 py-2"
          @click="closeMobileMenu"
        >
          Geometria
        </router-link>
        <router-link 
          to="/simulation" 
          class="block text-white hover:text-blue-200 px-3 py-2"
          @click="closeMobileMenu"
        >
          Simulação
        </router-link>
        <router-link 
          to="/results" 
          class="block text-white hover:text-blue-200 px-3 py-2"
          @click="closeMobileMenu"
        >
          Resultados
        </router-link>
        <router-link 
          to="/about" 
          class="block text-white hover:text-blue-200 px-3 py-2"
          @click="closeMobileMenu"
        >
          Sobre
        </router-link>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'NavHeader',
  data() {
    return {
      mobileMenuOpen: false
    }
  },
  methods: {
    toggleMobileMenu() {
      this.mobileMenuOpen = !this.mobileMenuOpen
    },
    closeMobileMenu() {
      this.mobileMenuOpen = false
    }
  }
}
</script>