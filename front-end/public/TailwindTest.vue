<template>
  <div class="p-8 bg-white rounded-lg shadow-lg max-w-md mx-auto mt-8">
    <h2 class="text-2xl font-bold text-gray-800 mb-4">Teste Tailwind CSS</h2>
    
    <div class="space-y-4">
      <button class="btn-primary w-full">Botão Primário</button>
      <button class="btn-secondary w-full">Botão Secundário</button>
      <input type="text" placeholder="Campo de texto" class="input-field" />
      <div class="bg-blue-100 text-blue-800 p-4 rounded-lg">
        <p class="font-medium">Tailwind CSS funcionando! 🎉</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TailwindTest'
}
</script>
