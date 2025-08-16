<template>
  <div class="geometry-container">
    <h2>Geometry Setup</h2>
    <p>Select or draw a geometry.</p>

    <!-- Barra Superior -->
    <div class="toolbar">
      <button @click="addCircle">🟡</button>
      <button @click="addSquare">⬜</button>
      <button @click="addTriangle">🔺</button>
      <button @click="enableDrawing">✏️</button>
      <button @click="clearCanvas">❌</button>
    </div>

    <!-- Barra de Dimensões -->
    <div class="dimension-bar">
      <label>Units:</label>
      <select v-model="selectedUnit">
        <option value="m">m</option>
        <option value="cm">cm</option>
        <option value="mm">mm</option>
      </select>

      <label>Width:</label>
      <input type="range" min="10" max="300" v-model="width" @input="updateSize" />
      <span>{{ width }} {{ selectedUnit }}</span>

      <label>Height:</label>
      <input type="range" min="10" max="300" v-model="height" @input="updateSize" />
      <span>{{ height }} {{ selectedUnit }}</span>
    </div>

    <!-- Canvas -->
    <GeometryCanvas ref="geometryCanvas" />
  </div>
</template>

<script>
import GeometryCanvas from "../components/GeometryCanvas.vue";
import { ref } from "vue";

export default {
  components: {
    GeometryCanvas,
  },
  setup() {
    const geometryCanvas = ref(null);
    const selectedUnit = ref("mm");
    const width = ref(100);
    const height = ref(100);

    const addCircle = () => {
      if (geometryCanvas.value) {
        geometryCanvas.value.addShape("circle");
      }
    };

    const addSquare = () => {
      if (geometryCanvas.value) {
        geometryCanvas.value.addShape("square");
      }
    };

    const addTriangle = () => {
      if (geometryCanvas.value) {
        geometryCanvas.value.addShape("triangle");
      }
    };

    const enableDrawing = () => {
      if (geometryCanvas.value) {
        geometryCanvas.value.enableDrawing();
      }
    };

    const clearCanvas = () => {
      if (geometryCanvas.value) {
        geometryCanvas.value.clearCanvas();
      }
    };

    const updateSize = () => {
      if (geometryCanvas.value) {
        geometryCanvas.value.updateShapeSize(width.value, height.value);
      }
    };

    return { geometryCanvas, selectedUnit, width, height, addCircle, addSquare, addTriangle, enableDrawing, clearCanvas, updateSize };
  },
};
</script>

<style scoped>
.geometry-container {
  background-color: #1e1e1e;
  color: #e0e0e0;
  min-height: 100vh;
  padding: 20px;
  box-shadow: 0 0 10px rgba(0,0,0,0.6);
}

h2 {
  color: #61dafb;
  margin-bottom: 10px;
}

p {
  color: #ccc;
  margin-bottom: 20px;
}

.toolbar {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-bottom: 20px;
}

.toolbar button {
  font-size: 1.5em;
  padding: 10px 15px;
  background: #292929;
  color: #fff;
  border: 1px solid #444;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.2s;
}

.toolbar button:hover {
  background: #3d3d3d;
}

.dimension-bar {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}

.dimension-bar label {
  color: #bbb;
}

.dimension-bar select,
.dimension-bar input[type="range"] {
  background: #222;
  color: #fff;
  border: 1px solid #444;
  border-radius: 4px;
  padding: 5px;
}

</style>
