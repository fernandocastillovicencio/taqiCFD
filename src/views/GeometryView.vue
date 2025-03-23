<template>
  <div class="geometry-container">
    <h2>Geometry Setup</h2>
    <p>Select or draw a geometry.</p>
    <GeometryCanvas />
  </div>
</template>

<script>
import GeometryCanvas from "../components/GeometryCanvas.vue";

export default {
  components: {
    GeometryCanvas,
  },
};
</script>

<style scoped>
.geometry-container {
  text-align: center;
  padding: 20px;
}

h2 {
  color: #333;
}

p {
  color: #666;
}

</style>
