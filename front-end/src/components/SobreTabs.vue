<template>
  <div class="sobre-tabs">
    <div class="tab-navigation mb-6">
      <div class="flex border-b border-gray-200">
        <button
          v-for="tab in tabs"
          :key="tab.id"
          @click="activeTab = tab.id"
          :class="[
            'px-4 py-2 font-medium text-sm transition-colors',
            activeTab === tab.id
              ? 'border-b-2 border-blue-500 text-blue-600'
              : 'text-gray-500 hover:text-gray-700'
          ]"
        >
          {{ tab.label }}
        </button>
      </div>
    </div>

    <div class="tab-content">
      <!-- Aba Projeto -->
      <div v-if="activeTab === 'projeto'" class="space-y-6">
        <div class="bg-white rounded-lg shadow-md p-6">
          <h3 class="text-xl font-semibold text-gray-800 mb-4">Sobre o taqiCFD</h3>
          <p class="text-gray-600 mb-4">
            O taqiCFD é uma ferramenta inovadora que combina a precisão das simulações de Dinâmica dos Fluidos Computacional (CFD) 
            com a velocidade e eficiência da inteligência artificial.
          </p>
          <p class="text-gray-600 mb-4">
            Desenvolvido como uma alternativa rápida e acessível às simulações tradicionais do OpenFOAM, 
            nossa plataforma utiliza redes neurais pré-treinadas para fornecer predições instantâneas de campos de velocidade e pressão.
          </p>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-6">
            <div class="bg-blue-50 p-4 rounded-lg">
              <h4 class="font-semibold text-blue-800 mb-2">Tecnologias</h4>
              <ul class="text-sm text-blue-600 space-y-1">
                <li>• Vue.js 3 + Vite</li>
                <li>• Flask + PyTorch</li>
                <li>• Plotly.js</li>
                <li>• TailwindCSS</li>
              </ul>
            </div>
            <div class="bg-green-50 p-4 rounded-lg">
              <h4 class="font-semibold text-green-800 mb-2">Funcionalidades</h4>
              <ul class="text-sm text-green-600 space-y-1">
                <li>• Simulações 2D instantâneas</li>
                <li>• Visualizações interativas</li>
                <li>• Interface intuitiva</li>
                <li>• Exportação de resultados</li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      <!-- Aba Equipe -->
      <div v-if="activeTab === 'equipe'" class="space-y-6">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <!-- Enzo -->
          <div class="bg-white rounded-lg shadow-md p-6">
            <div class="flex items-center mb-4">
              <div class="w-16 h-16 bg-blue-500 rounded-full flex items-center justify-center text-white text-xl font-bold">
                E
              </div>
              <div class="ml-4">
                <h3 class="text-xl font-semibold text-gray-800">Enzo Salles</h3>
                <p class="text-gray-600">Frontend Developer & UI/UX</p>
              </div>
            </div>
            <p class="text-gray-600 mb-4">
              Responsável pelo desenvolvimento da interface web, experiência do usuário e integração dos componentes visuais.
            </p>
            <div class="space-y-2">
              <div class="flex items-center text-sm text-gray-500">
                <span class="font-medium mr-2">Especialidades:</span>
                <span>Vue.js, TailwindCSS, Plotly.js</span>
              </div>
            </div>
          </div>

          <!-- Lucas -->
          <div class="bg-white rounded-lg shadow-md p-6">
            <div class="flex items-center mb-4">
              <div class="w-16 h-16 bg-green-500 rounded-full flex items-center justify-center text-white text-xl font-bold">
                L
              </div>
              <div class="ml-4">
                <h3 class="text-xl font-semibold text-gray-800">Lucas</h3>
                <p class="text-gray-600">Backend Developer & ML Engineer</p>
              </div>
            </div>
            <p class="text-gray-600 mb-4">
              Responsável pela implementação da API, desenvolvimento da rede neural e integração com sistemas de dados.
            </p>
            <div class="space-y-2">
              <div class="flex items-center text-sm text-gray-500">
                <span class="font-medium mr-2">Especialidades:</span>
                <span>Flask, PyTorch, Machine Learning</span>
              </div>
            </div>
          </div>

          <!-- Professor Orientador -->
          <div class="bg-white rounded-lg shadow-md p-6 md:col-span-2">
            <div class="flex items-center mb-4">
              <div class="w-16 h-16 bg-purple-500 rounded-full flex items-center justify-center text-white text-xl font-bold">
                C
              </div>
              <div class="ml-4">
                <h3 class="text-xl font-semibold text-gray-800">Prof. Castilho</h3>
                <p class="text-gray-600">Orientador do Projeto</p>
              </div>
            </div>
            <p class="text-gray-600">
              Professor orientador responsável pela supervisão acadêmica e direcionamento técnico do projeto taqiCFD.
            </p>
          </div>
        </div>
      </div>

      <!-- Aba OpenFOAM -->
      <div v-if="activeTab === 'openfoam'" class="space-y-6">
        <div class="bg-white rounded-lg shadow-md p-6">
          <h3 class="text-xl font-semibold text-gray-800 mb-4">O que é OpenFOAM?</h3>
          <p class="text-gray-600 mb-4">
            OpenFOAM (Open Source Field Operation and Manipulation) é uma biblioteca de C++ livre e de código aberto 
            para simulações de dinâmica dos fluidos computacional (CFD).
          </p>
          
          <div class="space-y-4">
            <div>
              <h4 class="font-semibold text-gray-800 mb-2">Capacidades</h4>
              <p class="text-gray-600 mb-2">Simula o comportamento de fluidos (como ar, água, óleo, gases, etc.) e resolve equações físicas complexas como:</p>
              <ul class="list-disc list-inside text-gray-600 space-y-1 ml-4">
                <li>Escoamento de fluidos (laminar ou turbulento)</li>
                <li>Transferência de calor</li>
                <li>Transporte de partículas</li>
                <li>Reações químicas e combustão</li>
                <li>Interação fluido-estrutura</li>
              </ul>
            </div>

            <div>
              <h4 class="font-semibold text-gray-800 mb-2">Como funciona?</h4>
              <div class="bg-gray-50 p-4 rounded-lg">
                <p class="text-gray-600 mb-2">Você define:</p>
                <ul class="list-disc list-inside text-gray-600 space-y-1 ml-4">
                  <li>A geometria do problema</li>
                  <li>A malha (divisão do espaço em pequenos volumes)</li>
                  <li>As condições de contorno e iniciais</li>
                  <li>Os modelos físicos (como turbulência ou calor)</li>
                </ul>
                <p class="text-gray-600 mt-2">E o OpenFOAM resolve numericamente as equações de Navier-Stokes e outras associadas.</p>
              </div>
            </div>

            <div>
              <h4 class="font-semibold text-gray-800 mb-2">Aplicações Práticas</h4>
              <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div class="bg-blue-50 p-4 rounded-lg">
                  <h5 class="font-medium text-blue-800 mb-2">Automotivo</h5>
                  <p class="text-sm text-blue-600">Simulação aerodinâmica de veículos</p>
                </div>
                <div class="bg-green-50 p-4 rounded-lg">
                  <h5 class="font-medium text-green-800 mb-2">Aeronáutico</h5>
                  <p class="text-sm text-green-600">Testes de túnel de vento virtual</p>
                </div>
                <div class="bg-purple-50 p-4 rounded-lg">
                  <h5 class="font-medium text-purple-800 mb-2">Industrial</h5>
                  <p class="text-sm text-purple-600">Escoamentos em tubulações</p>
                </div>
              </div>
            </div>

            <div class="bg-yellow-50 p-4 rounded-lg">
              <h4 class="font-semibold text-yellow-800 mb-2">Por que o taqiCFD?</h4>
              <p class="text-yellow-700">
                Enquanto o OpenFOAM é extremamente poderoso, pode ser complexo e demorado para análises rápidas. 
                O taqiCFD oferece uma alternativa ágil usando IA para predições instantâneas, ideal para estudos preliminares e educação.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SobreTabs',
  data() {
    return {
      activeTab: 'projeto',
      tabs: [
        { id: 'projeto', label: 'Projeto' },
        { id: 'equipe', label: 'Equipe' },
        { id: 'openfoam', label: 'OpenFOAM' }
      ]
    }
  }
}
</script>

<style scoped>
.sobre-tabs {
  max-width: 100%;
}
</style>
