from flask import Blueprint, request, jsonify
import numpy as np
from ..models.cfd.neural_network import CFDPredictor
from ..services.preprocessing_service import PreprocessingService

cfd_bp = Blueprint('cfd', __name__)

@cfd_bp.route('/predict', methods=['POST'])
def predict_flow():
    """
    Endpoint para predição de fluxo CFD usando rede neural
    Entrada: parâmetros geométricos e condições de contorno
    Saída: campos de velocidade e pressão
    """
    try:
        data = request.get_json()
        
        # Validação dos dados de entrada
        required_fields = ['geometry', 'boundary_conditions', 'fluid_properties']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Campo obrigatório '{field}' não encontrado"}), 400
        
        # Pré-processamento dos dados
        preprocessor = PreprocessingService()
        processed_data = preprocessor.process_input(data)
        
        # Predição usando rede neural
        predictor = CFDPredictor()
        prediction = predictor.predict(processed_data)
        
        return jsonify({
            "success": True,
            "prediction": prediction,
            "metadata": {
                "reynolds_number": processed_data.get('reynolds', 0),
                "mesh_size": processed_data.get('mesh_size', [50, 50])
            }
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@cfd_bp.route('/health', methods=['GET'])
def health_check():
    """Verificação de saúde da API"""
    return jsonify({
        "status": "healthy",
        "message": "API CFD está funcionando corretamente"
    })