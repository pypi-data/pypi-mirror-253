"""Configuration files for the project."""
import os

# Path to the vector store
APP_ENV = os.getenv("APP_ENV", 'development')
APP_NAME = os.getenv("APP_NAME", 'Prompt Engineers AI - API Server')
APP_SECRET = os.getenv("APP_SECRET", '')
APP_VERSION = os.getenv("APP_VERSION", '')
APP_ORIGINS = os.getenv("APP_ORIGINS", '*')

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", '')
## Ollama URL
OLLAMA_BASE_URL= os.getenv("OLLAMA_BASE_URL", 'http://localhost:11434')

# Mongo
DB_NAME= os.getenv('DB_NAME', 'promptengineers')
DB_COLLECTION = os.getenv('DB_COLLECTION', 'history')
MONGO_CONNECTION = os.getenv("MONGO_CONNECTION", f'mongodb://localhost:27017')
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", f'llm-server')

# Redis
REDIS_URL = os.getenv("REDIS_URL", 'redis://localhost:6379/0')

# S3 Bucket Credentials
BUCKET = os.getenv("BUCKET", 'precision-x')
S3_REGION = os.getenv("S3_REGION", 'us-east-1')
ACCESS_KEY_ID = os.getenv("ACCESS_KEY_ID", '')
ACCESS_SECRET_KEY = os.getenv("ACCESS_SECRET_KEY", '')
MINIO_SERVER = os.getenv("MINIO_SERVER", '')

# Pinecone Credentials
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY", '')
PINECONE_ENV = os.getenv("PINECONE_ENV", '')
PINECONE_INDEX = os.getenv("PINECONE_INDEX", '')

# Blockchain Credentials
ALCHEMY_API_KEY = os.getenv("ALCHEMY_API_KEY", '')

default_app_tokens = {
    'OPENAI_API_KEY': OPENAI_API_KEY,
    'OLLAMA_BASE_URL': OLLAMA_BASE_URL,
    'MONGO_CONNECTION': MONGO_CONNECTION,
    'MONGO_DB_NAME': MONGO_DB_NAME,
    'REDIS_URL': REDIS_URL,
    'BUCKET': BUCKET,
    'S3_REGION': S3_REGION,
    'ACCESS_KEY_ID': ACCESS_KEY_ID,
    'ACCESS_SECRET_KEY': ACCESS_SECRET_KEY,
    'MINIO_SERVER': MINIO_SERVER,
    'PINECONE_API_KEY': PINECONE_API_KEY,
    'PINECONE_ENV': PINECONE_ENV,
    'PINECONE_INDEX': PINECONE_INDEX,
    'ALCHEMY_API_KEY': ALCHEMY_API_KEY,
}

def retrieve_defaults(keys):
    """
    Extracts a sub-dictionary from the given default dictionary based on the specified keys.

    :param default_dict: The original dictionary from which to extract the keys.
    :param keys: A set or list of keys to extract from the default dictionary.
    :return: A new dictionary containing only the keys present in the keys argument.
    """
    return {k: default_app_tokens[k] for k in keys if k in default_app_tokens}