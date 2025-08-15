from flask import Blueprint, request, jsonify
from ..models.firebase.firebase_model import FirebaseModel
from datetime import datetime

geometry_bp = Blueprint('geometry', __name__)
firebase = FirebaseModel()
geometry_ref = firebase.get_reference('geometries')
simulation_ref = firebase.get_reference('simulations')

@geometry_bp.route('/save', methods=['POST'])
def save_geometry():
    data = request.json
    try:
        new_geom = geometry_ref.push()
        new_geom.set({
            'name': data.get('name'),
            'data': data.get('geometry_data'),
            'created_at': datetime.now().isoformat()
        })
        return jsonify({
            "status": "success",
            "geometry_id": new_geom.key
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500