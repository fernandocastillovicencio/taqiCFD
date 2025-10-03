import axios from 'axios'

// Configuração base da API
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000'

const apiClient = axios.create({
  baseURL: `${API_BASE_URL}/api`,
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json'
  }
})

// Interceptador para logs e tratamento de erros
apiClient.interceptors.response.use(
  response => response,
  error => {
    console.error('API Error:', error.response?.data || error.message)
    return Promise.reject(error)
  }
)

export const cfdAPI = {
  /**
   * Enviar dados para predição CFD
   * @param {Object} data - Dados da geometria e condições de contorno
   */
  async predictFlow(data) {
    try {
      const response = await apiClient.post('/cfd/predict', data)
      return response.data
    } catch (error) {
      throw new Error(`Erro na predição: ${error.response?.data?.error || error.message}`)
    }
  },

  /**
   * Verificar status da API
   */
  async healthCheck() {
    try {
      const response = await apiClient.get('/cfd/health')
      return response.data
    } catch (error) {
      throw new Error(`API indisponível: ${error.message}`)
    }
  },

  /**
   * Salvar geometria no Firebase
   * @param {Object} geometry - Dados da geometria
   */
  async saveGeometry(geometry) {
    try {
      const response = await apiClient.post('/geometry/save', geometry)
      return response.data
    } catch (error) {
      throw new Error(`Erro ao salvar: ${error.response?.data?.error || error.message}`)
    }
  }
}

export default apiClient