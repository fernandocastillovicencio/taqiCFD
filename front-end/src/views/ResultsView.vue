<template>
  <div class="results-view">
    <div class="mb-6">
      <div class="bg-gradient-to-r from-green-600 to-green-800 text-white rounded-lg p-6">
        <h1 class="text-2xl font-bold mb-2">Resultados da Simulação CFD</h1>
        <p class="opacity-90">Análise dos campos de velocidade e pressão</p>
      </div>
    </div>

    <!-- Tabs de Visualização -->
    <div class="mb-6">
      <div class="border-b border-gray-200">
        <nav class="-mb-px flex space-x-8">
          <button
            v-for="tab in tabs"
            :key="tab.id"
            @click="activeTab = tab.id"
            :class="[
              'py-2 px-1 border-b-2 font-medium text-sm transition-colors',
              activeTab === tab.id
                ? 'border-blue-500 text-blue-600'
                : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
            ]"
          >
            {{ tab.name }}
          </button>
        </nav>
      </div>
    </div>

    <!-- Conteúdo das Tabs -->
    <div class="grid lg:grid-cols-4 gap-6">
      <!-- Controles laterais -->
      <div class="lg:col-span-1 space-y-4">
        <!-- Controles de Visualização -->
        <div class="bg-white rounded-lg shadow-md p-4">
          <h3 class="text-lg font-semibold mb-3">Controles</h3>
          
          <div class="space-y-4">
            <div v-if="activeTab === 'velocity' || activeTab === 'streamlines'">
              <label class="block text-sm font-medium text-gray-700 mb-1">
                Escala de Velocidade
              </label>
              <input
                v-model.number="visualParams.velocityScale"
                type="range"
                min="0.1"
                max="2"
                step="0.1"
                class="w-full"
                @input="updateVisualization"
              >
              <span class="text-sm text-gray-500">{{ visualParams.velocityScale }}x</span>
            </div>

            <div v-if="activeTab === 'pressure'">
              <label class="block text-sm font-medium text-gray-700 mb-1">
                Range de Pressão
              </label>
              <div class="flex space-x-2">
                <input
                  v-model.number="visualParams.pressureMin"
                  type="number"
                  step="10"
                  class="flex-1 px-2 py-1 border border-gray-300 rounded text-sm"
                  @input="updateVisualization"
                >
                <input
                  v-model.number="visualParams.pressureMax"
                  type="number"
                  step="10"
                  class="flex-1 px-2 py-1 border border-gray-300 rounded text-sm"
                  @input="updateVisualization"
                >
              </div>
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">
                Mostrar Grade
              </label>
              <input
                v-model="visualParams.showGrid"
                type="checkbox"
                class="rounded"
                @change="updateVisualization"
              >
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">
                Mostrar Geometria
              </label>
              <input
                v-model="visualParams.showGeometry"
                type="checkbox"
                class="rounded"
                @change="updateVisualization"
              >
            </div>
          </div>
        </div>

        <!-- Estatísticas -->
        <div class="bg-white rounded-lg shadow-md p-4">
          <h3 class="text-lg font-semibold mb-3">Estatísticas</h3>
          <div class="space-y-3 text-sm">
            <div class="flex justify-between">
              <span>Vel. Máxima:</span>
              <span class="font-medium">{{ stats.maxVelocity.toFixed(2) }} m/s</span>
            </div>
            <div class="flex justify-between">
              <span>Vel. Média:</span>
              <span class="font-medium">{{ stats.avgVelocity.toFixed(2) }} m/s</span>
            </div>
            <div class="flex justify-between">
              <span>Pressão Max:</span>
              <span class="font-medium">{{ stats.maxPressure.toFixed(1) }} Pa</span>
            </div>
            <div class="flex justify-between">
              <span>Pressão Min:</span>
              <span class="font-medium">{{ stats.minPressure.toFixed(1) }} Pa</span>
            </div>
            <div class="flex justify-between">
              <span>Coef. Arrasto:</span>
              <span class="font-medium">{{ stats.dragCoefficient.toFixed(3) }}</span>
            </div>
            <div class="flex justify-between">
              <span>Reynolds:</span>
              <span class="font-medium">{{ stats.reynolds.toFixed(0) }}</span>
            </div>
          </div>
        </div>

        <!-- Ações -->
        <div class="bg-white rounded-lg shadow-md p-4">
          <h3 class="text-lg font-semibold mb-3">Exportar</h3>
          <div class="space-y-2">
            <button
              @click="exportImage"
              class="w-full bg-blue-600 text-white rounded-md px-4 py-2 shadow-md hover:bg-blue-700 transition-colors"
            >
              Exportar Imagem
            </button>
            <button
              @click="exportData"
              class="w-full bg-green-600 text-white rounded-md px-4 py-2 shadow-md hover:bg-green-700 transition-colors"
            >
              Exportar Dados
            </button>
          </div>
        </div>
      </div>

      <!-- Gráfico Principal -->
      <div class="lg:col-span-3 bg-white rounded-lg shadow-md p-4">
        <h3 class="text-lg font-semibold mb-4">{{ activeTab === 'velocity' ? 'Campo de Velocidade' : 'Campo de Pressão' }}</h3>
        
        <!-- Canvas para o gráfico -->
        <div class="relative" style="padding-top: 56.25%;"> <!-- 16:9 Aspect Ratio -->
          <canvas
            ref="resultCanvas"
            class="absolute inset-0 w-full h-full"
          ></canvas>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.results-view {
  background-color: #f9fafb;
  color: #111827;
  padding: 24px;
  min-height: 100vh;
  border-radius: 10px;
  font-family: 'Inter', sans-serif;
}

