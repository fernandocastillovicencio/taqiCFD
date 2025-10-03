from flask import Blueprint, request, jsonify
from ..models.simulation_model import SimulationModel

simulation_bp = Blueprint('simulation', __name__)
sim_model = SimulationModel()

@simulation_bp.route('/run', methods=['POST'])
def run_simulation():
    try:
        data = request.json
        sim_id = sim_model.create(data)
        
        # Simulação OpenFOAM (implemente sua lógica)
        # foam = OpenFoamService()
        # result = foam.run(data)
        
        sim_model.update(sim_id, {
            'status': 'completed',
            'results': {'path': '/simulation/results'},
            'completedAt': {'.sv': 'timestamp'}
        })
        
        return jsonify({
            "status": "success",
            "simulationId": sim_id
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500