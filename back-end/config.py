import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

class Config:
    FIREBASE_CREDENTIALS = BASE_DIR / "config" / "firebase_credentials.json"
    OPENFOAM_PATH = os.getenv('OPENFOAM_PATH', '/opt/openfoam')