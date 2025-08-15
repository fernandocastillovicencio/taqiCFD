from flask import Flask, jsonify
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # Rota raiz
    @app.route('/')
    def home():
        return jsonify({
            "message": "Bem-vindo à API do taqiCFD",
            "routes": {
                "geometry": "/api/geometry/save",
                "simulation": "/api/simulation/run"
            }
        })
    
    try:
        # Registra blueprints
        from .controllers.geometry_controller import geometry_bp
        from .controllers.simulation_controller import simulation_bp
        
        app.register_blueprint(geometry_bp, url_prefix='/api/geometry')
        app.register_blueprint(simulation_bp, url_prefix='/api/simulation')
        
    except Exception as e:
        print(f"Error registering blueprints: {e}")
        raise
    
    return app