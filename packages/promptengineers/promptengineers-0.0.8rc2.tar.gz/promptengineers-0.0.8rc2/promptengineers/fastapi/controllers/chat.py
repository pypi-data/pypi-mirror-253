"""Chat Controller"""
import ujson
import openai
import asyncio
from typing import Any, Union, AsyncIterable

# from fastapi import Request
from langchain.chains import LLMChain
from langchain.callbacks import AsyncIteratorCallbackHandler, get_openai_callback

from promptengineers.core.config.llm import ACCEPTED_OLLAMA_MODELS, ACCEPTED_OPENAI_MODELS, OpenAIModels
from promptengineers.core.interfaces.repos import IUserRepo
from promptengineers.models.message import SystemMessage, UserMessage, AssistantMessage
from promptengineers.repos.user import UserRepo
from promptengineers.llms.services.openai import openai_chat_functions_model
from promptengineers.llms.services.langchain.callbacks import AgentStreamCallbackHandler
from promptengineers.llms.services.langchain.chains import ChainService
from promptengineers.llms.strategies import OllamaStrategy, OpenAIStrategy, ModelContext
from promptengineers.llms.utils import retrieve_chat_messages, retrieve_system_message, get_chat_history, combine_documents
from promptengineers.retrieval.strategies import VectorstoreContext
from promptengineers.stream.utils import token_stream, wrap_done
from promptengineers.core.validations import Validator
from promptengineers.prompts.templates import get_system_template, get_retrieval_template

validator = Validator()

