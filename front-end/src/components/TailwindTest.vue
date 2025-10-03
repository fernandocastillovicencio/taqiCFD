<template>
  <div class="container-page">
    <div class="card max-w-md mx-auto animate-fade-in">
      <h2 class="text-2xl font-bold text-slate-800 mb-6">Teste Tailwind CSS</h2>
      
      <div class="space-y-4">
        <button class="btn-primary w-full">Botão Primário</button>
        <button class="btn-secondary w-full">Botão Secundário</button>
        <button class="btn-outline w-full">Botão Outline</button>
        <input type="text" placeholder="Campo de entrada" class="input-field" />
        <select class="select-field">
          <option>Selecione uma opção</option>
          <option>Opção 1</option>
          <option>Opção 2</option>
        </select>
        <div class="bg-green-100 text-green-800 p-4 rounded-lg border border-green-200">
          <p class="font-medium">✅ Tailwind CSS configurado corretamente!</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TailwindTest'
}
</script>