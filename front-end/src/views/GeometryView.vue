<template>
  <div class="geometry-view">
    <div class="page-header">
      <h2>Definição de Geometria</h2>
      <p>Configure a geometria do objeto e o domínio de simulação</p>
    </div>
    
    <div class="geometry-container">
      <GeometryCanvas 
        @geometry-changed="handleGeometryChange"
        ref="geometryCanvas"
      />
      
      <div class="geometry-summary">
        <h3>Resumo da Configuração</h3>
        <div class="summary-item" v-if="geometryData">
          <label>Tipo de Geometria:</label>
          <span>{{ getShapeName(geometryData.shape) }}</span>
        </div>
        
        <div class="summary-section" v-if="geometryData?.params">
          <h4>Dimensões do Objeto</h4>
          <div class="summary-item" v-for="(value, key) in geometryData.params" :key="key">
            <label>{{ getParamLabel(key) }}:</label>
            <span>{{ value }} m</span>
          </div>
        </div>
        
        <div class="summary-section" v-if="geometryData?.domain">
          <h4>Domínio de Simulação</h4>
          <div class="summary-item">
            <label>Largura:</label>
            <span>{{ geometryData.domain.width }} m</span>
          </div>
          <div class="summary-item">
            <label>Altura:</label>
            <span>{{ geometryData.domain.height }} m</span>
          </div>
          <div class="summary-item">
            <label>Área:</label>
            <span>{{ (geometryData.domain.width * geometryData.domain.height).toFixed(2) }} m²</span>
          </div>
        </div>
        
        <div class="action-buttons">
          <button @click="saveGeometry" class="btn btn-secondary">Salvar Geometria</button>
          <button @click="proceedToSimulation" class="btn btn-primary" :disabled="!geometryData">
            Prosseguir para Simulação
          </button>
        </div>
      </div>
    </div>
    
    <!-- Modal de confirmação -->
    <div v-if="showSaveModal" class="modal-overlay" @click="closeSaveModal">
      <div class="modal" @click.stop>
        <h3>Salvar Geometria</h3>
        <div class="form-group">
          <label>Nome da Geometria:</label>
          <input type="text" v-model="geometryName" placeholder="Ex: Cilindro 2D">
        </div>
        <div class="form-group">
          <label>Descrição:</label>
          <textarea v-model="geometryDescription" placeholder="Descrição opcional..."></textarea>
        </div>
        <div class="modal-actions">
          <button @click="closeSaveModal" class="btn btn-secondary">Cancelar</button>
          <button @click="confirmSave" class="btn btn-primary">Salvar</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import GeometryCanvas from '@/components/GeometryCanvas.vue';

export default {
  name: 'GeometryView',
  components: {
    GeometryCanvas
  },
  data() {
    return {
      geometryData: null,
      showSaveModal: false,
      geometryName: '',
      geometryDescription: ''
    }
  },
  methods: {
    handleGeometryChange(data) {
      this.geometryData = data;
    },
    
    getShapeName(shape) {
      const names = {
        rectangle: 'Retângulo',
        circle: 'Círculo',
        polygon: 'Polígono',
        custom: 'Desenho Personalizado'
      };
      return names[shape] || shape;
    },
    
    getParamLabel(param) {
      const labels = {
        width: 'Largura',
        height: 'Altura',
        radius: 'Raio'
      };
      return labels[param] || param;
    },
    
    saveGeometry() {
      this.showSaveModal = true;
    },
    
    closeSaveModal() {
      this.showSaveModal = false;
      this.geometryName = '';
      this.geometryDescription = '';
    },
    
    async confirmSave() {
      try {
        const geometryPayload = {
          name: this.geometryName,
          description: this.geometryDescription,
          shape: this.geometryData.shape,
          parameters: this.geometryData.params,
          domain: this.geometryData.domain,
          timestamp: new Date().toISOString()
        };
        
        // Aqui seria feita a chamada para a API
        console.log('Salvando geometria:', geometryPayload);
        
        // Simular salvamento
        await new Promise(resolve => setTimeout(resolve, 1000));
        
        this.$toast.success('Geometria salva com sucesso!');
        this.closeSaveModal();
        
      } catch (error) {
        console.error('Erro ao salvar geometria:', error);
        this.$toast.error('Erro ao salvar geometria');
      }
    },
    
    proceedToSimulation() {
      if (this.geometryData) {
        // Salvar dados da geometria para a próxima página
        this.$store.commit('setGeometryData', this.geometryData);
        this.$router.push('/simulation');
      }
    }
  }
}
</script>

<style scoped>
.geometry-view {
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

.geometry-container {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 30px;
  max-width: 1400px;
  margin: 0 auto;
}

.geometry-summary {
  background: white;
  border-radius: 8px;
  padding: 25px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  height: fit-content;
}

.geometry-summary h3 {
  margin-bottom: 20px;
  color: #2c3e50;
}

.summary-section {
  margin-bottom: 20px;
  padding-bottom: 15px;
  border-bottom: 1px solid #eee;
}

.summary-section h4 {
  color: #34495e;
  margin-bottom: 10px;
  font-size: 1.1em;
}

.summary-item {
  display: flex;
  justify-content: space-between;
  margin-bottom: 8px;
}

.summary-item label {
  font-weight: 500;
  color: #555;
}

.summary-item span {
  color: #2c3e50;
  font-weight: 600;
}

.action-buttons {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-top: 25px;
}

.btn {
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s;
}

.btn-primary {
  background-color: #3498db;
  color: white;
}

.btn-primary:hover:not(:disabled) {
  background-color: #2980b9;
  transform: translateY(-1px);
}

.btn-primary:disabled {
  background-color: #bdc3c7;
  cursor: not-allowed;
}

.btn-secondary {
  background-color: #95a5a6;
  color: white;
}

.btn-secondary:hover {
  background-color: #7f8c8d;
  transform: translateY(-1px);
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0,0,0,0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal {
  background: white;
  border-radius: 8px;
  padding: 25px;
  width: 90%;
  max-width: 500px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.3);
}

.modal h3 {
  margin-bottom: 20px;
  color: #2c3e50;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: 500;
  color: #555;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
}

.form-group textarea {
  resize: vertical;
  min-height: 80px;
}

.modal-actions {
  display: flex;
  gap: 10px;
  justify-content: flex-end;
  margin-top: 20px;
}
</style>