.mb-6 {
  margin-bottom: 1.5rem;
}

.bg-gradient-to-r {
  background-image: linear-gradient(to right, var(--tw-gradient-stops));
}

.from-green-600 {
  --tw-gradient-from: #4ade80;
  --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to, rgba(77, 224, 128, 0));
}

.to-green-800 {
  --tw-gradient-to: #065f46;
}

.text-white {
  color: #ffffff;
}

.rounded-lg {
  border-radius: 0.5rem;
}

.p-6 {
  padding: 1.5rem;
}

.text-2xl {
  font-size: 1.5rem;
}

.font-bold {
  font-weight: 700;
}

.mb-2 {
  margin-bottom: 0.5rem;
}

.opacity-90 {
  opacity: 0.9;
}

.border-b {
  border-bottom-width: 1px;
}

.border-gray-200 {
  --tw-border-opacity: 1;
  border-color: rgb(229 231 235 / var(--tw-border-opacity));
}

.-mb-px {
  margin-bottom: -1px;
}

.flex {
  display: flex;
}

.space-x-8 > * {
  margin-right: 2rem;
}

.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.px-1 {
  padding-left: 0.25rem;
  padding-right: 0.25rem;
}

.border-b-2 {
  border-bottom-width: 2px;
}

.font-medium {
  font-weight: 500;
}

.text-sm {
  font-size: 0.875rem;
}

.transition-colors {
  transition-property: background-color, border-color, color;
  transition-duration: 300ms;
}

.active {
  @apply border-blue-500 text-blue-600;
}

.inactive {
  @apply border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300;
}

.grid {
  display: grid;
}

.lg\:grid-cols-4 {
  grid-template-columns: repeat(4, minmax(0, 1fr));
}

.gap-6 {
  gap: 1.5rem;
}

.lg\:col-span-1 {
  grid-column: span 1 / span 1;
}

.space-y-4 > * {
  margin-bottom: 1rem;
}

.bg-white {
  background-color: #ffffff;
}

.rounded-lg {
  border-radius: 0.5rem;
}

.shadow-md {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.p-4 {
  padding: 1rem;
}

.text-lg {
  font-size: 1.125rem;
}

.font-semibold {
  font-weight: 600;
}

.mb-3 {
  margin-bottom: 0.75rem;
}

.space-y-4 {
  margin-bottom: 1rem;
}

.block {
  display: block;
}

.text-gray-700 {
  color: #374151;
}

.mb-1 {
  margin-bottom: 0.25rem;
}

input[type="range"] {
  -webkit-appearance: none;
  width: 100%;
  height: 8px;
  border-radius: 5px;
  background: #e5e7eb;
  outline: none;
  opacity: 0.7;
  transition: opacity 0.2s;
}

input[type="range"]:hover {
  opacity: 1;
}

input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: #2563eb;
  cursor: pointer;
}

input[type="range"]::-moz-range-thumb {
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: #2563eb;
  cursor: pointer;
}

input[type="number"] {
  -moz-appearance: textfield;
  appearance: textfield;
}

input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

.rounded {
  border-radius: 0.375rem;
}

.flex-1 {
  flex: 1;
}

.px-2 {
  padding-left: 0.5rem;
  padding-right: 0.5rem;
}

.py-1 {
  padding-top: 0.25rem;
  padding-bottom: 0.25rem;
}

.border {
  border-width: 1px;
}

.border-gray-300 {
  --tw-border-opacity: 1;
  border-color: rgb(209 213 219 / var(--tw-border-opacity));
}

.text-gray-500 {
  color: #6b7280;
}

.font-medium {
  font-weight: 500;
}

.hover\:bg-blue-700:hover {
  background-color: #1e40af;
}

.hover\:bg-green-700:hover {
  background-color: #15803d;
}

.absolute {
  position: absolute;
}

.inset-0 {
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}

.w-full {
  width: 100%;
}

.h-full {
  height: 100%;
}

.relative {
  position: relative;
}

.padding-top-56-25 {
  padding-top: 56.25%;
}
</style>
