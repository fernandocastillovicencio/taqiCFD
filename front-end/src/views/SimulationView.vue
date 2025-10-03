<template>
  <div class="simulation-view">
    <div class="flex flex-col xl:flex-row gap-6">
      <!-- Painel de Controle -->
      <div class="xl:w-1/3 bg-white rounded-lg shadow-md p-6">
        <h2 class="text-xl font-bold mb-4">Configuração da Simulação</h2>
        
        <!-- Parâmetros do Fluido -->
        <div class="mb-6">
          <h3 class="text-lg font-semibold mb-3 text-blue-600">Propriedades do Fluido</h3>
          
          <div class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">
                Tipo de Fluido
              </label>
              <select 
                v-model="fluidParams.type" 
                @change="onFluidTypeChange"
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              >
                <option value="air">Ar (20°C)</option>
                <option value="water">Água (20°C)</option>
                <option value="custom">Personalizado</option>
              </select>
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">
                Densidade (kg/m³)
              </label>
              <input 
                v-model.number="fluidParams.density"
                type="number" 
                step="0.1"
                :disabled="fluidParams.type !== 'custom'"
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-100"
              >
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">
                Viscosidade Dinâmica (Pa·s)
              </label>
              <input 
                v-model.number="fluidParams.viscosity"
                type="number" 
                step="0.0001"
                :disabled="fluidParams.type !== 'custom'"
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-100"
              >
            </div>
          </div>
        </div>

        <!-- Condições de Contorno -->
        <div class="mb-6">
          <h3 class="text-lg font-semibold mb-3 text-green-600">Condições de Contorno</h3>
          
          <div class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">
                Velocidade de Entrada (m/s)
              </label>
              <input 
                v-model.number="boundaryConditions.inletVelocity"
                type="number" 
                step="0.1" 
                min="0.1"
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              >
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">
                Direção do Escoamento
              </label>
              <select 
                v-model="boundaryConditions.flowDirection"
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              >
                <option value="horizontal">Horizontal (→)</option>
                <option value="vertical">Vertical (↑)</option>
                <option value="diagonal">Diagonal (↗)</option>
              </select>
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">
                Pressão de Saída (Pa)
              </label>
              <input 
                v-model.number="boundaryConditions.outletPressure"
                type="number"
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              >
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">
                Condição das Paredes
              </label>
              <select 
                v-model="boundaryConditions.wallCondition"
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              >
                <option value="no-slip">No-Slip (Aderência)</option>
                <option value="slip">Slip (Deslizamento)</option>
                <option value="symmetry">Simetria</option>
              </select>
            </div>
          </div>
        </div>

        <!-- Parâmetros Numéricos -->
        <div class="mb-6">
          <h3 class="text-lg font-semibold mb-3 text-purple-600">Configuração Numérica</h3>
          
          <div class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">
                Tipo de Solver
              </label>
              <select 
                v-model="numericalParams.solver"
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              >
                <option value="simpleFoam">simpleFoam (Laminar/Turbulento)</option>
                <option value="icoFoam">icoFoam (Incompressível Transiente)</option>
                <option value="pisoFoam">pisoFoam (Incompressível PISO)</option>
              </select>
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">
                Máximo de Iterações
              </label>
              <input 
                v-model.number="numericalParams.maxIterations"
                type="number" 
                min="100" 
                max="10000" 
                step="100"
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              >
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">
                Tolerância de Convergência
              </label>
              <input 
                v-model.number="numericalParams.tolerance"
                type="number" 
                step="1e-6"
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              >
            </div>
          </div>
        </div>

        <!-- Números Adimensionais -->
        <div class="mb-6 p-4 bg-gray-50 rounded-lg">
          <h3 class="text-lg font-semibold mb-3">Números Adimensionais</h3>
          <div class="space-y-2 text-sm">
            <p><strong>Reynolds:</strong> {{ reynoldsNumber.toFixed(0) }}</p>
            <p><strong>Mach:</strong> {{ machNumber.toFixed(3) }}</p>
            <p><strong>Strouhal:</strong> {{ strouhalNumber.toFixed(3) }}</p>
          </div>
        </div>

        <!-- Botões de Ação -->
        <div class="space-y-3">
          <button 
            @click="runSimulation"
            :disabled="isSimulating"
            class="w-full bg-green-600 hover:bg-green-700 disabled:bg-gray-400 text-white font-medium py-3 px-4 rounded-md transition-colors"
          >
            <span v-if="!isSimulating">🚀 Executar Simulação</span>
            <span v-else>⏳ Simulando...</span>
          </button>
          
          <button 
            @click="saveConfiguration"
            class="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-md transition-colors"
          >
            💾 Salvar Configuração
          </button>
          
          <button 
            @click="loadConfiguration"
            class="w-full bg-gray-600 hover:bg-gray-700 text-white font-medium py-2 px-4 rounded-md transition-colors"
          >
            📂 Carregar Configuração
          </button>
        </div>

        <!-- Progress Bar -->
        <div v-if="isSimulating" class="mt-4">
          <div class="bg-gray-200 rounded-full h-2">
            <div 
              class="bg-green-600 h-2 rounded-full transition-all duration-500"
              :style="{ width: simulationProgress + '%' }"
            ></div>
          </div>
          <p class="text-sm text-gray-600 mt-1 text-center">
            {{ simulationProgress }}% completo - {{ simulationStatus }}
          </p>
        </div>
      </div>

      <!-- Visualização e Status -->
      <div class="xl:w-2/3 space-y-6">
        <!-- Preview da Simulação -->
        <div class="bg-white rounded-lg shadow-md p-6">
          <h2 class="text-xl font-bold mb-4">Preview da Simulação</h2>
          
          <div class="border border-gray-300 rounded-lg overflow-hidden bg-gray-50">
            <canvas 
              ref="previewCanvas"
              :width="previewWidth" 
              :height="previewHeight"
              class="block w-full"
            ></canvas>
          </div>
          
          <div class="mt-4 grid grid-cols-2 md:grid-cols-4 gap-4 text-sm">
            <div class="text-center p-3 bg-blue-50 rounded-lg">
              <div class="text-blue-600 font-bold text-lg">{{ reynoldsNumber.toFixed(0) }}</div>
              <div class="text-gray-600">Reynolds</div>
            </div>
            <div class="text-center p-3 bg-green-50 rounded-lg">
              <div class="text-green-600 font-bold text-lg">{{ boundaryConditions.inletVelocity }}</div>
              <div class="text-gray-600">Velocidade (m/s)</div>
            </div>
            <div class="text-center p-3 bg-purple-50 rounded-lg">
              <div class="text-purple-600 font-bold text-lg">{{ fluidParams.density }}</div>
              <div class="text-gray-600">Densidade (kg/m³)</div>
            </div>
            <div class="text-center p-3 bg-red-50 rounded-lg">
              <div class="text-red-600 font-bold text-lg">{{ (fluidParams.viscosity * 1000).toFixed(1) }}</div>
              <div class="text-gray-600">Viscosidade (mPa·s)</div>
            </div>
          </div>
        </div>

        <!-- Log da Simulação -->
        <div class="bg-white rounded-lg shadow-md p-6">
          <h3 class="text-lg font-semibold mb-3">Log da Simulação</h3>
          <div class="bg-gray-900 text-green-400 p-4 rounded-lg h-48 overflow-y-auto font-mono text-sm">
            <div v-for="(log, index) in simulationLogs" :key="index" class="mb-1">
              <span class="text-gray-500">[{{ log.timestamp }}]</span> {{ log.message }}
            </div>
            <div v-if="simulationLogs.length === 0" class="text-gray-500">
              Aguardando início da simulação...
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Input oculto para upload de arquivo -->
    <input 
      ref="configFileInput" 
      type="file" 
      accept=".json"
      @change="onConfigFileLoad"
      class="hidden"
    >
  </div>
