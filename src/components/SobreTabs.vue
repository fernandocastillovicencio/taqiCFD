<template>
  <div class="geometry-container">

    <div class="toolbar">
      <button v-for="tab in tabs" :key="tab" @click="activeTab = tab">
        {{ tab }}
      </button>
    </div>

    <div class="content">
      <div v-if="activeTab === 'Professor'">
        <p><strong>Professor:</strong> Responsável por guiar os alunos na jornada fullstack, incentivando boas práticas e pensamento lógico.</p>
      </div>

      <div v-else-if="activeTab === 'Instituição'">
        <p><strong>Instituição:</strong> Oferece estrutura, apoio pedagógico e ambiente para o desenvolvimento profissional e técnico dos estudantes.</p>
      </div>

      <div v-else-if="activeTab === 'Aluno Back-end'">
        <p><strong>Aluno do Back-end:</strong> Trabalha com banco de dados, lógica de negócio e APIs para garantir que os sistemas funcionem corretamente.</p>
      </div>

      <div v-else-if="activeTab === 'Aluno Front-end'">
        <p><strong>Aluno do Front-end:</strong> Foca na parte visual e interativa do sistema, garantindo uma boa experiência para os usuários.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const tabs = ['Professor', 'Instituição', 'Aluno Back-end', 'Aluno Front-end']
const activeTab = ref('Professor')
</script>

<style scoped>
.geometry-container {
  background-color: #1e1e1e;
  color: #e0e0e0;
  min-height: 100vh;
  padding: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.6);
}

h2 {
  color: #61dafb;
  margin-bottom: 10px;
  text-align: center;
}

p {
  color: #ccc;
  margin-bottom: 20px;
  font-size: 1.1em;
}

.toolbar {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}

.toolbar button {
  font-size: 1.1em;
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

.content {
  max-width: 800px;
  margin: 0 auto;
  background: #2a2a2a;
  padding: 20px;
  border-radius: 10px;
  box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.3);
}
</style>
