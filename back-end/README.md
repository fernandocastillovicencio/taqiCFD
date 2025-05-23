# Projeto de Iniciação Científica - Backend com Rede Neural

## Objetivo

Criar um sistema backend em Python para ingestão de dados de planilhas (.csv ou .xlsx), treinar uma rede neural com esses dados e expor a funcionalidade via API para predições futuras.

---

## Tecnologias

* **Linguagem:** Python 3.11+
* **Framework Web:** FastAPI
* **Machine Learning:** TensorFlow ou PyTorch
* **Gerenciamento de Pacotes:** pip / pipenv / poetry
* **Banco de Dados:** SQLite (desenvolvimento), PostgreSQL (produção)
* **Armazenamento de Arquivos:** Local ou AWS S3
* **Outros:** pandas, scikit-learn, uvicorn, pydantic

---

## Funcionalidades

### 1. Upload de Planilha

* Rota: `POST /upload`
* Entrada: Arquivo `.csv` ou `.xlsx`
* Ação:

  * Validação e leitura dos dados com `pandas`
  * Armazenamento no banco de dados
  * Preparo dos dados para treino

---

### 2. Treinamento de Rede Neural

* Rota: `POST /train`
* Entrada: parâmetros opcionais (épocas, tamanho do batch, arquitetura, etc.)
* Ação:

  * Divide dados entre treino/teste
  * Normaliza os dados
  * Cria e treina uma rede neural
  * Salva modelo treinado (formato `.h5` ou `.pt`)
  * Salva métricas de avaliação

---

### 3. Predição

* Rota: `POST /predict`
* Entrada: JSON com dados
* Ação:

  * Carrega modelo treinado
  * Realiza predição com base nos dados
  * Retorna valor previsto

---

### 4. Listagem de Treinamentos

* Rota: `GET /models`
* Retorna: Lista de modelos treinados, data, métrica de acurácia, etc.

---

### 5. Download de Modelo

* Rota: `GET /model/{model_id}`
* Retorna: Arquivo do modelo treinado

---

## Estrutura de Pastas

```
taqiCFD/
│├──back-end/
│├── app/
││   ├── main.py
││   ├── models/
││   │   └── neural_network.py
││   ├── routes/
││   │   ├── upload.py
││   │   ├── train.py
││   │   └── predict.py
││   ├── services/
││   │   ├── file_handler.py
││   │   ├── train_handler.py
││   │   └── predict_handler.py
││   └── utils/
││       └── preprocessor.py
│├── data/
││   └── uploads/
│├── models/
││   └── saved_models/
│├── database/
││   └── db.py
│├── requirements.txt
│├── README.md
│└── .env
Outros pastas e arquivos...
```

---

## Planejamento de Arquitetura

### Camada 1: Entrada

* FastAPI
* Endpoints REST
* Upload de arquivos e dados

### Camada 2: Processamento de Dados

* pandas para leitura e pré-processamento
* Conversão, normalização, limpeza

### Camada 3: Machine Learning

* TensorFlow ou PyTorch
* Script modular para rede neural
* Função de treino e validação
* Salvar modelo treinado

### Camada 4: Predição

* Carregamento de modelo treinado
* Aplicação em dados de entrada
* Retorno via API

### Camada 5: Armazenamento

* SQLite/PostgreSQL para registros e logs
* Diretório local ou AWS S3 para arquivos e modelos

---

## Extensões Futuras

* Frontend em React ou Streamlit para visualização
* Monitoramento de métricas em tempo real
* Versionamento de modelos com MLFlow
* Autenticação JWT para API
* Criação de agendador para retreinamento automático

---

## Requisitos de Sistema

* Python 3.11+
* pipenv / poetry
* Git
* Docker (opcional)

---

