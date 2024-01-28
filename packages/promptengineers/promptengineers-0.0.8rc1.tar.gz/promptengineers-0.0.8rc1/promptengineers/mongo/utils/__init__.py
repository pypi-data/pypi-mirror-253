import json


from cryptography.fernet import Fernet
from bson import ObjectId

from promptengineers.core.config import APP_SECRET

def encrypt(data: str) -> str:
	return Fernet(APP_SECRET).encrypt(data.encode()).decode()

def decrypt(data: str) -> str:
	return Fernet(APP_SECRET).decrypt(data.encode()).decode()

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)