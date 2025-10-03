<template>
  <div class="results-viewer">
    <div class="results-header">
      <h3>Resultados da Simulação</h3>
      <div class="results-controls">
        <select v-model="selectedField" @change="updateVisualization">
          <option value="velocity">Campo de Velocidade</option>
          <option value="pressure">Campo de Pressão</option>
          <option value="streamlines">Linhas de Corrente</option>
          <option value="vorticity">Vorticidade</option>
        </select>
        <button @click="exportResults" class="btn btn-export">Exportar Resultados</button>
      </div>
    </div>
    
    <div class="results-content">
      <div class="visualization-panel">
        <canvas
          ref="resultsCanvas"
          :width="canvasWidth"
          :height="canvasHeight"
          class="results-canvas"
        ></canvas>
        
        <div class="color-scale" v-if="colorScale">
          <div class="scale-title">{{ getFieldTitle(selectedField) }}</div>
          <div class="scale-bar">
            <div class="scale-gradient" :style="{ background: colorScale.gradient }"></div>
            <div class="scale-labels">
              <span>{{ colorScale.min }}</span>
              <span>{{ colorScale.max }}</span>
            </div>
          </div>
          <div class="scale-unit">{{ colorScale.unit }}</div>
        </div>
      </div>
      
      <div class="analysis-panel">
        <div class="statistics">
          <h4>Estatísticas</h4>
          <div class="stat-item">
            <label>Velocidade Máxima:</label>
            <span>{{ results.maxVelocity?.toFixed(3) }} m/s</span>
          </div>
          <div class="stat-item">
            <label>Pressão Máxima:</label>
            <span>{{ results.maxPressure?.toFixed(2) }} Pa</span>
          </div>
          <div class="stat-item">
            <label>Pressão Mínima:</label>
            <span>{{ results.minPressure?.toFixed(2) }} Pa</span>
          </div>
          <div class="stat-item">
            <label>Coeficiente de Arrasto (Cd):</label>
            <span>{{ results.dragCoefficient?.toFixed(4) }}</span>
          </div>
          <div class="stat-item">
            <label>Coeficiente de Sustentação (Cl):</label>
            <span>{{ results.liftCoefficient?.toFixed(4) }}</span>
          </div>
          <div class="stat-item">
            <label>Tempo de Simulação:</label>
            <span>{{ results.simulationTime }} s</span>
          </div>
          <div class="stat-item">
            <label>Convergência:</label>
            <span class="convergence-status" :class="{ converged: results.converged }">
              {{ results.converged ? 'Convergiu' : 'Não Convergiu' }}
            </span>
          </div>
        </div>
        
        <div class="convergence-plot">
          <h4>Histórico de Convergência</h4>
          <canvas ref="convergenceCanvas" width="300" height="200" class="convergence-canvas"></canvas>
        </div>
        
        <div class="export-options">
          <h4>Opções de Exportação</h4>
          <button @click="exportData('csv')" class="export-btn">Exportar Dados (CSV)</button>
          <button @click="exportData('vtk')" class="export-btn">Exportar Malha (VTK)</button>
          <button @click="exportImage('png')" class="export-btn">Salvar Imagem (PNG)</button>
          <button @click="generateReport" class="export-btn">Gerar Relatório (PDF)</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ResultsViewer',
  props: {
    simulationResults: {
      type: Object,
      default: () => ({})
    }
  },
  data() {
    return {
      selectedField: 'velocity',
      canvasWidth: 600,
      canvasHeight: 400,
      results: {
        maxVelocity: 2.5,
        maxPressure: 150,
        minPressure: -100,
        dragCoefficient: 1.2,
        liftCoefficient: 0.15,
        simulationTime: '45.2',
        converged: true,
        convergenceHistory: [0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001]
      },
      colorScale: null
    }
  },
  mounted() {
    this.initializeVisualization();
    this.drawConvergencePlot();
  },
  methods: {
    initializeVisualization() {
      const canvas = this.$refs.resultsCanvas;
      const ctx = canvas.getContext('2d');
      
      // Simular visualização de campo de velocidade
      this.drawVelocityField(ctx);
      this.updateColorScale();
    },
    
    drawVelocityField(ctx) {
      // Limpar canvas
      ctx.fillStyle = '#f0f8ff';
      ctx.fillRect(0, 0, this.canvasWidth, this.canvasHeight);
      
      // Desenhar geometria
      ctx.fillStyle = '#4CAF50';
      const centerX = this.canvasWidth / 2;
      const centerY = this.canvasHeight / 2;
      ctx.fillRect(centerX - 50, centerY - 30, 100, 60);
      
      // Simular vetores de velocidade
      ctx.strokeStyle = '#1976D2';
      ctx.lineWidth = 2;
      
      for (let x = 50; x < this.canvasWidth - 50; x += 30) {
        for (let y = 50; y < this.canvasHeight - 50; y += 30) {
          // Pular área da geometria
          if (x > centerX - 60 && x < centerX + 60 && y > centerY - 40 && y < centerY + 40) continue;
          
          // Simular campo de velocidade ao redor do objeto
          let vx = 2 + Math.random() * 0.5;
          let vy = (Math.random() - 0.5) * 0.3;
          
          // Desenhar vetor
          this.drawArrow(ctx, x, y, vx * 10, vy * 10);
        }
      }
    },
    
    drawArrow(ctx, x, y, dx, dy) {
      ctx.beginPath();
      ctx.moveTo(x, y);
      ctx.lineTo(x + dx, y + dy);
      ctx.stroke();
      
      // Ponta da seta
      const angle = Math.atan2(dy, dx);
      const arrowLength = 5;
      ctx.beginPath();
      ctx.moveTo(x + dx, y + dy);
      ctx.lineTo(x + dx - arrowLength * Math.cos(angle - Math.PI / 6), 
                 y + dy - arrowLength * Math.sin(angle - Math.PI / 6));
      ctx.moveTo(x + dx, y + dy);
      ctx.lineTo(x + dx - arrowLength * Math.cos(angle + Math.PI / 6), 
                 y + dy - arrowLength * Math.sin(angle + Math.PI / 6));
      ctx.stroke();
    },
    
    updateVisualization() {
      const canvas = this.$refs.resultsCanvas;
      const ctx = canvas.getContext('2d');
      
      switch(this.selectedField) {
        case 'velocity':
          this.drawVelocityField(ctx);
          break;
        case 'pressure':
          this.drawPressureField(ctx);
          break;
        case 'streamlines':
          this.drawStreamlines(ctx);
          break;
      }
      
      this.updateColorScale();
    },
    
    drawPressureField(ctx) {
      // Implementar visualização de pressão com cores
      ctx.fillStyle = '#f0f8ff';
      ctx.fillRect(0, 0, this.canvasWidth, this.canvasHeight);
      
      // Simular campo de pressão com gradiente de cores
      for (let x = 0; x < this.canvasWidth; x += 10) {
        for (let y = 0; y < this.canvasHeight; y += 10) {
          const pressure = Math.sin(x / 50) * Math.cos(y / 50);
          const color = this.pressureToColor(pressure);
          ctx.fillStyle = color;
          ctx.fillRect(x, y, 10, 10);
        }
      }
    },
    
    pressureToColor(pressure) {
      // Converter pressão em cor (azul para baixa, vermelho para alta)
      const normalized = (pressure + 1) / 2; // -1 to 1 -> 0 to 1
      const red = Math.floor(255 * normalized);
      const blue = Math.floor(255 * (1 - normalized));
      return `rgb(${red}, 0, ${blue})`;
    },
    
    drawStreamlines(ctx) {
      // Implementar desenho de linhas de corrente
      ctx.fillStyle = '#f0f8ff';
      ctx.fillRect(0, 0, this.canvasWidth, this.canvasHeight);
      
      ctx.strokeStyle = '#1976D2';
      ctx.lineWidth = 2;
      
      // Simular linhas de corrente
      for (let y = 100; y < this.canvasHeight - 100; y += 40) {
        ctx.beginPath();
        ctx.moveTo(50, y);
        
        for (let x = 50; x < this.canvasWidth - 50; x += 5) {
          const streamY = y + 20 * Math.sin((x - 200) / 100);
          ctx.lineTo(x, streamY);
        }
        
        ctx.stroke();
      }
    },
    
    updateColorScale() {
      switch(this.selectedField) {
        case 'velocity':
          this.colorScale = {
            gradient: 'linear-gradient(to right, blue, green, yellow, red)',
            min: '0',
            max: '2.5',
            unit: 'm/s'
          };
          break;
        case 'pressure':
          this.colorScale = {
            gradient: 'linear-gradient(to right, blue, cyan, yellow, red)',
            min: '-100',
            max: '150',
            unit: 'Pa'
          };
          break;
      }
    },
    
    drawConvergencePlot() {
      const canvas = this.$refs.convergenceCanvas;
      const ctx = canvas.getContext('2d');
      
      ctx.fillStyle = 'white';
      ctx.fillRect(0, 0, 300, 200);
      
      ctx.strokeStyle = '#333';
      ctx.lineWidth = 1;
      
      // Eixos
      ctx.beginPath();
      ctx.moveTo(30, 170);
      ctx.lineTo(270, 170);
      ctx.moveTo(30, 170);
      ctx.lineTo(30, 30);
      ctx.stroke();
      
      // Dados de convergência
      const data = this.results.convergenceHistory;
      ctx.strokeStyle = '#e74c3c';
      ctx.lineWidth = 2;
      ctx.beginPath();
      
      for (let i = 0; i < data.length; i++) {
        const x = 30 + (i / (data.length - 1)) * 240;
        const y = 170 - (Math.log10(data[i] + 0.0001) + 4) * 35;
        
        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }
      
      ctx.stroke();
      
      // Labels
      ctx.fillStyle = '#333';
      ctx.font = '10px Arial';
      ctx.fillText('Iterações', 120, 190);
      ctx.save();
      ctx.translate(15, 100);
      ctx.rotate(-Math.PI / 2);
      ctx.fillText('Resíduo', 0, 0);
      ctx.restore();
    },
    
    getFieldTitle(field) {
      const titles = {
        velocity: 'Velocidade',
        pressure: 'Pressão',
        streamlines: 'Linhas de Corrente',
        vorticity: 'Vorticidade'
      };
      return titles[field] || field;
    },
    
    exportResults() {
      this.$emit('export-results', {
        field: this.selectedField,
        results: this.results
      });
    },
    
    exportData(format) {
      console.log(`Exportando dados em formato ${format}`);
      // Implementar exportação
    },
    
    exportImage(format) {
      const canvas = this.$refs.resultsCanvas;
      const link = document.createElement('a');
      link.download = `taqiCFD_results.${format}`;
      link.href = canvas.toDataURL();
      link.click();
    },
    
    generateReport() {
      console.log('Gerando relatório PDF...');
      // Implementar geração de relatório
    }
  }
}
</script>

