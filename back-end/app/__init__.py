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
            "version": "1.0.0",
            "routes": {
                "geometry": "/api/geometry/save",
                "simulation": "/api/simulation/run", 
                "cfd_predict": "/api/cfd/predict",
                "health": "/api/cfd/health"
            }
        })
    
    try:
        # Registra blueprints existentes
        from .controllers.geometry_controller import geometry_bp
        from .controllers.simulation_controller import simulation_bp
        
        # Novo blueprint para CFD
        from .controllers.cfd_controller import cfd_bp
        
        app.register_blueprint(geometry_bp, url_prefix='/api/geometry')
        app.register_blueprint(simulation_bp, url_prefix='/api/simulation')
        app.register_blueprint(cfd_bp, url_prefix='/api/cfd')
        
    except Exception as e:
        print(f"Error registering blueprints: {e}")
        raise
    
    return app