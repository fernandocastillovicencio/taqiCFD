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
    let currentShape = null; // <- Mantém referência à última forma adicionada

    onMounted(() => {
      if (!fabricCanvas.value) return;

      canvas = new fabric.Canvas(fabricCanvas.value, {
        width: 500,
        height: 400,
        backgroundColor: "#1e1e1e", // fundo escuro confortável
      });
    });

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
        canvas.setActiveObject(shape);
        currentShape = shape;
        canvas.renderAll();
      }
    };

    const enableDrawing = () => {
      if (!canvas) return;

      canvas.isDrawingMode = !canvas.isDrawingMode;
      canvas.freeDrawingBrush.width = 3;
      canvas.freeDrawingBrush.color = "white";
      canvas.defaultCursor = canvas.isDrawingMode ? "crosshair" : "default";
    };

    const clearCanvas = () => {
      if (!canvas) return;

      canvas.clear();
      canvas.setBackgroundColor("#1e1e1e", canvas.renderAll.bind(canvas));
      currentShape = null;
    };

    const updateShapeSize = (width, height) => {
      if (!currentShape) return;

      if (currentShape.type === "circle") {
        currentShape.set({
          radius: Math.min(width, height) / 2, // círculo usa raio
        });
      } else {
        currentShape.set({
          width: width,
          height: height,
        });
      }

      currentShape.setCoords(); // atualiza o bounding box
      canvas.renderAll();
    };

    const setCanvasBackground = (color) => {
      if (!canvas) return;
      canvas.setBackgroundColor(color, canvas.renderAll.bind(canvas));
    };

    expose({
      addShape,
      enableDrawing,
      clearCanvas,
      updateShapeSize,
      setCanvasBackground,
    });

    return { fabricCanvas };
  },
};
</script>

  
<style scoped>
canvas {
  border: 2px solid #444;
  background-color: #1e1e1e; /* visual escuro já no estilo também */
}
</style>
  