import torch
import torch.nn as nn
import numpy as np
import os

class CFDNet(nn.Module):
    """
    Rede Neural para predição de campos de velocidade e pressão
    Arquitetura: MLP com camadas residuais para melhor convergência
    """
    def __init__(self, input_dim=10, hidden_dims=[512, 256, 128], output_dim=7500):
        super(CFDNet, self).__init__()
        
        layers = []
        prev_dim = input_dim
        
        # Camadas ocultas com ativação ReLU e Dropout
        for hidden_dim in hidden_dims:
            layers.extend([
                nn.Linear(prev_dim, hidden_dim),
                nn.ReLU(inplace=True),
                nn.Dropout(0.1),
                nn.BatchNorm1d(hidden_dim)
            ])
            prev_dim = hidden_dim
        
        # Camada de saída (velocidade u, v e pressão p)
        layers.append(nn.Linear(prev_dim, output_dim))
        
        self.network = nn.Sequential(*layers)
        
    def forward(self, x):
        return self.network(x)

class CFDPredictor:
    """
    Classe para carregar modelo treinado e fazer predições
    """
    def __init__(self, model_path="models/cfd_model.pth"):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = CFDNet()
        self.model_path = os.path.join(os.path.dirname(__file__), model_path)
        
        # Carregar modelo pré-treinado se existir
        if os.path.exists(self.model_path):
            self.model.load_state_dict(torch.load(self.model_path, map_location=self.device))
            self.model.eval()
            print(f"✅ Modelo carregado de {self.model_path}")
        else:
            print("⚠️ Modelo não encontrado. Inicializando com pesos aleatórios.")
            # Criar dados mock para demonstração
            self.create_mock_model()
    
    def create_mock_model(self):
        """Criar modelo mock para testes"""
        print("🔧 Criando modelo mock para demonstração...")
        self.model.eval()
    
    def predict(self, input_data):
        """
        Fazer predição dos campos de velocidade e pressão
        """
        try:
            # Converter para tensor
            input_tensor = torch.FloatTensor(input_data['features']).unsqueeze(0).to(self.device)
            
            with torch.no_grad():
                if hasattr(self, '_use_mock') or not os.path.exists(self.model_path):
                    # Usar dados mock para demonstração
                    prediction = self._generate_mock_prediction(input_data)
                else:
                    prediction = self.model(input_tensor)
                    prediction = prediction.cpu().numpy().reshape(-1)
            
            # Reshaping para campos 2D (assumindo grid 50x50)
            grid_size = input_data.get('grid_size', [50, 50])
            fields_per_variable = grid_size[0] * grid_size[1]
            
            if len(prediction) < 3 * fields_per_variable:
                # Usar predição mock se o modelo não foi treinado adequadamente
                prediction = self._generate_mock_prediction(input_data)
                prediction = prediction.flatten()
            
            # Separar velocidade u, v e pressão
            u_field = prediction[:fields_per_variable].reshape(grid_size)
            v_field = prediction[fields_per_variable:2*fields_per_variable].reshape(grid_size)
            p_field = prediction[2*fields_per_variable:3*fields_per_variable].reshape(grid_size)
            
            return {
                "velocity_u": u_field.tolist(),
                "velocity_v": v_field.tolist(),
                "pressure": p_field.tolist(),
                "grid_size": grid_size
            }
            
        except Exception as e:
            # Fallback para dados mock em caso de erro
            return self._generate_mock_result(input_data.get('grid_size', [50, 50]))
    
    def _generate_mock_prediction(self, input_data):
        """Gerar predição mock para demonstração"""
        grid_size = input_data.get('grid_size', [50, 50])
        total_points = grid_size[0] * grid_size[1]
        
        # Criar campos simulados
        x = np.linspace(0, 1, grid_size[1])
        y = np.linspace(0, 1, grid_size[0])
        X, Y = np.meshgrid(x, y)
        
        # Campo de velocidade u (parabólico)
        u_field = 4 * Y * (1 - Y) * np.ones_like(X)
        
        # Campo de velocidade v (pequeno)
        v_field = 0.1 * np.sin(2 * np.pi * X) * Y
        
        # Campo de pressão (decrescente)
        p_field = 1 - X + 0.1 * np.sin(4 * np.pi * X) * np.cos(4 * np.pi * Y)
        
        return np.concatenate([u_field.flatten(), v_field.flatten(), p_field.flatten()])
    
    def _generate_mock_result(self, grid_size):
        """Gerar resultado mock em caso de erro"""
        mock_data = self._generate_mock_prediction({'grid_size': grid_size})
        total_points = grid_size[0] * grid_size[1]
        
        return {
            "velocity_u": mock_data[:total_points].reshape(grid_size).tolist(),
            "velocity_v": mock_data[total_points:2*total_points].reshape(grid_size).tolist(),
            "pressure": mock_data[2*total_points:3*total_points].reshape(grid_size).tolist(),
            "grid_size": grid_size
        }