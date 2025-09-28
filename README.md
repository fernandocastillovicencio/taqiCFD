# taqiCFD - Fast and Interactive CFD Prediction Tool

## 🚀 Visão Geral

taqiCFD é uma ferramenta web interativa que permite simular e analisar escoamentos 2D ao redor de geometrias simples usando um modelo de machine learning pré-treinado. Em vez de executar simulações CFD complexas, o taqiCFD fornece predições instantâneas baseadas em geometrias e condições de contorno de entrada.

## 🏗️ Arquitetura

```
taqiCFD/
├── front-end/          # Interface Vue.js + Plotly.js + Tailwind
├── back-end/           # API Flask + Rede Neural PyTorch  
├── docs/               # Documentação
└── tests/              # Testes automatizados
```

## ⚡ Funcionalidades

### Frontend (Vue.js)
- ✅ Upload ou desenho de geometrias 2D
- ✅ Configuração de condições de contorno
- ✅ Visualizações interativas com Plotly.js
- ✅ Interface responsiva com Tailwind CSS
- ✅ Exportação de resultados

### Backend (Flask + PyTorch)
- ✅ API REST para predições CFD
- ✅ Rede neural para campos de velocidade e pressão
- ✅ Pré-processamento e normalização de dados
- ✅ Integração com Firebase
- ✅ Cálculo automático de números adimensionais

## 🛠️ Instalação

### Prerequisites
- Node.js 18+
- Python 3.9+
- Git

### Backend Setup
```bash
cd back-end
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac  
source venv/bin/activate

pip install -r requirements.txt
python run.py
```

### Frontend Setup
```bash
cd front-end
npm install
npm run dev
```

## 🔬 Como Usar

1. **Definir Geometria**: Desenhe ou configure uma geometria 2D
2. **Condições de Contorno**: Defina velocidade, pressão e propriedades do fluido
3. **Executar Predição**: Clique em "Simular" para predição instantânea
4. **Visualizar Resultados**: Analise campos de velocidade, pressão e linhas de fluxo
5. **Exportar**: Baixe os resultados em JSON ou imagens

## 📈 Roadmap

- [ ] Geometrias 3D
- [ ] Mais tipos de escoamento (turbulento, térmico)
- [ ] Comparação com OpenFOAM
- [ ] Interface para treinamento do modelo
- [ ] Deploy em nuvem

## 👥 Equipe

- **Enzo Salles** - Frontend & UI/UX
- **Lucas** - Backend & Machine Learning
- **Prof. Castilho** - Orientação

## 📄 Licença

MIT License - veja LICENSE para detalhes.