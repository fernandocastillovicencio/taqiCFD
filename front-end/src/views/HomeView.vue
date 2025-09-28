<template>
  <div class="home">
    <!-- Hero Section -->
    <div class="bg-gradient-to-r from-blue-600 to-blue-800 text-white rounded-lg p-8 mb-8">
      <div class="text-center">
        <h1 class="text-4xl font-bold mb-4">taqiCFD</h1>
        <p class="text-xl mb-6">Ferramenta Rápida e Interativa para Predições CFD</p>
        <p class="text-lg opacity-90 max-w-3xl mx-auto">
          Simule e analise escoamentos 2D ao redor de geometrias simples usando 
          modelos de machine learning pré-treinados. Obtenha resultados instantâneos 
          sem a necessidade de simulações CFD complexas.
        </p>
      </div>
    </div>

    <!-- Features Grid -->
    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
      <div class="bg-white p-6 rounded-lg shadow-md border border-gray-200">
        <div class="text-blue-600 text-3xl mb-4">🎯</div>
        <h3 class="text-xl font-semibold mb-2">Geometrias Simples</h3>
        <p class="text-gray-600">
          Desenhe ou carregue geometrias 2D como círculos, quadrados, polígonos e formas customizadas.
        </p>
      </div>

      <div class="bg-white p-6 rounded-lg shadow-md border border-gray-200">
        <div class="text-green-600 text-3xl mb-4">⚡</div>
        <h3 class="text-xl font-semibold mb-2">Predições Instantâneas</h3>
        <p class="text-gray-600">
          Resultados CFD em segundos usando modelos de IA pré-treinados, sem esperas longas.
        </p>
      </div>

      <div class="bg-white p-6 rounded-lg shadow-md border border-gray-200">
        <div class="text-purple-600 text-3xl mb-4">🔧</div>
        <h3 class="text-xl font-semibold mb-2">Condições Configuráveis</h3>
        <p class="text-gray-600">
          Configure velocidade, pressão, tamanho do domínio e outras condições de contorno.
        </p>
      </div>

      <div class="bg-white p-6 rounded-lg shadow-md border border-gray-200">
        <div class="text-orange-600 text-3xl mb-4">📊</div>
        <h3 class="text-xl font-semibold mb-2">Visualização Interativa</h3>
        <p class="text-gray-600">
          Interface intuitiva com múltiplas abas, botões e ferramentas de visualização.
        </p>
      </div>

      <div class="bg-white p-6 rounded-lg shadow-md border border-gray-200">
        <div class="text-red-600 text-3xl mb-4">🚀</div>
        <h3 class="text-xl font-semibold mb-2">Leve e Rápido</h3>
        <p class="text-gray-600">
          Sem necessidade de computações CFD pesadas - tudo roda no navegador.
        </p>
      </div>

      <div class="bg-white p-6 rounded-lg shadow-md border border-gray-200">
        <div class="text-indigo-600 text-3xl mb-4">📈</div>
        <h3 class="text-xl font-semibold mb-2">Resultados Detalhados</h3>
        <p class="text-gray-600">
          Análise completa com gráficos, visualizações e opções de exportação.
        </p>
      </div>
    </div>

    <!-- Quick Start -->
    <div class="bg-white rounded-lg shadow-md p-8 mb-8">
      <h2 class="text-2xl font-bold text-gray-800 mb-6 text-center">Como Começar</h2>
      <div class="grid md:grid-cols-3 gap-6">
        <div class="text-center">
          <div class="bg-blue-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
            <span class="text-blue-600 font-bold text-xl">1</span>
          </div>
          <h3 class="font-semibold mb-2">Defina a Geometria</h3>
          <p class="text-gray-600">Desenhe ou carregue sua geometria 2D</p>
          <router-link to="/geometry" class="text-blue-600 hover:text-blue-800 mt-2 inline-block">
            Ir para Geometria →
          </router-link>
        </div>

        <div class="text-center">
          <div class="bg-green-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
            <span class="text-green-600 font-bold text-xl">2</span>
          </div>
          <h3 class="font-semibold mb-2">Configure a Simulação</h3>
          <p class="text-gray-600">Defina condições de contorno e parâmetros</p>
          <router-link to="/simulation" class="text-blue-600 hover:text-blue-800 mt-2 inline-block">
            Ir para Simulação →
          </router-link>
        </div>

        <div class="text-center">
          <div class="bg-purple-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
            <span class="text-purple-600 font-bold text-xl">3</span>
          </div>
          <h3 class="font-semibold mb-2">Visualize Resultados</h3>
          <p class="text-gray-600">Analise campos de velocidade e pressão</p>
          <router-link to="/results" class="text-blue-600 hover:text-blue-800 mt-2 inline-block">
            Ver Resultados →
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeView'
}
</script>