</template>

<script>
export default {
  name: 'SimulationView',
  data() {
    return {
      fluidParams: {
        type: 'air',
        density: 1.225, // kg/m³ para ar a 20°C
        viscosity: 1.81e-5, // Pa·s para ar a 20°C
        temperature: 293.15 // K
      },
      boundaryConditions: {
        inletVelocity: 10, // m/s
        flowDirection: 'horizontal',
        outletPressure: 0, // Pa (gauge pressure)
        wallCondition: 'no-slip'
      },
      numericalParams: {
        solver: 'simpleFoam',
        maxIterations: 1000,
        tolerance: 1e-6,
        relaxationFactors: {
          velocity: 0.7,
          pressure: 0.3
        }
      },
      isSimulating: false,
      simulationProgress: 0,
      simulationStatus: 'Aguardando...',
      simulationLogs: [],
      previewWidth: 600,
      previewHeight: 300,
      characteristicLength: 1 // metros - será obtido da geometria
    }
  },
  computed: {
    reynoldsNumber() {
      return (this.fluidParams.density * this.boundaryConditions.inletVelocity * this.characteristicLength) / this.fluidParams.viscosity
    },
    machNumber() {
      const soundSpeed = 343 // m/s para ar a 20°C
      return this.boundaryConditions.inletVelocity / soundSpeed
    },
    strouhalNumber() {
      const frequency = 1 // Hz - valor estimado
      return (frequency * this.characteristicLength) / this.boundaryConditions.inletVelocity
    }
  },
  mounted() {
    this.initPreviewCanvas()
    this.loadGeometryData()
  },
  methods: {
    onFluidTypeChange() {
      const presets = {
        air: {
          density: 1.225,
          viscosity: 1.81e-5,
          temperature: 293.15
        },
        water: {
          density: 998.2,
          viscosity: 1.003e-3,
          temperature: 293.15
        }
      }
      
      if (this.fluidParams.type !== 'custom') {
        Object.assign(this.fluidParams, presets[this.fluidParams.type])
      }
    },
    
    loadGeometryData() {
      // Carregar dados da geometria do localStorage ou API
      const savedGeometry = localStorage.getItem('taqiCFD_geometry')
      if (savedGeometry) {
        const geometryData = JSON.parse(savedGeometry)
        // Definir comprimento característico baseado na geometria
        this.characteristicLength = this.getCharacteristicLength(geometryData)
        this.drawPreview(geometryData)
      }
    },
    
    getCharacteristicLength(geometryData) {
      switch (geometryData.type) {
        case 'circle':
          return geometryData.params.radius * 2 // diâmetro
        case 'square':
          return geometryData.params.side
        case 'rectangle':
          return Math.min(geometryData.params.width, geometryData.params.height)
        default:
          return 1
      }
    },
    
    initPreviewCanvas() {
      const canvas = this.$refs.previewCanvas
      if (canvas) {
        this.previewWidth = Math.min(600, canvas.parentElement.clientWidth - 40)
        this.previewHeight = this.previewWidth * 0.5
      }
    },
    
    drawPreview(geometryData = null) {
      const canvas = this.$refs.previewCanvas
      if (!canvas) return

      const ctx = canvas.getContext('2d')
      ctx.clearRect(0, 0, this.previewWidth, this.previewHeight)

      // Desenhar background com gradiente de velocidade
      const gradient = ctx.createLinearGradient(0, 0, this.previewWidth, 0)
      gradient.addColorStop(0, '#dbeafe')
      gradient.addColorStop(1, '#93c5fd')
      
      ctx.fillStyle = gradient
      ctx.fillRect(0, 0, this.previewWidth, this.previewHeight)

      // Desenhar setas indicando direção do fluxo
      this.drawFlowArrows(ctx)

      // Desenhar geometria simplificada
      if (geometryData) {
        this.drawSimpleGeometry(ctx, geometryData)
      }

      // Desenhar informações
      ctx.fillStyle = '#1f2937'
      ctx.font = '12px Arial'
      ctx.fillText(`Reynolds: ${this.reynoldsNumber.toFixed(0)}`, 10, 20)
      ctx.fillText(`Velocidade: ${this.boundaryConditions.inletVelocity} m/s`, 10, 35)
    },
    
    drawFlowArrows(ctx) {
      const numArrows = 8
      const arrowSpacing = this.previewWidth / (numArrows + 1)
      
      ctx.strokeStyle = '#3b82f6'
      ctx.fillStyle = '#3b82f6'
      ctx.lineWidth = 2
      
      for (let i = 1; i <= numArrows; i++) {
        const x = i * arrowSpacing
        const y = this.previewHeight / 2
        
        // Linha da seta
        ctx.beginPath()
        ctx.moveTo(x - 15, y)
        ctx.lineTo(x + 15, y)
        ctx.stroke()
        
        // Ponta da seta
        ctx.beginPath()
        ctx.moveTo(x + 15, y)
        ctx.lineTo(x + 10, y - 5)
        ctx.lineTo(x + 10, y + 5)
        ctx.closePath()
        ctx.fill()
      }
    },
    
    drawSimpleGeometry(ctx, geometryData) {
      const centerX = this.previewWidth * 0.3
      const centerY = this.previewHeight / 2
      const scale = 50
      
      ctx.fillStyle = '#ef4444'
      ctx.strokeStyle = '#dc2626'
      ctx.lineWidth = 2
      
      switch (geometryData.type) {
        case 'circle':
          const radius = geometryData.params.radius * scale
          ctx.beginPath()
          ctx.arc(centerX, centerY, radius, 0, 2 * Math.PI)
          ctx.fill()
          ctx.stroke()
          break
          
        case 'square':
          const side = geometryData.params.side * scale
          ctx.fillRect(centerX - side/2, centerY - side/2, side, side)
          ctx.strokeRect(centerX - side/2, centerY - side/2, side, side)
          break
          
        case 'rectangle':
          const width = geometryData.params.width * scale
          const height = geometryData.params.height * scale
          ctx.fillRect(centerX - width/2, centerY - height/2, width, height)
          ctx.strokeRect(centerX - width/2, centerY - height/2, width, height)
          break
      }
    },
    
    async runSimulation() {
      this.isSimulating = true
      this.simulationProgress = 0
      this.simulationLogs = []
      this.simulationStatus = 'Inicializando...'
      
      const simulationData = {
        geometry: JSON.parse(localStorage.getItem('taqiCFD_geometry') || '{}'),
        fluid: this.fluidParams,
        boundary: this.boundaryConditions,
        numerical: this.numericalParams,
        timestamp: new Date().toISOString()
      }
      
      try {
        // Simular processo de simulação
        await this.simulateProcess()
        
        // Salvar dados para a página de resultados
        localStorage.setItem('taqiCFD_simulation', JSON.stringify(simulationData))
        
        this.addLog('Simulação concluída com sucesso!')
        this.simulationStatus = 'Concluída'
        
        // Redirecionar para resultados após delay
        setTimeout(() => {
          this.$router.push('/results')
        }, 2000)
        
      } catch (error) {
        this.addLog(`Erro na simulação: ${error.message}`)
        this.simulationStatus = 'Erro'
      } finally {
        this.isSimulating = false
      }
    },
    
    async simulateProcess() {
      const steps = [
        { name: 'Preparando geometria...', duration: 500 },
        { name: 'Gerando malha...', duration: 1000 },
        { name: 'Configurando condições de contorno...', duration: 300 },
        { name: 'Inicializando campos...', duration: 400 },
        { name: 'Executando iterações...', duration: 3000 },
        { name: 'Verificando convergência...', duration: 500 },
        { name: 'Pós-processando resultados...', duration: 800 }
      ]
      
      let totalProgress = 0
      const progressIncrement = 100 / steps.length
      
      for (const step of steps) {
        this.simulationStatus = step.name
        this.addLog(step.name)
        
        await new Promise(resolve => setTimeout(resolve, step.duration))
        
        totalProgress += progressIncrement
        this.simulationProgress = Math.min(100, totalProgress)
      }
    },
    
    addLog(message) {
      const timestamp = new Date().toLocaleTimeString()
      this.simulationLogs.push({ timestamp, message })
      
      // Manter apenas os últimos 20 logs
      if (this.simulationLogs.length > 20) {
        this.simulationLogs.shift()
      }
    },
    
    saveConfiguration() {
      const configData = {
        fluid: this.fluidParams,
        boundary: this.boundaryConditions,
        numerical: this.numericalParams,
        timestamp: new Date().toISOString()
      }
      
      const blob = new Blob([JSON.stringify(configData, null, 2)], {
        type: 'application/json'
      })
      
      const url = URL.createObjectURL(blob)
      const a = document.createElement('a')
      a.href = url
      a.download = `config_simulacao_${Date.now()}.json`
      a.click()
      URL.revokeObjectURL(url)
    },
    
    loadConfiguration() {
      this.$refs.configFileInput.click()
    },
    
    onConfigFileLoad(event) {
      const file = event.target.files[0]
      if (file) {
        const reader = new FileReader()
        reader.onload = (e) => {
          try {
            const config = JSON.parse(e.target.result)
            this.fluidParams = { ...this.fluidParams, ...config.fluid }
            this.boundaryConditions = { ...this.boundaryConditions, ...config.boundary }
            this.numericalParams = { ...this.numericalParams, ...config.numerical }
            
            alert('Configuração carregada com sucesso!')
          } catch (error) {
            alert('Erro ao carregar configuração: formato inválido')
          }
        }
        reader.readAsText(file)
      }
    }
  },
  
  watch: {
    fluidParams: {
      handler() {
        this.drawPreview()
      },
      deep: true
    },
    boundaryConditions: {
      handler() {
        this.drawPreview()
      },
      deep: true
    }
  }
}
</script>