<style scoped>
.results-viewer {
  background: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.results-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.results-controls {
  display: flex;
  gap: 15px;
  align-items: center;
}

.results-controls select {
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.results-content {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 30px;
}

.visualization-panel {
  position: relative;
}

.results-canvas {
  border: 2px solid #ddd;
  border-radius: 4px;
  display: block;
  margin-bottom: 15px;
}

.color-scale {
  background: #f8f9fa;
  padding: 15px;
  border-radius: 4px;
}

.scale-title {
  font-weight: 500;
  margin-bottom: 10px;
  text-align: center;
}

.scale-bar {
  position: relative;
  margin-bottom: 10px;
}

.scale-gradient {
  height: 20px;
  border-radius: 2px;
  border: 1px solid #ddd;
}

.scale-labels {
  display: flex;
  justify-content: space-between;
  margin-top: 5px;
  font-size: 12px;
}

.scale-unit {
  text-align: center;
  font-size: 12px;
  color: #666;
}

.analysis-panel {
  display: flex;
  flex-direction: column;
  gap: 25px;
}

.statistics h4 {
  margin-bottom: 15px;
  color: #2c3e50;
}

.stat-item {
  display: flex;
  justify-content: space-between;
  margin-bottom: 8px;
  padding: 5px 0;
  border-bottom: 1px solid #eee;
}

.stat-item label {
  font-weight: 500;
}

.convergence-status.converged {
  color: #27ae60;
  font-weight: 500;
}

.convergence-canvas {
  border: 1px solid #ddd;
  border-radius: 4px;
}

.export-options {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.export-btn {
  padding: 8px 16px;
  border: 1px solid #3498db;
  background: white;
  color: #3498db;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.3s;
}

.export-btn:hover {
  background: #3498db;
  color: white;
}

.btn-export {
  padding: 8px 16px;
  background: #27ae60;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.btn-export:hover {
  background: #219a52;
}
</style>