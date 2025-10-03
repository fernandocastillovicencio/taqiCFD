<template>
  <div class="simulation-config">
    <h3>Configurações da Simulação</h3>
    
    <div class="config-sections">
      <div class="section">
        <h4>Condições de Contorno</h4>
        <div class="form-group">
          <label>Velocidade de Entrada (m/s):</label>
          <input type="number" v-model="config.inlet.velocity" step="0.1" min="0">
        </div>
        
        <div class="form-group">
          <label>Pressão de Saída (Pa):</label>
          <input type="number" v-model="config.outlet.pressure" step="100">
        </div>
        
        <div class="form-group">
          <label>Condição das Paredes:</label>
          <select v-model="config.walls.condition">
            <option value="noSlip">No Slip (Parede Sólida)</option>
            <option value="slip">Slip (Parede Deslizante)</option>
            <option value="symmetry">Simetria</option>
          </select>
        </div>
      </div>
      
      <div class="section">
        <h4>Propriedades do Fluido</h4>
        <div class="form-group">
          <label>Tipo de Fluido:</label>
          <select v-model="config.fluid.type" @change="updateFluidProperties">
            <option value="air">Ar (20°C)</option>
            <option value="water">Água (20°C)</option>
            <option value="custom">Personalizado</option>
          </select>
        </div>
        
        <div class="form-group">
          <label>Densidade (kg/m³):</label>
          <input type="number" v-model="config.fluid.density" step="0.1" :disabled="config.fluid.type !== 'custom'">
        </div>
        
        <div class="form-group">
          <label>Viscosidade Dinâmica (Pa·s):</label>
          <input type="number" v-model="config.fluid.viscosity" step="0.00001" :disabled="config.fluid.type !== 'custom'">
        </div>
      </div>
      
      <div class="section">
        <h4>Parâmetros de Simulação</h4>
        <div class="form-group">
          <label>Solver:</label>
          <select v-model="config.solver.type">
            <option value="simpleFoam">simpleFoam (Turbulento, Estacionário)</option>
            <option value="icoFoam">icoFoam (Laminar, Transiente)</option>
            <option value="pisoFoam">pisoFoam (Turbulento, Transiente)</option>
          </select>
        </div>
        
        <div class="form-group">
          <label>Número de Iterações:</label>
          <input type="number" v-model="config.solver.iterations" min="100" step="100">
        </div>
        
        <div class="form-group">
          <label>Tolerância de Convergência:</label>
          <input type="number" v-model="config.solver.tolerance" step="0.00001" min="0.00001">
        </div>
        
        <div class="form-group">
          <label>Modelo de Turbulência:</label>
          <select v-model="config.turbulence.model" v-if="config.solver.type !== 'icoFoam'">
            <option value="kEpsilon">k-ε</option>
            <option value="kOmega">k-ω</option>
            <option value="kOmegaSST">k-ω SST</option>
          </select>
        </div>
      </div>
      
      <div class="section">
        <h4>Configuração de Malha</h4>
        <div class="form-group">
          <label>Células em X:</label>
          <input type="number" v-model="config.mesh.cellsX" min="10" step="5">
        </div>
        
        <div class="form-group">
          <label>Células em Y:</label>
          <input type="number" v-model="config.mesh.cellsY" min="10" step="5">
        </div>
        
        <div class="form-group">
          <label>Tipo de Malha:</label>
          <select v-model="config.mesh.type">
            <option value="structured">Estruturada (blockMesh)</option>
            <option value="unstructured">Não Estruturada (snappyHexMesh)</option>
          </select>
        </div>
      </div>
    </div>
    
    <div class="action-buttons">
      <button @click="validateConfig" class="btn btn-secondary">Validar Configuração</button>
      <button @click="startSimulation" class="btn btn-primary" :disabled="!isValid">Iniciar Simulação</button>
    </div>
    
    <div v-if="validationErrors.length > 0" class="validation-errors">
      <h4>Erros de Validação:</h4>
      <ul>
        <li v-for="error in validationErrors" :key="error">{{ error }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SimulationConfig',
  data() {
    return {
      config: {
        inlet: {
          velocity: 2.0
        },
        outlet: {
          pressure: 0
        },
        walls: {
          condition: 'noSlip'
        },
        fluid: {
          type: 'air',
          density: 1.225,
          viscosity: 0.0000181
        },
        solver: {
          type: 'simpleFoam',
          iterations: 1000,
          tolerance: 0.001
        },
        turbulence: {
          model: 'kEpsilon'
        },
        mesh: {
          cellsX: 50,
          cellsY: 30,
          type: 'structured'
        }
      },
      validationErrors: [],
      isValid: true
    }
  },
  methods: {
    updateFluidProperties() {
      const fluidProperties = {
        air: { density: 1.225, viscosity: 0.0000181 },
        water: { density: 998.2, viscosity: 0.001003 }
      };
      
      if (this.config.fluid.type in fluidProperties) {
        this.config.fluid.density = fluidProperties[this.config.fluid.type].density;
        this.config.fluid.viscosity = fluidProperties[this.config.fluid.type].viscosity;
      }
    },
    
    validateConfig() {
      this.validationErrors = [];
      
      if (this.config.inlet.velocity <= 0) {
        this.validationErrors.push('Velocidade de entrada deve ser maior que zero');
      }
      
      if (this.config.fluid.density <= 0) {
        this.validationErrors.push('Densidade deve ser maior que zero');
      }
      
      if (this.config.fluid.viscosity <= 0) {
        this.validationErrors.push('Viscosidade deve ser maior que zero');
      }
      
      if (this.config.solver.iterations < 100) {
        this.validationErrors.push('Número mínimo de iterações é 100');
      }
      
      if (this.config.mesh.cellsX < 10 || this.config.mesh.cellsY < 10) {
        this.validationErrors.push('Número mínimo de células é 10 em cada direção');
      }
      
      this.isValid = this.validationErrors.length === 0;
    },
    
    startSimulation() {
      this.validateConfig();
      if (this.isValid) {
        this.$emit('start-simulation', this.config);
      }
    }
  },
  
  mounted() {
    this.validateConfig();
  }
}
</script>

<style scoped>
.simulation-config {
  background: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.config-sections {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 30px;
  margin: 20px 0;
}

.section {
  background: #f8f9fa;
  padding: 20px;
  border-radius: 6px;
}

.section h4 {
  margin-bottom: 15px;
  color: #2c3e50;
  border-bottom: 2px solid #3498db;
  padding-bottom: 5px;
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
.form-group select {
  width: 100%;
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
}

.form-group input:disabled {
  background-color: #f5f5f5;
  color: #999;
}

.action-buttons {
  display: flex;
  gap: 15px;
  justify-content: center;
  margin-top: 30px;
}

.btn {
  padding: 12px 24px;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  transition: background-color 0.3s;
}

.btn-primary {
  background-color: #3498db;
  color: white;
}

.btn-primary:hover:not(:disabled) {
  background-color: #2980b9;
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
}

.validation-errors {
  margin-top: 20px;
  padding: 15px;
  background-color: #ffe6e6;
  border: 1px solid #ff9999;
  border-radius: 4px;
  color: #d63031;
}

.validation-errors ul {
  margin: 10px 0 0 20px;
}
</style>