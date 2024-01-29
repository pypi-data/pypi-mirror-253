"""Retrieval Chat"""
from typing import AsyncIterable, Union, Any

from langchain.callbacks import get_openai_callback
from promptengineers.core.config.llm import ACCEPTED_OLLAMA_MODELS, ACCEPTED_OPENAI_MODELS, OpenAIModels
from promptengineers.llms.services.langchain.callbacks import AgentStreamCallbackHandler
from promptengineers.llms.services.langchain.chains import ChainService
from promptengineers.llms.strategies import OllamaStrategy, OpenAIStrategy, ModelContext
from promptengineers.llms.utils import retrieve_chat_messages, retrieve_system_message, get_chat_history
from promptengineers.models.message import SystemMessage, UserMessage, AssistantMessage
from promptengineers.retrieval.strategies import VectorstoreContext
from promptengineers.stream.utils import token_stream
from promptengineers.prompts.templates import get_retrieval_template

############################################################################
## Prompt Engineers AI - Retrieval HTTP Chat
############################################################################
async def langchain_http_retrieval_chat(
	messages: list[Union[SystemMessage, UserMessage, AssistantMessage]],
	model: str = OpenAIModels.GPT_3_5_TURBO_16K.value,
	temperature: float or int = 0.9,
	vectorstore: VectorstoreContext = None,
	openai_api_key: str = None,
) -> (str, Any):
	"""Send a message to the chatbot and yield the response."""
	filtered_messages = retrieve_chat_messages(messages)
	# Retrieve the chat history
	chat_history = list(zip(filtered_messages[::2], filtered_messages[1::2])) ## TODO: Fix this
	# Retrieve the system message
	system_message = retrieve_system_message(messages)
	# Create the model
	if model in ACCEPTED_OPENAI_MODELS:
		model_service = ModelContext(strategy=OpenAIStrategy(api_key=openai_api_key))
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

############################################################################
## Prompt Engineers AI - Retrieval Stream Chat
############################################################################
async def langchain_stream_retrieval_chat(
	messages: list[Union[SystemMessage, UserMessage, AssistantMessage]],
	model: OpenAIModels,
	temperature: float = 0.9,
	vectorstore: VectorstoreContext = None,
	openai_api_key: str = None,
	ollama_base_url: str = None,
) -> AsyncIterable[str]:
	"""Send a message to the chatbot and yield the response."""
	filtered_messages = retrieve_chat_messages(messages)
	# Retrieve the chat history
	chat_history = list(zip(filtered_messages[::2], filtered_messages[1::2]))
	# Retrieve the system message
	system_message = retrieve_system_message(messages)
	# Create the callback
	callback = AgentStreamCallbackHandler()
	# Create the model
	if model in ACCEPTED_OPENAI_MODELS:
		model_service = ModelContext(strategy=OpenAIStrategy(api_key=openai_api_key))
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
		if ollama_base_url:
			strategy = OllamaStrategy(base_url=ollama_base_url)
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