<script setup>
import { ref, watch } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const mobileMenuOpen = ref(false)

// Fechar menu ao trocar de rota
watch(
  () => route.path,
  () => {
    mobileMenuOpen.value = false
  }
)
</script>

<template>
  <nav class="bg-white shadow-lg border-b border-gray-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between h-16">
        <!-- Logo -->
        <div class="flex items-center">
          <RouterLink to="/" class="flex items-center space-x-3 hover:opacity-80 transition-opacity">
            <div class="w-10 h-10 bg-gradient-to-r from-blue-600 to-blue-700 rounded-xl flex items-center justify-center shadow-md">
              <span class="text-white font-bold text-lg">T</span>
            </div>
            <span class="text-2xl font-bold text-gray-800">taqiCFD</span>
          </RouterLink>
        </div>

        <!-- Menu principal -->
        <div class="hidden md:flex items-center space-x-1">
          <RouterLink 
            to="/" 
            class="text-gray-700 hover:text-blue-600 px-4 py-2 rounded-lg text-sm font-medium transition-all duration-200 hover:bg-blue-50"
            :class="{ 'text-blue-600 bg-blue-50 shadow-sm': route.path === '/' }"
          >
            🏠 Simulação
          </RouterLink>
          <RouterLink 
            to="/about" 
            class="text-gray-700 hover:text-blue-600 px-4 py-2 rounded-lg text-sm font-medium transition-all duration-200 hover:bg-blue-50"
            :class="{ 'text-blue-600 bg-blue-50 shadow-sm': route.path === '/about' }"
          >
            👥 Sobre Nós
          </RouterLink>
          <a 
            href="https://github.com/taqicfd" 
            target="_blank" 
            class="text-gray-700 hover:text-blue-600 px-4 py-2 rounded-lg text-sm font-medium transition-all duration-200 hover:bg-blue-50"
          >
            💻 GitHub
          </a>
        </div>

        <!-- Botão mobile -->
        <div class="md:hidden flex items-center">
          <button 
            @click="mobileMenuOpen = !mobileMenuOpen"
            class="text-gray-500 hover:text-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 rounded-lg p-2"
          >
            <svg class="h-6 w-6" viewBox="0 0 24 24" fill="none" stroke="currentColor">
              <path v-if="!mobileMenuOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
              <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
            </svg>
          </button>
        </div>
      </div>

      <!-- Menu mobile -->
      <transition
        enter-active-class="transition duration-200 ease-out"
        enter-from-class="transform scale-95 opacity-0"
        enter-to-class="transform scale-100 opacity-100"
        leave-active-class="transition duration-75 ease-in"
        leave-from-class="transform scale-100 opacity-100"
        leave-to-class="transform scale-95 opacity-0"
      >
        <div v-if="mobileMenuOpen" class="md:hidden">
          <div class="px-2 pt-2 pb-3 space-y-1 bg-gray-50 border-t border-gray-200">
            <RouterLink 
              to="/" 
              class="block px-3 py-3 rounded-lg text-base font-medium text-gray-700 hover:text-blue-600 hover:bg-blue-50 transition-colors"
              @click="mobileMenuOpen = false"
            >
              🏠 Simulação
            </RouterLink>
            <RouterLink 
              to="/about" 
              class="block px-3 py-3 rounded-lg text-base font-medium text-gray-700 hover:text-blue-600 hover:bg-blue-50 transition-colors"
              @click="mobileMenuOpen = false"
            >
              👥 Sobre Nós
            </RouterLink>
            <a 
              href="https://github.com/taqicfd" 
              target="_blank" 
              class="block px-3 py-3 rounded-lg text-base font-medium text-gray-700 hover:text-blue-600 hover:bg-blue-50 transition-colors"
            >
              💻 GitHub
            </a>
          </div>
        </div>
      </transition>
    </div>
  </nav>
</template>

<style scoped>
.router-link-active {
  @apply text-blue-600 bg-blue-50 shadow-sm;
}
</style>
