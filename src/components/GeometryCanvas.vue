<template>
    <div>
      <canvas ref="fabricCanvas"></canvas>
    </div>
  </template>
  
  <script>
  import { onMounted, ref } from "vue";
  import * as fabric from "fabric";
  
  export default {
    setup(_, { expose }) {
      const fabricCanvas = ref(null);
      let canvas = null;
  
      onMounted(() => {
        // Garante que o canvas está sendo inicializado corretamente
        if (!fabricCanvas.value) return;
  
        canvas = new fabric.Canvas(fabricCanvas.value, {
          width: 500,
          height: 400,
          backgroundColor: "white",
        });
      });
  
      // Método para adicionar formas ao canvas
      const addShape = (type) => {
        if (!canvas) return;
  
        let shape;
        switch (type) {
          case "circle":
            shape = new fabric.Circle({
              radius: 50,
              fill: "yellow",
              left: 100,
              top: 100,
            });
            break;
          case "square":
            shape = new fabric.Rect({
              width: 100,
              height: 100,
              fill: "blue",
              left: 100,
              top: 100,
            });
            break;
          case "triangle":
            shape = new fabric.Triangle({
              width: 100,
              height: 100,
              fill: "red",
              left: 100,
              top: 100,
            });
            break;
        }
  
        if (shape) {
          canvas.add(shape);
          canvas.renderAll();
        }
      };
  
      // Método para ativar/desativar desenho manual
      let isDrawing = false;
      const enableDrawing = () => {
        if (!canvas) return;
  
        isDrawing = !isDrawing; // Alterna o modo desenho
        canvas.isDrawingMode = isDrawing;
        canvas.freeDrawingBrush.width = 3;
        canvas.freeDrawingBrush.color = "black";
        canvas.defaultCursor = isDrawing ? "crosshair" : "default";
      };
  
      // Método para limpar o canvas
      const clearCanvas = () => {
        if (!canvas) return;
        canvas.clear();
        canvas.setBackgroundColor("white", canvas.renderAll.bind(canvas));
      };
  
      expose({ addShape, enableDrawing, clearCanvas });
  
      return { fabricCanvas };
    },
  };
  </script>
  
  <style scoped>
  canvas {
    border: 1px solid black;
  }
  </style>
  