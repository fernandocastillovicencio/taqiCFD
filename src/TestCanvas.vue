<template>
  <div>
    <h2>Testando Fabric.js</h2>
    <canvas ref="fabricCanvas"></canvas>
  </div>
</template>

<script>
import { onMounted, ref } from "vue";
import { fabric } from "fabric";

export default {
  setup() {
    const fabricCanvas = ref(null);

    onMounted(() => {
      if (!fabricCanvas.value) return;

      const canvas = new fabric.Canvas(fabricCanvas.value, {
        width: 500,
        height: 400,
        backgroundColor: "white",
      });

      const rect = new fabric.Rect({
        left: 100,
        top: 100,
        fill: "blue",
        width: 100,
        height: 100,
      });

      canvas.add(rect);
    });

    return { fabricCanvas };
  },
};
</script>

<style scoped>
canvas {
  border: 1px solid black;
}
</style>
