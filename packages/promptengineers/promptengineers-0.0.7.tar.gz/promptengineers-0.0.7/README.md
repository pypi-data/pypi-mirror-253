# Prompt Engineers AI Open Source Package

### Build and Publish

```bash
## Build Package
bash scripts/build.sh

## Publish Package to PyPi
bash scripts/publish.sh
```

### Development

```bash
## In the application directory start your virtual env (this would be the workspace
## where your API server that you would like to install the model)
source .venv/bin/activate

## Then change directory to where your package is, make changes and run the following.
pip install .

## Switch back to the directory of your where your workspace is for you app server.
cd <path>/<app>/<server>
pip install -r requirements.txt

## Make sure your app server has the packages shown in setup.py and run your server...
```

## How to use...

### Load Documents from Sources
```py
import os
from promptengineers.retrieval.factories import EmbeddingFactory, LoaderFactory, RetrievalFactory
from promptengineers.retrieval.strategies import VectorstoreContext

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
PINECONE_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_ENV = os.environ.get('PINECONE_ENV')
PINECONE_INDEX = os.environ.get('PINECONE_INDEX')

INDEX_PROVIDER = 'pinecone'
INDEX_NAME = 'default'
NAMESPACE = '000000000000000000000000::formio'
EMBEDDING_LLM = 'text-embedding-ada-002'
LOADERS = [
	{
		"type": "copy",
	  	"text": "In a quaint village, an elderly man discovered a mysterious, "
				"ancient book in his attic. Each night, he read a chapter, and the "
				"next day, miracles began happening in the village. Unbeknownst to "
				"the villagers, their fortunes were being written by the man's dreams, "
				"guided by the magical book."
	},
	{
		"type": "web_base",
	  	"urls": ['https://adaptive.biz']
	},
	{
		"type": "website",
	  	"urls": ['https://adaptive.biz'] # Retrieves subpages
	},
	{
		"type": "youtube",
	  	"urls": ['https://www.youtube.com/watch?v=GyllRd2E6fg']
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

# Create loaders and process each
all_loaders = []
for loader_config in LOADERS:
	try:
		loader = LoaderFactory.create(loader_type=loader_config['type'], loader_config=loader_config)
		all_loaders.append(loader)
	except ValueError as e:
		print(f"Error creating loader: {e}")
	except Exception as e:
		print(f"Unexpected error: {e}")

# Assuming PineconeService and EmbeddingFactory have internal error handling
try:
	# Create a vector store service context
	vectostore_service = VectorstoreContext(retrieval_provider.create_strategy())
	vectorstore = vectostore_service.add(all_loaders)
except Exception as e:
	print(f"Error processing documents with Pinecone: {e}")
```

### Retrieval Augemented Generation (RAG) - HTTP Chat
```py
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
NAMESPACE = '000000000000000000000000::formio'
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
```

### Retrieval Augemented Generation (RAG) - Stream Chat
```py
import os
import asyncio

from promptengineers.chat import langchain_stream_vectorstore_chat
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
NAMESPACE = '000000000000000000000000::formio'
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
    response = langchain_stream_vectorstore_chat(
        messages=MESSAGES,         
        model=CHAT_LLM, 
        temperature=TEMPERATURE, 
        vectorstore=vectorstore,
        openai_api_key=OPENAI_API_KEY
    )
    async for data in response:
        print(data)

asyncio.run(main())
```

### Agent Chat equipped w/ tools - HTTP Chat
```py
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
NAMESPACE = '000000000000000000000000::formio'
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
```

### Agent Chat equipped w/ tools - Stream Chat
```py
import os
import asyncio

from promptengineers.chat import langchain_stream_agent_chat
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
NAMESPACE = '000000000000000000000000::formio'
EMBEDDING_LLM = 'text-embedding-ada-002'

# Chat Constants
CHAT_LLM = 'gpt-4-0125-preview'
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
        # 'content': 'What is 14125 compounded annually for 5 years at 4 percent for 23 years?' # Math Agent
        'content': 'Can you provide a react code sample to render a form in Form.io?'           # Retrieval Agent
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
    response = langchain_stream_agent_chat(
        messages=MESSAGES,         
        model=CHAT_LLM,
        tools=tools,
        temperature=TEMPERATURE, 
        openai_api_key=OPENAI_API_KEY
    )
    async for data in response:
        print(data)

asyncio.run(main())
```