class ChatController:
	def __init__(
		self,
		user_id: str = None,
		# request: Request = None,
		request = None,
		user_repo: IUserRepo = None,
		available_tools: dict[str, Any] = None
	):
		self.request = request
		self.user_id = user_id or getattr(request.state, "user_id", None)
		self.user_repo = user_repo or UserRepo()
		self.available_tools = available_tools or None

	#######################################################
	## Open AI Chat GPT
	#######################################################
	def openai_http_chat(
		self,
		messages,
		model:str,
		temperature: float or int = 0.0,
		stream: bool = False,
	) -> AsyncIterable[str]:
		"""Send a message to the chatbot and yield the response."""
		response = openai.ChatCompletion.create(
			model=model,
			messages=messages,
			temperature=temperature,
			stream=stream
		)
		return response

	async def openai_stream_chat(
		self,
		messages,
		model:str,
		temperature: float or int = 0.0
	) -> AsyncIterable[str]:
		"""Send a message to the chatbot and yield the response."""
		response = openai.ChatCompletion.create(
			model=model,
			messages=messages,
			temperature=temperature,
			stream=True
		)
		for chunk in response:
			## Would also consider gathering data here
			token = chunk['choices'][0]['delta'].get('content', '')
			yield token_stream(token)
		yield token_stream()

	#######################################################
	## Open AI Function Calling
	#######################################################
	def openai_http_function_chat(
		self,
		messages,
		model: str,
		functions: list[str],
		temperature: float or int = 0
	):
		"""Send a message to the chatbot and yield the response."""
		response = openai_chat_functions_model(
			messages=messages,
			model_name=model,
			temperature=temperature,
			streaming=False,
			keys=functions,
		)
		return response

	async def openai_stream_function_chat(
		self,
		messages,
		model: str,
		functions: list[str],
		temperature: float or int = 0
	) -> AsyncIterable[str]:
		"""Send a message to the chatbot and yield the response."""
		response = openai_chat_functions_model(
			messages=messages,
			model_name=model,
			temperature=temperature,
			streaming=True,
			keys=functions,
		)
		for chunk in response:
			token = chunk['choices'][0]['delta'].get('content', '')
			yield token_stream(token)
		yield token_stream()

	##############################################################################
	## Normal Chat
	##############################################################################
	async def langchain_http_chat(
		self,
		messages,
		model: str,
		temperature: float or int = 0.0,
	) -> (str, Any):
		# Retrieve the chat messages
		filtered_messages = retrieve_chat_messages(messages)
		# Retrieve the chat history
		chat_history = list(zip(filtered_messages[::2], filtered_messages[1::2]))
		# Retrieve the system message
		system_message = retrieve_system_message(messages)
		# Get Tokens
		api_key = await self.user_repo.find_token(self.user_id, 'OPENAI_API_KEY')
		# Check allowed
		if model in ACCEPTED_OPENAI_MODELS:
			model_service = ModelContext(strategy=OpenAIStrategy(api_key=api_key))
		# Construct the model
		model = model_service.chat(
			model_name=model,
			temperature=temperature,
			streaming=False
		)
		query = {'question': filtered_messages[-1], 'chat_history': chat_history}
		with get_openai_callback() as cb:
			# Retrieve the conversation
			chain = LLMChain(llm=model, prompt=get_system_template(system_message))
			# Begin a task that runs in the background.
			response = chain.run(query)
		return response, cb

	##############################################################################
	## Langchain Agent Chat
	##############################################################################
	async def langchain_http_agent_chat(
		self,
		messages,
		model: str,
		tools,
		temperature: float or int = 0.0,
	) -> (str, Any):
		"""Send a message to the chatbot and yield the response."""
		filtered_messages = retrieve_chat_messages(messages)
		# Retrieve the chat history
		chat_history = list(zip(filtered_messages[::2], filtered_messages[1::2]))
		# Retrieve the system message
		system_message = retrieve_system_message(messages)
		# Attach the application user id to the system message
		system_message = system_message + '\n' + "USER_ID=" + str(self.user_id)
		# Get Tokens
		api_key = await self.user_repo.find_token(self.user_id, 'OPENAI_API_KEY')
		# Create the model
		if model in ACCEPTED_OPENAI_MODELS:
			model_service = ModelContext(strategy=OpenAIStrategy(api_key=api_key))
		else:
			raise NotImplementedError(f"Model {model} not implemented")

		model = model_service.chat(
			model_name=model,
			temperature=temperature,
			streaming=False
		)
		with get_openai_callback() as cb:
			# Retrieve the conversation
			chain = ChainService(model).agent_with_tools(system_message=system_message,
														chat_history=chat_history,
														tools=tools)
			# Begin a task that runs in the background.
			response = await chain.ainvoke(filtered_messages[-1])
		return response, cb

	##############################################################################
	## Langchain Vectorstore Chat
	##############################################################################
	async def langchain_http_vectorstore_chat(
		self,
		messages: list[Union[SystemMessage, UserMessage, AssistantMessage]] = None,
		model: str = OpenAIModels.GPT_3_5_TURBO_16K.value,
		temperature: float or int = 0.9,
		vectorstore: VectorstoreContext = None,
	) -> (str, Any):
		"""Send a message to the chatbot and yield the response."""
		filtered_messages = retrieve_chat_messages(messages)
		# Retrieve the chat history
		chat_history = list(zip(filtered_messages[::2], filtered_messages[1::2])) ## TODO: Fix this
		# Retrieve the system message
		system_message = retrieve_system_message(messages)
		# Get Tokens
		api_key = await self.user_repo.find_token(self.user_id, 'OPENAI_API_KEY')
		# Create the model
		if model in ACCEPTED_OPENAI_MODELS:
			model_service = ModelContext(strategy=OpenAIStrategy(api_key=api_key))
		else:
			raise NotImplementedError(f"Model {model} not implemented")

		model = model_service.chat(
			model_name=model,
			temperature=temperature,
			streaming=False
		)
		with get_openai_callback() as cb:
			# Retrieve the conversation
			chain = ChainService(model).conversation_retrieval(
				system_message=system_message, vectorstore=vectorstore, chat_history=chat_history
			)
			# Begin a task that runs in the background.
			response = chain(filtered_messages[-1], return_only_outputs=True)
		return response, cb

	##############################################################################
	## Langchain Chat Stream
	##############################################################################
	async def langchain_stream_chat(
		self,
		messages,
		model:str,
		temperature: float or int = 0.0,
		stream: bool = True,
	) -> AsyncIterable[str]:
		"""Send a message to the chatbot and yield the response."""
		filtered_messages = retrieve_chat_messages(messages)
		# Retrieve the chat history
		chat_history = list(zip(filtered_messages[::2], filtered_messages[1::2]))
		# Retrieve the system message
		system_message = retrieve_system_message(messages)

		# Create the model
		if model in ACCEPTED_OPENAI_MODELS:
			# Get Tokens
			api_key = await self.user_repo.find_token(self.user_id, 'OPENAI_API_KEY')
			model_service = ModelContext(strategy=OpenAIStrategy(api_key=api_key))
			callback = AsyncIteratorCallbackHandler()
			model = model_service.chat(
				model_name=model,
				temperature=temperature,
				streaming=stream,
				callbacks=[callback]
			)
			query = {'question': filtered_messages[-1], 'chat_history': chat_history}
			# Retrieve the conversation
			chain = LLMChain(llm=model, prompt=get_system_template(system_message))
			# Begin a task that runs in the background.
			task = asyncio.create_task(wrap_done(
				chain.acall(query),
				callback.done),
			)
			# Yield the tokens as they come in.
			async for token in callback.aiter():
				yield token_stream(token)
			yield token_stream()
			await task
		elif model in ACCEPTED_OLLAMA_MODELS:
			# Get Tokens
			base_url = await self.user_repo.find_token(self.user_id, 'OLLAMA_BASE_URL')
			if base_url:
				strategy = OllamaStrategy(base_url=base_url)
			else:
				strategy = OllamaStrategy()
			model_service = ModelContext(strategy=strategy)
			callback = AgentStreamCallbackHandler()
			llm = model_service.chat(
				model_name=model,
				temperature=temperature,
				streaming=stream,
				callbacks=[callback]
			)
			template = get_system_template(system_message)
			prompt = template.format(
				context=get_chat_history(chat_history),
				question=filtered_messages[-1]
			)
			# Yield the tokens as they come in.
			for token in llm._stream(prompt):
				yield token_stream(token.text)
			yield token_stream()

	#######################################################
	## Langchain Agent Stream Chat
	#######################################################
	async def langchain_stream_agent_chat(
		self,
		messages,
		model: str,
		tools,
		temperature: float or int = 0.0,
	):
		"""Send a message to the chatbot and yield the response."""
		filtered_messages = retrieve_chat_messages(messages)
		# Retrieve the chat history
		chat_history = list(zip(filtered_messages[::2], filtered_messages[1::2]))
		# Retrieve the system message
		system_message = retrieve_system_message(messages)
		# Attach the application user id to the system message
		system_message = system_message + '\n' + "USER_ID=" + str(self.user_id)
		# Get Tokens
		api_key = await self.user_repo.find_token(self.user_id, 'OPENAI_API_KEY')
		# Create the model
		if model in ACCEPTED_OPENAI_MODELS:
			model_service = ModelContext(strategy=OpenAIStrategy(api_key=api_key))
		else:
			raise NotImplementedError(f"Model {model} not implemented")

		callback = AgentStreamCallbackHandler()
		model = model_service.chat(
			model_name=model,
			temperature=temperature,
			streaming=True,
			callbacks=[callback]
		)
		query = {'input': filtered_messages[-1], 'chat_history': chat_history}
		# tools = load_tools(tools, llm=model)
		agent_executor = ChainService(model).agent_with_tools(system_message=system_message,
															chat_history=chat_history,
															tools=tools,
															callbacks=[callback])
		runnable = agent_executor.astream_log(query)
		async for chunk in runnable:
			operation = chunk.ops[0]['value']
			if operation:
				if type(operation) == str:
					filled_chunk = operation
					if filled_chunk:
						yield token_stream(filled_chunk)
				else:
					generations = operation.get('generations', False)
					if generations:
						function_call = generations[0][0].get('message', {}).additional_kwargs.get('function_call', {})
						tool = function_call.get('name', None)
						if tool:
							yield token_stream(tool, 'tool')
						args = function_call.get('arguments', None)
						if args:
							if type(args) == str:
								tool_args = ujson.loads(args)
							else:
								tool_args =  ujson.loads(args)['__arg1']

							yield token_stream(f"Invoking: `{tool}` with `{tool_args}`", 'log')
		yield token_stream()

	#######################################################
	## Vectorstore
	#######################################################
	async def langchain_stream_vectorstore_chat(
		self,
		messages: list[str],
		model: str,
		temperature: float or int = 0.9,
		vectorstore: VectorstoreContext = None,
	) -> AsyncIterable[str]:
		"""Send a message to the chatbot and yield the response."""
		filtered_messages = retrieve_chat_messages(messages)
		# Retrieve the chat history
		chat_history = list(zip(filtered_messages[::2], filtered_messages[1::2]))
		# Retrieve the system message
		system_message = retrieve_system_message(messages)
		# Get Tokens
		api_key = await self.user_repo.find_token(self.user_id, 'OPENAI_API_KEY')
		# Create the callback
		callback = AgentStreamCallbackHandler()
		# Create the model
		if model in ACCEPTED_OPENAI_MODELS:
			model_service = ModelContext(strategy=OpenAIStrategy(api_key=api_key))
			llm = model_service.chat(
				model_name=model,
				temperature=temperature,
				streaming=True,
				callbacks=[callback]
			)
			# Retrieve the conversation
			qa_chain = ChainService(llm).conversation_retrieval(
				system_message=system_message,
				chat_history=chat_history,
				vectorstore=vectorstore,
				callbacks=[callback]
			)
			runnable = qa_chain.astream_log(filtered_messages[-1])
			docs_processed = False
			async for chunk in runnable:
				operation = chunk.ops[0]['value']
				# print(operation)
				async for chunk in runnable:
					operation = chunk.ops[0]['value']
					return_output = False

					if isinstance(operation, dict):
						docs = operation.get('documents')
						if docs:
							for doc in docs:
								yield token_stream({
									'page_content': doc.page_content,
									'metadata': doc.metadata,
								}, 'doc')
							docs_processed = True  # Set this flag when docs are processed

					# Check if docs have been processed at least once
					if docs_processed:
						return_output = True

					if operation and isinstance(operation, str) and return_output:
						yield token_stream(operation)
			yield token_stream()

		elif model in ACCEPTED_OLLAMA_MODELS:
			base_url = await self.user_repo.find_token(self.user_id, 'OLLAMA_BASE_URL')
			if base_url:
				strategy = OllamaStrategy(base_url=base_url)
			else:
				strategy = OllamaStrategy()
			model_service = ModelContext(strategy=strategy)
			callback = AgentStreamCallbackHandler()
			llm = model_service.chat(
				model_name=model,
				temperature=temperature,
				streaming=True,
				callbacks=[callback]
			)
			question = filtered_messages[-1]
			template = get_retrieval_template(system_message)
			history = get_chat_history(chat_history)
			documents = vectorstore.similarity_search(question)
			context = '\n'.join([doc.page_content for doc in documents])
			prompt = template.format(
				chat_history=history,
				context=context,
				question=question
			)
			# Yield the tokens as they come in.
			for token in llm._stream(prompt):
				yield token_stream(token.text)
			yield token_stream()
		else:
			raise NotImplementedError(f"Model {model} not implemented")