<style scoped>
.simulation-view {
  min-height: calc(100vh - 80px);
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.page-header {
  text-align: center;
  color: white;
  margin-bottom: 30px;
}

.page-header h2 {
  font-size: 2.5em;
  margin-bottom: 10px;
}

.page-header p {
  font-size: 1.2em;
  opacity: 0.9;
}

.simulation-container {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 30px;
  max-width: 1400px;
  margin: 0 auto;
}

.geometry-preview {
  background: white;
  border-radius: 8px;
  padding: 25px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  height: fit-content;
}

.geometry-preview h3 {
  margin-bottom: 20px;
  color: #2c3e50;
}

.geometry-info {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.info-item {
  display: flex;
  justify-content: space-between;
  padding: 8px 0;
  border-bottom: 1px solid #eee;
}

.info-item label {
  font-weight: 500;
  color: #555;
}

.info-item span {
  color: #2c3e50;
  font-weight: 600;
}

.no-geometry {
  text-align: center;
  padding: 20px;
  color: #e67e22;
}

.btn-outline {
  display: inline-block;
  padding: 10px 20px;
  border: 2px solid #3498db;
  color: #3498db;
  text-decoration: none;
  border-radius: 4px;
  margin-top: 10px;
  transition: all 0.3s;
}

.btn-outline:hover {
  background: #3498db;
  color: white;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0,0,0,0.8);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.simulation-modal {
  background: white;
  border-radius: 12px;
  padding: 30px;
  width: 90%;
  max-width: 600px;
  max-height: 80vh;
  overflow-y: auto;
  box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 25px;
}

.modal-header h3 {
  color: #2c3e50;
  margin: 0;
}

.status-indicator {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: #95a5a6;
}

.status-indicator.running {
  background: #27ae60;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% { opacity: 1; }
  50% { opacity: 0.5; }
  100% { opacity: 1; }
}

.progress-container {
  display: flex;
  align-items: center;
  gap: 15px;
  margin-bottom: 25px;
}

.progress-bar {
  flex: 1;
  height: 8px;
  background: #ecf0f1;
  border-radius: 4px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #3498db, #2ecc71);
  transition: width 0.3s ease;
  border-radius: 4px;
}

.log-header {
  font-weight: 500;
  margin-bottom: 10px;
  color: #333;
}

.log-content {
  max-height: 300px;
  overflow-y: auto;
  padding-right: 10px;
}

.log-entry {
  display: flex;
  justify-content: space-between;
  padding: 8px 0;
  border-bottom: 1px solid #eee;
}

.log-time {
  font-size: 0.9em;
  color: #999;
  min-width: 70px;
}

.log-message {
  flex: 1;
  margin-left: 10px;
  font-size: 0.95em;
}

.log-entry.info .log-message {
  color: #3498db;
}

.log-entry.success .log-message {
  color: #27ae60;
}

.log-entry.warning .log-message {
  color: #e67e22;
}

.log-entry.error .log-message {
  color: #e74c3c;
}

@media (max-width: 1024px) {
  .simulation-container {
    grid-template-columns: 1fr;
  }
  
  .simulation-config {
    order: 1;
  }
  
  .geometry-preview {
    order: 2;
  }
  
  .modal-header {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .modal-header h3 {
    margin-bottom: 10px;
  }
}
</style>

