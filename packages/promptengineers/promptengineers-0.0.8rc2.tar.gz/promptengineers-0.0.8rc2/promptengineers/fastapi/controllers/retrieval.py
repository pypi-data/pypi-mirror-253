from typing import List
import os
import time
import pickle
import tempfile
from queue import Queue
from concurrent.futures import ThreadPoolExecutor

from fastapi import HTTPException, UploadFile, File, Request

from promptengineers.core.config.loaders import FileLoaderType
from promptengineers.retrieval.factories.embedding import EmbeddingFactory
from promptengineers.retrieval.factories.loader import LoaderFactory
from promptengineers.core.interfaces.repos import IUserRepo
from promptengineers.repos.user import UserRepo
from promptengineers.retrieval.services.redis import RedisService
from promptengineers.retrieval.services.pinecone import PineconeService
from promptengineers.storage.services import StorageService
from promptengineers.core.utils import logger
from promptengineers.core.validations import Validator
from promptengineers.retrieval.utils import create_faiss_vectorstore
from promptengineers.core.config.llm import OllamaModels

validator = Validator()
user_repo = UserRepo()

##############################################################
### Process File
##############################################################
def process_file(
	index_name: str,
	tmpdirname: str,
	file: UploadFile,
	embeddings,
	pinecone_service: PineconeService,
):
	try:
		file_path = os.path.join(tmpdirname, file.filename)
		_, file_extension = os.path.splitext(file.filename)
		file_extension_cleaned = file_extension.replace('.', '')

		# Check if the file extension is a valid type
		if file_extension_cleaned not in [e.value for e in FileLoaderType]:
			raise HTTPException(status_code=400, detail=f"Invalid file type: {file_extension_cleaned}")

		with open(file_path, 'wb') as f:
			f.write(file.file.read())  # write the file to the temporary directory
		doc_loader = LoaderFactory.create(file_extension_cleaned, {'file_path': file_path})

		pinecone_service.from_documents([doc_loader], embeddings, namespace=index_name)
	except HTTPException:
		raise  # Re-raise the HTTPException without modifying it
	except Exception as e:
		raise HTTPException(status_code=400, detail=str(e)) from e

##############################################################
### Accumulate Files
##############################################################
def accumulate_files(files, user_id, tokens):
	collected_files = []
	for name in files:
		try:
			s3 = StorageService(tokens.get('ACCESS_KEY_ID'), tokens.get('ACCESS_SECRET_KEY'))
			file = s3.retrieve_file(
				path=f'users/{user_id}/files/{name}',
				bucket=tokens.get('BUCKET'),
			)
			collected_files.append(file)
		except Exception as err:
			logger.error(err)
			raise HTTPException(
				status_code=404, detail=f"File Not Found in S3: {str(name)}"
			) from err
	filtered_lst = [x for x in collected_files if x is not None]
	return filtered_lst

##############################################################
### Accumulate Loaders
##############################################################
def accumulate_loaders(loaders, files=None, tmpdirname=None):
	accumulate_loaders = []
	for loader in loaders:
		try:
			# First, try accessing as if loader is a dictionary
			loader_type = loader['type']
		except TypeError:
			# If it fails, then access it as an attribute
			loader_type = loader.type
		loader_data = {}
		if loader_type == 'copy':
			try:
				loader_data = {'text': loader['text']}
			except TypeError:
				loader_data = {'text': loader.text}
		elif loader_type == 'yt':
			try:
				loader_data = {'ytId': loader['ytId']}
			except TypeError:
				loader_data = {'ytId': loader.ytId}
		elif loader_type in ['ethereum', 'polygon']:
			try:
				loader_data = {'contract_address': loader['contract_address']}
			except TypeError:
				loader_data = {'contract_address': loader.contract_address}
		else:
			try:
				loader_data = {'urls': loader['urls']}
			except TypeError:
				loader_data = {'urls': loader.urls}


		doc_loader = LoaderFactory.create(loader_type,  loader_data)
		accumulate_loaders.append(doc_loader)

	if tmpdirname:
		try:
			for file_body, name in zip(files, body.files):
				file_path = os.path.join(tmpdirname, name)
				with open(file_path, 'wb') as file:
					file.write(file_body.read())  # write the file to the temporary directory
				filename = file_path.split('/')[-1]
				loader = os.path.splitext(filename)[1][1:]
				doc_loader = LoaderFactory.create(
					loader,
					{'file_path': file_path}
				)
				accumulate_loaders.append(doc_loader)
		except Exception as err:
			logger.error(err)
			raise HTTPException(
				status_code=500,
				detail=f"Error creating loaders in tmp directory: {str(err)}"
			) from err
	return accumulate_loaders

