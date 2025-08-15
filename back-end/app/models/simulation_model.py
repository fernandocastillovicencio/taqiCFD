from .firebase.firebase_model import FirebaseModel

class SimulationModel:
    def __init__(self):
        self.firebase = FirebaseModel()
        self.ref = self.firebase.get_reference('simulations')
    
    def create_simulation(self, data):
        new_ref = self.ref.push()
        new_ref.set({
            'name': data.get('name'),
            'parameters': data.get('parameters'),
            'status': 'pending',
            'createdAt': {'.sv': 'timestamp'}
        })
        return new_ref.key