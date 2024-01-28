import os
from promptengineers.retrieval.factories import EmbeddingFactory, LoaderFactory, RetrievalFactory
from promptengineers.retrieval.strategies import VectorstoreContext
from promptengineers.retrieval.utils import get_links

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
PINECONE_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_ENV = os.environ.get('PINECONE_ENV')
PINECONE_INDEX = os.environ.get('PINECONE_INDEX')

INDEX_PROVIDER = 'pinecone'
INDEX_NAME = 'default'
NAMESPACE = '63f0962f9a09c84c98ab6caf::formio'
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
	print(vectorstore)
except Exception as e:
	print(f"Error processing documents with Pinecone: {e}")