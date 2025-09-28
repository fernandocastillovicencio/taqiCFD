import os
import firebase_admin
from firebase_admin import credentials, db

class FirebaseModel:
    _initialized = False

    def __init__(self):
        if not FirebaseModel._initialized:
            try:
                # Caminho do JSON na mesma pasta do arquivo
                BASE_DIR = os.path.dirname(os.path.abspath(__file__))
                FIREBASE_JSON = os.path.join(BASE_DIR, "firebase-service-account.json")

                # Inicializa o Firebase usando o JSON do service account
                cred = credentials.Certificate(FIREBASE_JSON)

                # Substitua pela URL real do seu Realtime Database
                DATABASE_URL = 'https://taqi-cfd-backend-default-rtdb.firebaseio.com'

                firebase_admin.initialize_app(cred, {
                    'databaseURL': DATABASE_URL
                })

                FirebaseModel._initialized = True
                print("✅ Firebase inicializado com sucesso!")
            except Exception as e:
                print(f"❌ Erro ao inicializar Firebase: {str(e)}")
                raise RuntimeError("Não foi possível inicializar o Firebase") from e

        # Referência principal do banco de dados
        self.db = db.reference()

    def get_reference(self, path):
        """
        Retorna uma referência a um caminho específico do Realtime Database.
        Exemplo:
            firebase = FirebaseModel()
            ref = firebase.get_reference("usuarios")
        """
        return self.db.child(path)