<style scoped>
.home {
  margin-top: 70px;
  min-height: calc(100vh - 70px);
}

.bg-gradient-to-r {
  background: linear-gradient(to right, #2563eb, #3b82f6);
}

.text-white {
  color: white;
}

.rounded-lg {
  border-radius: 0.5rem;
}

.p-8 {
  padding: 2rem;
}

.mb-8 {
  margin-bottom: 2rem;
}

.text-center {
  text-align: center;
}

.text-4xl {
  font-size: 2.25rem;
}

.font-bold {
  font-weight: 700;
}

.mb-4 {
  margin-bottom: 1rem;
}

.text-xl {
  font-size: 1.25rem;
}

.opacity-90 {
  opacity: 0.9;
}

.max-w-3xl {
  max-width: 48rem;
}

.mx-auto {
  margin-left: auto;
  margin-right: auto;
}

.grid {
  display: grid;
}

.md\:grid-cols-2 {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

.lg\:grid-cols-3 {
  grid-template-columns: repeat(3, minmax(0, 1fr));
}

.gap-6 {
  gap: 1.5rem;
}

.bg-white {
  background-color: white;
}

.p-6 {
  padding: 1.5rem;
}

.rounded-lg {
  border-radius: 0.5rem;
}

.shadow-md {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.border {
  border-width: 1px;
}

.border-gray-200 {
  border-color: #e5e7eb;
}

.text-blue-600 {
  color: #2563eb;
}

.text-green-600 {
  color: #10b981;
}

.text-purple-600 {
  color: #6b5bca;
}

.text-orange-600 {
  color: #f97316;
}

.text-red-600 {
  color: #ef4444;
}

.text-indigo-600 {
  color: #6366f1;
}

.text-xl {
  font-size: 1.25rem;
}

.font-semibold {
  font-weight: 600;
}

.mb-2 {
  margin-bottom: 0.5rem;
}

.text-gray-600 {
  color: #4b5563;
}

.hover\:text-blue-800:hover {
  color: #1e40af;
}

.mt-2 {
  margin-top: 0.5rem;
}

.inline-block {
  display: inline-block;
}

.bg-blue-100 {
  background-color: #ebf8ff;
}

.w-16 {
  width: 4rem;
}

.h-16 {
  height: 4rem;
}

.rounded-full {
  border-radius: 9999px;
}

.flex {
  display: flex;
}

.items-center {
  align-items: center;
}

.justify-center {
  justify-content: center;
}

.mx-auto {
  margin-left: auto;
  margin-right: auto;
}

.mb-4 {
  margin-bottom: 1rem;
}

.font-bold {
  font-weight: 700;
}

.text-xl {
  font-size: 1.25rem;
}

.text-blue-600 {
  color: #2563eb;
}

.hover\:text-blue-800:hover {
  color: #1e40af;
}

.mt-2 {
  margin-top: 0.5rem;
}

.inline-block {
  display: inline-block;
}

@media (max-width: 768px) {
  .hero-section {
    flex-direction: column;
    text-align: center;
    padding: 40px 20px;
  }
  
  .hero-content h1 {
    font-size: 3rem;
  }
  
  .cta-buttons {
    justify-content: center;
  }
}
</style>