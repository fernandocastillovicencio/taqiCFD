<template>
    <div>
      <canvas ref="fabricCanvas"></canvas>
    </div>
  </template>
  
  <script>
  import { onMounted, ref } from "vue";
  import * as fabric from "fabric";


  
  export default {
    setup() {
      const fabricCanvas = ref(null);
      let canvas = null;
  
      onMounted(() => {
        if (!fabricCanvas.value) return;
  
        canvas = new fabric.Canvas(fabricCanvas.value, {
          width: 500,
          height: 400,
          backgroundColor: "white",
        });
  
        const circle = new fabric.Circle({
          radius: 50,
          fill: "yellow",
          left: 100,
          top: 100,
        });
  
        canvas.add(circle);
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
  