##############################################################
### Create a FAISS Vectorstore
##############################################################
def faiss_vectorstore(loaders, tmpdirname, user_id, name, tokens):
	documents = []
	for loader in loaders:
		documents.extend(loader.load())
	logger.info("[main.load_vectorstore_from_file] Loaders: %s", str(len(loaders)))
	logger.info("[main.load_vectorstore_from_file] Documents: %s", str(len(documents)))
	vectorstore = create_faiss_vectorstore(documents)
	## Save Vectorstore to tmp directory
	temp_file_path = os.path.join(tmpdirname, f'{int(time.time())}-{name}.pkl')
	try:
		## Write to temp file
		with open(temp_file_path, "wb") as file:
			pickle.dump(vectorstore, file)

		s3 = StorageService(tokens.get('ACCESS_KEY_ID'), tokens.get('ACCESS_SECRET_KEY'))
		# Save to S3
		file = s3.upload_file(
			file_name=temp_file_path,
			bucket=tokens.get('BUCKET'),
			object_name=f'users/{user_id}/vectorstores/{name}.pkl'
		)
	except Exception as err:
		raise HTTPException(
			status_code=500,
			detail=f"Error saving vectorstore in tmp directory: {str(err)}"
		) from err
	finally:
		with os.scandir(tmpdirname) as entries:
			for entry in entries:
				os.remove(entry.path)


