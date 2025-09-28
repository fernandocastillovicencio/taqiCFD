import numpy as np
from scipy import interpolate
import math

class PreprocessingService:
    """
    Serviço para pré-processamento dos dados de entrada
    Normalização, adimensionalização e preparação para rede neural
    """
    
    def __init__(self):
        # Valores de referência para normalização
        self.reference_values = {
            "velocity": 1.0,  # m/s
            "length": 1.0,    # m
            "density": 1.0,   # kg/m³
            "viscosity": 1e-3 # Pa.s
        }
    
    def process_input(self, raw_data):
        """
        Processar dados de entrada e gerar features para rede neural
        """
        try:
            geometry = raw_data['geometry']
            boundary_conditions = raw_data['boundary_conditions']
            fluid_properties = raw_data['fluid_properties']
            
            # Extrair parâmetros geométricos
            geometry_features = self._extract_geometry_features(geometry)
            
            # Calcular números adimensionais
            reynolds = self._calculate_reynolds(
                boundary_conditions.get('inlet_velocity', 1.0),
                geometry.get('characteristic_length', 0.1),
                fluid_properties.get('density', 1.0),
                fluid_properties.get('viscosity', 1e-3)
            )
            
            # Normalizar condições de contorno
            normalized_bc = self._normalize_boundary_conditions(boundary_conditions)
            
            # Combinar todas as features
            features = np.concatenate([
                geometry_features,
                normalized_bc,
                [reynolds / 1000.0]  # Normalizar Reynolds
            ])
            
            return {
                "features": features.astype(np.float32),
                "reynolds": reynolds,
                "grid_size": raw_data.get('grid_size', [50, 50]),
                "geometry": geometry
            }
            
        except Exception as e:
            raise ValueError(f"Erro no pré-processamento: {str(e)}")
    
    def _extract_geometry_features(self, geometry):
        """Extrair características geométricas relevantes"""
        features = []
        
        # Tipo de geometria (one-hot encoding)
        geometry_types = ['circle', 'square', 'rectangle', 'polygon']
        geometry_type = geometry.get('type', 'circle')
        geometry_vector = [1.0 if geometry_type == gt else 0.0 for gt in geometry_types]
        features.extend(geometry_vector)
        
        # Dimensões normalizadas
        if geometry_type == 'circle':
            radius = geometry.get('radius', 0.1)
            features.extend([
                radius / self.reference_values['length'],
                radius / self.reference_values['length'],  # Simetria
                1.0  # Fator de forma circular
            ])
        elif geometry_type in ['square', 'rectangle']:
            width = geometry.get('width', 0.2)
            height = geometry.get('height', 0.2)
            features.extend([
                width / self.reference_values['length'],
                height / self.reference_values['length'],
                width / max(height, 1e-6)  # Aspect ratio
            ])
        else:
            # Fallback para geometrias não reconhecidas
            features.extend([0.1, 0.1, 1.0])
        
        return np.array(features)
    
    def _normalize_boundary_conditions(self, bc):
        """Normalizar condições de contorno"""
        return np.array([
            bc.get('inlet_velocity', 1.0) / self.reference_values['velocity'],
            bc.get('outlet_pressure', 0.0) / 101325.0,  # Normalizar por pressão atmosférica
            bc.get('wall_temperature', 300.0) / 300.0   # Normalizar por temp. ambiente
        ])
    
    def _calculate_reynolds(self, velocity, length, density, viscosity):
        """Calcular número de Reynolds"""
        return (density * velocity * length) / viscosity