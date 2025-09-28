<template>
  <div class="cfd-visualization w-full h-full">
    <!-- Header com controles -->
    <div class="bg-white shadow-md p-4 mb-4 rounded-lg">
      <div class="flex justify-between items-center">
        <h2 class="text-xl font-bold text-gray-800">Visualização CFD</h2>
        <div class="flex space-x-2">
          <select v-model="activeField" @change="updateVisualization" 
                  class="px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500">
            <option value="velocity_magnitude">Magnitude da Velocidade</option>
            <option value="velocity_u">Velocidade U</option>
            <option value="velocity_v">Velocidade V</option>
            <option value="pressure">Pressão</option>
            <option value="streamlines">Linhas de Fluxo</option>
          </select>
          <button @click="exportResults" 
                  class="px-4 py-2 bg-green-600 text-white rounded-md hover:bg-green-700 transition-colors">
            Exportar
          </button>
        </div>
      </div>
    </div>

    <!-- Área de plotagem -->
    <div class="bg-white rounded-lg shadow-md p-4">
      <div id="plotly-div" class="w-full" style="height: 600px;"></div>
      
      <!-- Loading overlay -->
      <div v-if="isLoading" class="absolute inset-0 bg-white bg-opacity-80 flex items-center justify-center rounded-lg">
        <div class="text-center">
          <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
          <p class="text-gray-600">Gerando visualização...</p>
        </div>
      </div>
    </div>

    <!-- Legenda e informações -->
    <div class="mt-4 grid grid-cols-1 md:grid-cols-3 gap-4">
      <div class="bg-blue-50 p-4 rounded-lg">
        <h3 class="font-semibold text-blue-800">Reynolds</h3>
        <p class="text-2xl font-bold text-blue-600">{{ formatNumber(metadata.reynolds_number) }}</p>
      </div>
      <div class="bg-green-50 p-4 rounded-lg">
        <h3 class="font-semibold text-green-800">Malha</h3>
        <p class="text-lg text-green-600">{{ metadata.mesh_size?.join(' × ') || 'N/A' }}</p>
      </div>
      <div class="bg-purple-50 p-4 rounded-lg">
        <h3 class="font-semibold text-purple-800">Tempo</h3>
        <p class="text-lg text-purple-600">{{ formatTime(computationTime) }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import Plotly from 'plotly.js-dist'

export default {
  name: 'CFDVisualization',
  props: {
    predictionData: {
      type: Object,
      default: () => ({})
    },
    metadata: {
      type: Object,
      default: () => ({})
    },
    isLoading: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      activeField: 'velocity_magnitude',
      computationTime: 0
    }
  },
  mounted() {
    this.initializePlot()
  },
  watch: {
    predictionData: {
      handler(newData) {
        if (newData && Object.keys(newData).length > 0) {
          this.updateVisualization()
        }
      },
      deep: true
    }
  },
  methods: {
    initializePlot() {
      const layout = {
        title: 'Simulação CFD - taqiCFD',
        xaxis: { title: 'X (m)' },
        yaxis: { title: 'Y (m)' },
        showlegend: true,
        coloraxis: {
          colorbar: { title: 'Magnitude' }
        }
      }
      
      Plotly.newPlot('plotly-div', [], layout, {
        responsive: true,
        displayModeBar: true,
        modeBarButtonsToAdd: ['drawclosedpath', 'eraseshape']
      })
    },

    updateVisualization() {
      const startTime = Date.now()
      
      if (!this.predictionData || Object.keys(this.predictionData).length === 0) return

      let plotData = []
      
      try {
        switch (this.activeField) {
          case 'velocity_magnitude':
            plotData = this.createVelocityMagnitudePlot()
            break
          case 'velocity_u':
            plotData = this.createScalarPlot(this.predictionData.velocity_u, 'Velocidade U (m/s)')
            break
          case 'velocity_v':
            plotData = this.createScalarPlot(this.predictionData.velocity_v, 'Velocidade V (m/s)')
            break
          case 'pressure':
            plotData = this.createScalarPlot(this.predictionData.pressure, 'Pressão (Pa)')
            break
          case 'streamlines':
            plotData = this.createStreamlinesPlot()
            break
        }

        Plotly.react('plotly-div', plotData)
        this.computationTime = Date.now() - startTime
        
      } catch (error) {
        console.error('Erro na visualização:', error)
      }
    },

    createVelocityMagnitudePlot() {
      const u = this.predictionData.velocity_u
      const v = this.predictionData.velocity_v
      
      // Calcular magnitude da velocidade
      const magnitude = u.map((row, i) => 
        row.map((uVal, j) => Math.sqrt(uVal**2 + v[i][j]**2))
      )

      return [{
        z: magnitude,
        type: 'heatmap',
        colorscale: 'Viridis',
        name: 'Magnitude da Velocidade'
      }]
    },

    createScalarPlot(data, title) {
      return [{
        z: data,
        type: 'heatmap',
        colorscale: 'RdBu',
        name: title
      }]
    },

    createStreamlinesPlot() {
      // Implementar linhas de fluxo usando quiver plot
      const u = this.predictionData.velocity_u
      const v = this.predictionData.velocity_v
      
      // Downsampling for better performance
      const step = 3
      const x = []
      const y = []
      const uSample = []
      const vSample = []

      for (let i = 0; i < u.length; i += step) {
        for (let j = 0; j < u[i].length; j += step) {
          x.push(j)
          y.push(i)
          uSample.push(u[i][j])
          vSample.push(v[i][j])
        }
      }

      return [{
        x: x,
        y: y,
        u: uSample,
        v: vSample,
        type: 'scatter',
        mode: 'markers',
        marker: {
          symbol: 'arrow',
          angle: uSample.map((u, i) => Math.atan2(vSample[i], u) * 180 / Math.PI),
          size: uSample.map((u, i) => Math.sqrt(u**2 + vSample[i]**2) * 10)
        }
      }]
    },

    exportResults() {
      const data = {
        prediction: this.predictionData,
        metadata: this.metadata,
        timestamp: new Date().toISOString()
      }
      
      const blob = new Blob([JSON.stringify(data, null, 2)], { 
        type: 'application/json' 
      })
      
      const url = URL.createObjectURL(blob)
      const link = document.createElement('a')
      link.href = url
      link.download = `cfd_results_${Date.now()}.json`
      link.click()
      
      URL.revokeObjectURL(url)
    },

    formatNumber(num) {
      return num ? num.toLocaleString('pt-BR', { 
        maximumFractionDigits: 2 
      }) : 'N/A'
    },

    formatTime(ms) {
      return `${ms}ms`
    }
  }
}
</script>

<style scoped>
.cfd-visualization {
  position: relative;
}
</style>