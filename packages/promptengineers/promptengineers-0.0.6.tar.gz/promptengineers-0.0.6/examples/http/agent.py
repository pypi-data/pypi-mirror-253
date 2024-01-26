########################################################################
## Prompt Engineers AI - Agent Chat equipped w/ tools
########################################################################
import os
import asyncio

from promptengineers.chat import langchain_http_agent_chat
from promptengineers.core.config.tools import AVAILABLE_TOOLS
from promptengineers.llms.utils import gather_tools
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
CHAT_LLM = 'gpt-3.5-turbo-1106'
TEMPERATURE = 0.1
MESSAGES = [
    {
        'role': 'system', 
        'content': 'You are a powerful AI assistant, you are equipped with tools '
                    'to help you accomplish your tasks. Query the context when you need '
                    'additional information to complete your task. If the user query is not '
                    'related to the context then you can use the tools complete the task.'
    },
    {
        'role': 'user', 
        'content': 'What is 14125 compounded annually for 5 years at 4 percent for 23 years?' # Math Agent
        # 'content': 'Can you provide a react code sample to render a form in Form.io?'           # Retrieval Agent
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

# Gather the tools
tools = gather_tools(tools=['math_tool'],
                    available_tools=AVAILABLE_TOOLS,
                    vectorstore=vectorstore,
                    plugins=[])

# Run the chat
async def main():
    response, cb = await langchain_http_agent_chat(
        messages=MESSAGES,         
        model=CHAT_LLM,
        tools=tools,
        temperature=TEMPERATURE, 
        openai_api_key=OPENAI_API_KEY
    )
    print(response)
    print(cb)

asyncio.run(main())