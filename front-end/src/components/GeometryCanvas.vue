<template>
  <div class="geometry-canvas-container">
    <div class="canvas-header">
      <h3>Definir Geometria</h3>
      <div class="geometry-controls">
        <select v-model="selectedShape" @change="createShape">
          <option value="rectangle">Retângulo</option>
          <option value="circle">Círculo</option>
          <option value="polygon">Polígono</option>
          <option value="custom">Desenho Livre</option>
        </select>
      </div>
    </div>
    
    <canvas
      ref="canvas"
      :width="canvasWidth"
      :height="canvasHeight"
      @mousedown="startDrawing"
      @mousemove="draw"
      @mouseup="stopDrawing"
      class="geometry-canvas"
    ></canvas>
    
    <div class="geometry-params">
      <div class="param-group" v-if="selectedShape === 'rectangle'">
        <label>Largura (m):</label>
        <input type="number" v-model="geometryParams.width" @input="updateGeometry" step="0.1" min="0.1">
        <label>Altura (m):</label>
        <input type="number" v-model="geometryParams.height" @input="updateGeometry" step="0.1" min="0.1">
      </div>
      
      <div class="param-group" v-if="selectedShape === 'circle'">
        <label>Raio (m):</label>
        <input type="number" v-model="geometryParams.radius" @input="updateGeometry" step="0.1" min="0.1">
      </div>
      
      <div class="param-group">
        <label>Domínio - Largura (m):</label>
        <input type="number" v-model="domainParams.width" step="0.5" min="1">
        <label>Domínio - Altura (m):</label>
        <input type="number" v-model="domainParams.height" step="0.5" min="1">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'GeometryCanvas',
  data() {
    return {
      selectedShape: 'rectangle',
      canvasWidth: 800,
      canvasHeight: 600,
      isDrawing: false,
      geometryParams: {
        width: 2.0,
        height: 1.0,
        radius: 1.0
      },
      domainParams: {
        width: 10.0,
        height: 8.0
      }
    }
  },
  mounted() {
    this.initCanvas();
    this.createShape();
  },
  methods: {
    initCanvas() {
      const canvas = this.$refs.canvas;
      this.ctx = canvas.getContext('2d');
      this.ctx.fillStyle = '#f0f8ff';
      this.ctx.fillRect(0, 0, this.canvasWidth, this.canvasHeight);
    },
    
    createShape() {
      this.clearCanvas();
      this.drawDomain();
      
      const centerX = this.canvasWidth / 2;
      const centerY = this.canvasHeight / 2;
      const scale = 50; // pixels per meter
      
      this.ctx.fillStyle = '#4CAF50';
      this.ctx.strokeStyle = '#2E7D32';
      this.ctx.lineWidth = 2;
      
      switch(this.selectedShape) {
        case 'rectangle':
          const width = this.geometryParams.width * scale;
          const height = this.geometryParams.height * scale;
          this.ctx.fillRect(centerX - width/2, centerY - height/2, width, height);
          this.ctx.strokeRect(centerX - width/2, centerY - height/2, width, height);
          break;
          
        case 'circle':
          const radius = this.geometryParams.radius * scale;
          this.ctx.beginPath();
          this.ctx.arc(centerX, centerY, radius, 0, 2 * Math.PI);
          this.ctx.fill();
          this.ctx.stroke();
          break;
      }
    },
    
    drawDomain() {
      this.ctx.strokeStyle = '#1976D2';
      this.ctx.lineWidth = 3;
      this.ctx.setLineDash([10, 5]);
      this.ctx.strokeRect(50, 50, this.canvasWidth - 100, this.canvasHeight - 100);
      this.ctx.setLineDash([]);
    },
    
    clearCanvas() {
      this.ctx.clearRect(0, 0, this.canvasWidth, this.canvasHeight);
      this.ctx.fillStyle = '#f0f8ff';
      this.ctx.fillRect(0, 0, this.canvasWidth, this.canvasHeight);
    },
    
    updateGeometry() {
      this.createShape();
      this.$emit('geometry-changed', {
        shape: this.selectedShape,
        params: this.geometryParams,
        domain: this.domainParams
      });
    },
    
    startDrawing(e) {
      if (this.selectedShape === 'custom') {
        this.isDrawing = true;
      }
    },
    
    draw(e) {
      if (!this.isDrawing) return;
      
      const rect = this.$refs.canvas.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      
      this.ctx.lineTo(x, y);
      this.ctx.stroke();
      this.ctx.beginPath();
      this.ctx.moveTo(x, y);
    },
    
    stopDrawing() {
      this.isDrawing = false;
      this.ctx.beginPath();
    }
  }
}
</script>

<style scoped>
.geometry-canvas-container {
  background: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.canvas-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}

.geometry-controls select {
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
}

.geometry-canvas {
  border: 2px solid #ddd;
  border-radius: 4px;
  cursor: crosshair;
  display: block;
  margin: 0 auto;
}

.geometry-params {
  margin-top: 20px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

.param-group {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.param-group label {
  font-weight: 500;
  color: #333;
}

.param-group input {
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
}
</style>
