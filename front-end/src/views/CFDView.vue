<template>
  <div class="cfd-view min-h-screen bg-gray-50">
    <div class="container mx-auto px-4 py-8">
      <!-- Header -->
      <div class="bg-white shadow-md rounded-lg mb-6 p-6">
        <h1 class="text-3xl font-bold text-gray-800 mb-2">taqiCFD - Simulação CFD</h1>
        <p class="text-gray-600">Ferramenta rápida e interativa para predição de escoamentos 2D</p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-4 gap-6">
        <!-- Sidebar com parâmetros -->
        <div class="lg:col-span-1">
          <div class="bg-white shadow-md rounded-lg p-6">
            <h2 class="text-xl font-semibold text-gray-800 mb-4">Parâmetros</h2>
            
            <!-- Geometria -->
            <div class="mb-6">
              <h3 class="text-lg font-medium text-gray-700 mb-3">Geometria</h3>
              <div class="space-y-3">
                <div>
                  <label class="block text-sm font-medium text-gray-600 mb-1">Tipo</label>
                  <select v-model="parameters.geometry.type" 
                          class="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500">
                    <option value="circle">Círculo</option>
                    <option value="square">Quadrado</option>
                    <option value="rectangle">Retângulo</option>
                  </select>
                </div>
                
                <div v-if="parameters.geometry.type === 'circle'">
                  <label class="block text-sm font-medium text-gray-600 mb-1">Raio (m)</label>
                  <input v-model.number="parameters.geometry.radius" type="number" step="0.01" min="0.01"
                         class="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500">
                </div>
                
                <div v-if="parameters.geometry.type !== 'circle'" class="grid grid-cols-2 gap-2">
                  <div>
                    <label class="block text-sm font-medium text-gray-600 mb-1">Largura (m)</label>
                    <input v-model.number="parameters.geometry.width" type="number" step="0.01" min="0.01"
                           class="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500">
                  </div>
                  <div>
                    <label class="block text-sm font-medium text-gray-600 mb-1">Altura (m)</label>
                    <input v-model.number="parameters.geometry.height" type="number" step="0.01" min="0.01"
                           class="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500">
                  </div>
                </div>
              </div>
            </div>

            <!-- Condições de Contorno -->
            <div class="mb-6">
              <h3 class="text-lg font-medium text-gray-700 mb-3">Condições de Contorno</h3>
              <div class="space-y-3">
                <div>
                  <label class="block text-sm font-medium text-gray-600 mb-1">Velocidade de Entrada (m/s)</label>
                  <input v-model.number="parameters.boundary_conditions.inlet_velocity" 
                         type="number" step="0.1" min="0.1"
                         class="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500">
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-600 mb-1">Pressão de Saída (Pa)</label>
                  <input v-model.number="parameters.boundary_conditions.outlet_pressure" 
                         type="number" step="1"
                         class="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500">
                </div>
              </div>
            </div>

            <!-- Propriedades do Fluido -->
            <div class="mb-6">
              <h3 class="text-lg font-medium text-gray-700 mb-3">Propriedades do Fluido</h3>
              <div class="space-y-3">
                <div>
                  <label class="block text-sm font-medium text-gray-600 mb-1">Densidade (kg/m³)</label>
                  <input v-model.number="parameters.fluid_properties.density" 
                         type="number" step="0.1" min="0.1"
                         class="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500">
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-600 mb-1">Viscosidade (Pa·s)</label>
                  <input v-model.number="parameters.fluid_properties.viscosity" 
                         type="number" step="0.0001" min="0.0001"
                         class="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500">
                </div>
              </div>
            </div>

            <!-- Botões -->
            <div class="space-y-3">
              <button @click="runSimulation" :disabled="isLoading"
                      class="w-full bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 disabled:bg-gray-400 transition-colors">
                {{ isLoading ? 'Simulando...' : 'Executar Simulação' }}
              </button>
              <button @click="resetParameters"
                      class="w-full bg-gray-500 text-white py-2 px-4 rounded-md hover:bg-gray-600 transition-colors">
                Resetar
              </button>
            </div>

            <!-- Status da API -->
            <div class="mt-4 p-3 rounded-md" :class="apiStatus.connected ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'">
              <p class="text-sm font-medium">{{ apiStatus.message }}</p>
            </div>
          </div>
        </div>

        <!-- Área principal de visualização -->
        <div class="lg:col-span-3">
          <CFDVisualization 
            :prediction-data="predictionData"
            :metadata="metadata"
            :is-loading="isLoading"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { cfdAPI } from '../services/api.js'
import CFDVisualization from '../components/CFDVisualization.vue'

export default {
  name: 'CFDView',
  components: {
    CFDVisualization
  },
  data() {
    return {
      isLoading: false,
      predictionData: {},
      metadata: {},
      apiStatus: {
        connected: false,
        message: 'Verificando conexão...'
      },
      parameters: {
        geometry: {
          type: 'circle',
          radius: 0.1,
          width: 0.2,
          height: 0.2,
          characteristic_length: 0.1
        },
        boundary_conditions: {
          inlet_velocity: 1.0,
          outlet_pressure: 0.0,
          wall_temperature: 300.0
        },
        fluid_properties: {
          density: 1.0,
          viscosity: 0.001
        },
        grid_size: [50, 50]
      }
    }
  },
  async mounted() {
    await this.checkAPIHealth()
  },
  methods: {
    async checkAPIHealth() {
      try {
        await cfdAPI.healthCheck()
        this.apiStatus = {
          connected: true,
          message: 'API conectada ✅'
        }
      } catch (error) {
        this.apiStatus = {
          connected: false,
          message: 'API desconectada ❌'
        }
        console.error('API Health Check failed:', error)
      }
    },

    async runSimulation() {
      if (!this.apiStatus.connected) {
        alert('API não está disponível. Verifique a conexão.')
        return
      }

      this.isLoading = true
      
      try {
        // Atualizar characteristic_length baseado na geometria
        if (this.parameters.geometry.type === 'circle') {
          this.parameters.geometry.characteristic_length = this.parameters.geometry.radius * 2
        } else {
          this.parameters.geometry.characteristic_length = Math.min(
            this.parameters.geometry.width, 
            this.parameters.geometry.height
          )
        }

        const response = await cfdAPI.predictFlow(this.parameters)
        
        if (response.success) {
          this.predictionData = response.prediction
          this.metadata = response.metadata
        } else {
          throw new Error(response.error || 'Erro na predição')
        }
      } catch (error) {
        console.error('Simulation error:', error)
        alert(`Erro na simulação: ${error.message}`)
      } finally {
        this.isLoading = false
      }
    },

    resetParameters() {
      this.parameters = {
        geometry: {
          type: 'circle',
          radius: 0.1,
          width: 0.2,
          height: 0.2,
          characteristic_length: 0.1
        },
        boundary_conditions: {
          inlet_velocity: 1.0,
          outlet_pressure: 0.0,
          wall_temperature: 300.0
        },
        fluid_properties: {
          density: 1.0,
          viscosity: 0.001
        },
        grid_size: [50, 50]
      }
      this.predictionData = {}
      this.metadata = {}
    }
  }
}
</script>