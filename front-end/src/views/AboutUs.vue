<template>
  <div class="min-h-screen gradient-slate">
    <div class="container-page">
      <!-- Header -->
      <div class="header-section animate-fade-in">
        <h1 class="title-main">Sobre Nós</h1>
        <p class="subtitle-text">Conheça mais sobre o projeto taqiCFD e nossa equipe</p>
      </div>

      <!-- Tabs Component -->
      <div class="animate-slide-up">
        <SobreTabs />
      </div>
    </div>
  </div>
</template>

<script>
import SobreTabs from '@/components/SobreTabs.vue'

export default {
  name: 'AboutUs',
  components: {
    SobreTabs
  }
}
</script>
