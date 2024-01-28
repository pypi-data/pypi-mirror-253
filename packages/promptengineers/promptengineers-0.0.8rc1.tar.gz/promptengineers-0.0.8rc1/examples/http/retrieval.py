########################################################################
## Prompt Engineers AI - Retrieval Augmented Generation (RAG)
########################################################################
import os
import asyncio

from promptengineers.chat import langchain_http_retrieval_chat
from promptengineers.retrieval.factories import EmbeddingFactory, RetrievalFactory
from promptengineers.retrieval.strategies import VectorstoreContext

# Environment Variables
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
PINECONE_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_ENV = os.environ.get('PINECONE_ENV')
PINECONE_INDEX = os.environ.get('PINECONE_INDEX')

# Retrieval Constants
INDEX_PROVIDER = 'pinecone'
INDEX_NAME = 'default'
NAMESPACE = '63f0962f9a09c84c98ab6caf::formio'
EMBEDDING_LLM = 'text-embedding-ada-002'

# Chat Constants
CHAT_LLM = 'gpt-3.5-turbo'
TEMPERATURE = 0.9
MESSAGES = [
    {
        'role': 'system', 
        'content': 'You are a helpful document retrieval AI, '
                    'use the context to answer the user queries.'
    },
    {
        'role': 'user', 
        'content': 'Can you summarize the context?'
    }
]

# Generate Embeddings
embedding = EmbeddingFactory(EMBEDDING_LLM, OPENAI_API_KEY)

# Choose the appropriate vector search provider strategy for Pinecone
retrieval_provider = RetrievalFactory(
    INDEX_PROVIDER, 
    embedding.create_embedding(), 
    {
        'api_key': PINECONE_KEY, 
        'env': PINECONE_ENV, 
        'index_name': INDEX_NAME, 
        'namespace': NAMESPACE
    }
)

# Create a vector store service context
vectostore_service = VectorstoreContext(retrieval_provider.create_strategy())

# Load the vectorstore using the service context
vectorstore = vectostore_service.load()

# Run the chat
async def main():
    response, cb = await langchain_http_retrieval_chat(
        messages=MESSAGES,         
        model=CHAT_LLM, 
        temperature=TEMPERATURE, 
        vectorstore=vectorstore,
        openai_api_key=OPENAI_API_KEY
    )
    print(response)
    print(cb)

asyncio.run(main())