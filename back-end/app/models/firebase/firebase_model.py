import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, db

# Load environment variables from .env file
load_dotenv()

class FirebaseModel:
    _initialized = False

    def __init__(self):
        if not FirebaseModel._initialized:
            service_account_info = {
                "type": os.getenv("FIREBASE_TYPE"),
                "project_id": os.getenv("FIREBASE_PROJECT_ID"),
                "private_key_id": os.getenv("FIREBASE_PRIVATE_KEY_ID"),
                "private_key": os.getenv("FIREBASE_PRIVATE_KEY").replace("\\n", "\n"),
                "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
                "client_id": os.getenv("FIREBASE_CLIENT_ID"),
                "auth_uri": os.getenv("FIREBASE_AUTH_URI"),
                "token_uri": os.getenv("FIREBASE_TOKEN_URI"),
                "auth_provider_x509_cert_url": os.getenv("FIREBASE_AUTH_PROVIDER_X509_CERT_URL"),
                "client_x509_cert_url": os.getenv("FIREBASE_CLIENT_X509_CERT_URL"),
                "universe_domain": os.getenv("FIREBASE_UNIVERSE_DOMAIN")
            }

            try:
                cred = credentials.Certificate(service_account_info)
                firebase_admin.initialize_app(cred, {
                    'databaseURL': os.getenv("FIREBASE_DATABASE_URL")
                })
                FirebaseModel._initialized = True
                print("✅ Firebase inicializado com sucesso!")
            except Exception as e:
                print(f"❌ Erro ao inicializar Firebase: {str(e)}")
                raise RuntimeError("Não foi possível inicializar o Firebase") from e

        # Obtém a referência do banco de dados
        self.db = db.reference()

    def get_reference(self, path):
        return self.db.child(path)