class VectorSearchController:
	def __init__(self, request: Request = None, user_repo: IUserRepo = None):
		# Initialize any necessary variables or objects here
		self.request = request
		self.user_id = getattr(request.state, "user_id", None)
		self.user_repo = user_repo or UserRepo()

	##############################################################
	### Create multi loader vectorstore
	##############################################################
	async def create_multi_loader_vectorstore(
			self,
			provider: str,
			index_name: str,
			embedding: str,
			loaders: List[dict] = None,
			files: List[str] = None
	):
		"""Create a vectorstore from multiple loaders with specific arguments."""
		pinecone_keys = ['PINECONE_API_KEY', 'PINECONE_ENV', 'PINECONE_INDEX', 'OPENAI_API_KEY']
		redis_keys = ['REDIS_URL', 'OPENAI_API_KEY']
		aws_keys = ['ACCESS_KEY_ID', 'ACCESS_SECRET_KEY', 'BUCKET']
		if not files:
			if provider == 'pinecone':
				tokens = await self.user_repo.find_token(self.user_id, pinecone_keys)
				embeddings = EmbeddingFactory(embedding, tokens.get('OPENAI_API_KEY'))
				validator.validate_api_keys(tokens, pinecone_keys)
				pinecone_service = PineconeService(
					api_key=tokens.get('PINECONE_API_KEY'),
					env=tokens.get('PINECONE_ENV'),
					index_name=tokens.get('PINECONE_INDEX'),
				)
				loaders = accumulate_loaders(loaders)
				pinecone_service.from_documents(
					loaders,
					embeddings(),
					namespace=index_name
				)

			if provider == 'redis':
				tokens = await self.user_repo.find_token(self.user_id, redis_keys)
				validator.validate_api_keys(tokens, redis_keys)
				embeddings = EmbeddingFactory(embedding, tokens.get('OPENAI_API_KEY'))
				redis_service = RedisService(
					embeddings=embeddings(),
					redis_url=tokens.get('REDIS_URL'),
					index_name=index_name,
				)
				loaders = accumulate_loaders(loaders)
				redis_service.add_docs(loaders)
		else:
			aws_keys = ['ACCESS_KEY_ID', 'ACCESS_SECRET_KEY', 'BUCKET']
			tokens = await self.user_repo.find_token(self.user_id, [*pinecone_keys, *aws_keys])
			validator.validate_api_keys(tokens, [*pinecone_keys, *aws_keys])
			# Accumulate Files
			accumulated_files = accumulate_files(files, self.user_id, tokens)

			# Create a temporary directory
			with tempfile.TemporaryDirectory() as tmpdirname:

				# Your logic here to save uploaded files to tmpdirname
				loaders = accumulate_loaders(loaders, accumulated_files, tmpdirname)

				if provider == 'faiss':
					faiss_vectorstore(loaders, tmpdirname, self.user_id, index_name, tokens)

				if provider == 'pinecone':
					embeddings = EmbeddingFactory(embedding, tokens.get('OPENAI_API_KEY'))
					pinecone_service = PineconeService(
						api_key=tokens.get('PINECONE_API_KEY'),
						env=tokens.get('PINECONE_ENV'),
						index_name=tokens.get('PINECONE_INDEX'),
					)
					pinecone_service.from_documents(loaders, embeddings(), namespace=index_name)

				if provider == 'redis':
					tokens = await self.user_repo.find_token(self.user_id, redis_keys)
					validator.validate_api_keys(tokens, redis_keys)
					redis_service = RedisService(
						openai_api_key=tokens.get('OPENAI_API_KEY'),
						redis_url=tokens.get('REDIS_URL'),
						index_name=index_name,
					)
					redis_service.add_docs(loaders)

	##############################################################
	### Create a Vectorstore from files
	##############################################################
	async def create_vectorstore_from_files(
		self,
		provider: str,
		index_name: str,
		embedding: str,
		files: List[UploadFile] = File(...),
		tokens: dict = None,
		threaded: bool = True,
	):
		"""Create a vectorstore from files."""
		# Validate the file extensions before processing
		for file in files:
			_, file_extension = os.path.splitext(file.filename)
			file_extension_cleaned = file_extension.replace('.', '')

			# Check if the file extension is a valid type
			if file_extension_cleaned not in [e.value for e in FileLoaderType]:
				raise HTTPException(status_code=400, detail=f"Invalid file type: {file_extension_cleaned}")

		## Get Tokens
		if provider == 'pinecone':
			## Get Embeddings and Pinecone Service
			embeddings = EmbeddingFactory(embedding, tokens.get('OPENAI_API_KEY'))
			pinecone_service = PineconeService(
				api_key=tokens.get('PINECONE_API_KEY'),
				env=tokens.get('PINECONE_ENV'),
				index_name=tokens.get('PINECONE_INDEX'),
			)

		## Create a temporary directory
		with tempfile.TemporaryDirectory() as tmpdirname:
			# Your logic here to save uploaded files to tmpdirname
			if threaded:
				file_queue = Queue()
				for file in files:
					file_queue.put(file)

				def worker():
					while not file_queue.empty():
						file = file_queue.get()
						try:
							process_file(index_name, tmpdirname, file, embeddings.create_embedding(), pinecone_service)
						finally:
							file_queue.task_done()

				with ThreadPoolExecutor() as executor:
					num_workers = min(len(files), os.cpu_count())  # You can adjust the number of workers
					for _ in range(num_workers):
						executor.submit(worker)

				file_queue.join()  # Wait for all files to be processed
			else:
				for file in files:
					process_file(index_name, tmpdirname, file, embeddings.create_embedding(), pinecone_service)


	##############################################################
	### Retrieve Pinecone Vectorstores
	##############################################################
	async def retrieve_pinecone_vectorstores(self, tokens: dict = None):
		## Get Tokens
		keys = ['PINECONE_API_KEY', 'PINECONE_ENV', 'PINECONE_INDEX']
		if not tokens:
			tokens = await self.user_repo.find_token(self.user_id, keys)
		## Check for token, else throw error
		validator.validate_api_keys(tokens, keys)
		## Get Vectorstores
		pinecone_service = PineconeService(
			api_key=tokens.get('PINECONE_API_KEY'),
			env=tokens.get('PINECONE_ENV'),
			index_name=tokens.get('PINECONE_INDEX'),
		)
		index_stats = pinecone_service.describe_index_stats()
		namespaces = index_stats.get('namespaces')

		# String to be removed
		remove_str = f"{self.user_id}::"

		# Trimming and including only the keys that were trimmed
		trimmed_namespaces = {key.replace(remove_str, ''): value for key, value in namespaces.items() if remove_str in key}

		return {
			'vectorstores': list(trimmed_namespaces.keys()),
		}

	##############################################################
	### Delete Pinecone Vectorstore
	##############################################################
	async def delete_pinecone_vectorstore(self, prefix: str, tokens: dict = None):
		## Get Tokens
		keys = ['PINECONE_API_KEY', 'PINECONE_ENV', 'PINECONE_INDEX']
		if not tokens:
			tokens = await self.user_repo.find_token(self.user_id, keys)
		## Check for token, else throw error
		validator.validate_api_keys(tokens, keys)
		## Delete Vectorstore
		pinecone_service = PineconeService(
			api_key=tokens.get('PINECONE_API_KEY'),
			env=tokens.get('PINECONE_ENV'),
			index_name=tokens.get('PINECONE_INDEX'),
		)
		deleted = pinecone_service.delete(namespace=f"{self.user_id}::{prefix}")
		if deleted:
			return True
		else:
			return False

	##############################################################
	### Retrieve Pinecone Vectorstores
	##############################################################
	def retrieve_redis_vectorstores(self):
		## Get Tokens
		keys = ['REDIS_URL']
		tokens = self.user_repo.find_token(self.user_id, keys)
		## Check for token, else throw error
		validator.validate_api_keys(tokens, keys)
		## Get Vectorstores
		redis_service = RedisService(
			redis_url=tokens.get('REDIS_URL')
		)
		index_stats = redis_service.list_indexes()

		return {
			'vectorstores': list(index_stats),
		}

	##############################################################
	### Delete Pinecone Vectorstore
	##############################################################
	def delete_redis_vectorstore(self, prefix: str):
		## Get Tokens
		keys = ['REDIS_URL']
		tokens = self.user_repo.find_token(self.user_id, keys)
		## Check for token, else throw error
		validator.validate_api_keys(tokens, keys)
		## Delete Vectorstore
		redis_service = RedisService(
			redis_url=tokens.get('REDIS_URL'),
			index_name=prefix,
		)
		deleted = redis_service.delete(index_name=prefix)
		if deleted:
			return True
		else:
			return False