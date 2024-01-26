import ujson
import traceback

from fastapi import APIRouter, Depends, Request, Response, HTTPException
from fastapi.responses import StreamingResponse

from promptengineers.chat import (langchain_http_agent_chat, langchain_stream_agent_chat,
									langchain_http_retrieval_chat, langchain_stream_retrieval_chat)
from promptengineers.fastapi.controllers import ChatController
from promptengineers.core.exceptions import ValidationException
from promptengineers.retrieval.factories import RetrievalFactory, EmbeddingFactory
from promptengineers.models.request import ReqBodyChat, ReqBodyAgentChat, ReqBodyVectorstoreChat
from promptengineers.models.response import (ResponseChat, ResponseAgentChat, ResponseVectorstoreChat,
									RESPONSE_STREAM_AGENT_CHAT, RESPONSE_STREAM_VECTORSTORE_CHAT,
									RESPONSE_STREAM_CHAT)
from promptengineers.retrieval.strategies import VectorstoreContext
from promptengineers.core.utils import logger
from promptengineers.llms.utils import gather_tools, retrieve_system_message
from promptengineers.tools.utils import format_agent_actions
from promptengineers.core.exceptions import NotFoundException

router = APIRouter()
TAG = "Chat"

def get_controller(request: Request) -> ChatController:
	try:
		return ChatController(
			request=request, 
			user_repo=request.state.user_repo, 
			available_tools=request.state.available_tools
		)
	except NotFoundException as e:
		# Handle specific NotFoundException with a custom message or logging
		logger.warn(f"Failed to initialize HistoryController: {str(e)}")
		raise HTTPException(status_code=404, detail=f"Initialization failed: {str(e)}") from e
	except Exception as e:
		# Catch all other exceptions
		logger.error(f"Unexpected error initializing HistoryController: {str(e)}")
		raise HTTPException(status_code=500, detail="Internal server error") from e

#################################################
# ChatGPT
#################################################
@router.post(
	"/chat",
	tags=[TAG],
	name='chat',
	response_model=ResponseChat,
	responses={
		200: {
			"content": {
				"text/event-stream": {
					"example": RESPONSE_STREAM_CHAT
				}
			}
		}
	},
)
async def chat(
	body: ReqBodyChat,
	chat_controller: ChatController = Depends(get_controller),
):
	"""Chat endpoint."""
	try:
		logger.debug('[POST /chat] Query: %s', str(body))
		# You can use the stream variable in your function as needed
		if not body.stream:
			# Format Response
			result, cb = await chat_controller.langchain_http_chat(
				messages=body.messages,
				model=body.model,
				temperature=body.temperature
			)
			data = ujson.dumps({
				'message': result,
				'usage': {
					'total_tokens': cb.total_tokens,
					'prompt_tokens': cb.prompt_tokens,
					'completion_tokens': cb.completion_tokens,
					'total_cost': cb.total_cost,
					'successful_requests': cb.successful_requests
				},
			})
			logger.debug('[POST /chat] Result: %s', str(data))
			return Response(
				content=data,
				media_type='application/json',
				status_code=200
			)

		return StreamingResponse(
			chat_controller.langchain_stream_chat(
				messages=body.messages,
				model=body.model,
				temperature=body.temperature
			),
			headers={
				"Cache-Control": "no-cache",
				"Connection": "keep-alive",
				"Content-Type": "text/event-stream",
			}
		)
	except Exception as err:
		tb = traceback.format_exc()
		logger.error("[routes.chat.chat] Exception: %s\n%s", err, tb)
		raise HTTPException(status_code=500, detail="Internal Server Error") from err



#################################################
# Langchain Agent
#################################################
@router.post(
	"/chat/agent",
	tags=[TAG],
	name='chat_agent',
	response_model=ResponseAgentChat,
	responses={
		200: {
			"content": {
				"text/event-stream": {
					"example": RESPONSE_STREAM_AGENT_CHAT
				}
			}
		}
	},
)
async def agent(
	body: ReqBodyAgentChat,
	chat_controller: ChatController = Depends(get_controller),
):
	"""Chat endpoint."""
	try:
		tokens = await chat_controller.user_repo.find_token(
			chat_controller.user_id, 
			['OPENAI_API_KEY', 'PINECONE_API_KEY', 'PINECONE_ENV', 'PINECONE_INDEX', 'REDIS_URL']
		)

		vectorstore = None
		if body.retrieval.provider and body.retrieval.index_name:

			# Generate Embeddings
			embedding = EmbeddingFactory(body.model, tokens.get('OPENAI_API_KEY'))

			if body.retrieval.provider == 'redis':
				provider_keys={
					'redis_url': tokens.get('REDIS_URL'),
					'index_name': f"{chat_controller.request.state.user_id}::{body.retrieval.index_name}",
				}
			elif body.retrieval.provider == 'pinecone':
				provider_keys = {
					'api_key': tokens.get('PINECONE_API_KEY'),
					'env': tokens.get('PINECONE_ENV'),
					'index_name': tokens.get('PINECONE_INDEX'),
					'namespace': f"{chat_controller.request.state.user_id}::{body.retrieval.index_name}",
				}
			else:
				raise HTTPException(
					status_code=400,
					detail=f"Invalid retrieval provider: {body.retrieval.provider}"
				)

			retrieval_provider = RetrievalFactory(
				provider=body.retrieval.provider,
				embeddings=embedding.create_embedding(),
				provider_keys=provider_keys
			)
			vectostore_service = VectorstoreContext(retrieval_provider.create_strategy())
			vectorstore = vectostore_service.load()
		
		tools = gather_tools(
			tools=body.tools,
			available_tools=chat_controller.available_tools,
			vectorstore=vectorstore,
			plugins=body.plugins
		)
		if not tools:
			raise HTTPException(
				status_code=400,
				detail="No tools selected"
			)

		# Retrieve the system message
		system_message = retrieve_system_message(body.messages)
		# Attach the application user id to the system message
		system_message = system_message + '\n' + "USER_ID=" + str(chat_controller.user_id)
		body.messages[0]['content'] = system_message

		# You can use the stream variable in your function as needed
		if not body.stream:
			# Format Response
			result, cb = await langchain_http_agent_chat(
				messages=body.messages,
				model=body.model,
				tools=tools,
				temperature=body.temperature,
				openai_api_key=tokens.get('OPENAI_API_KEY'),
			)
			data = ujson.dumps({
				'message': result['output'],
				'actions': format_agent_actions(result['intermediate_steps']),
				'usage': {
					'total_tokens': cb.total_tokens,
					'prompt_tokens': cb.prompt_tokens,
					'completion_tokens': cb.completion_tokens,
					'total_cost': cb.total_cost,
					'successful_requests': cb.successful_requests
				},
			})
			logger.debug('[POST /chat/agent] Result: %s', str(data))
			return Response(
				content=data,
				media_type='application/json',
				status_code=200
			)

		return StreamingResponse(
			langchain_stream_agent_chat(
				messages=body.messages,
				model=body.model,
				temperature=body.temperature,
				tools=tools,
				openai_api_key=tokens.get('OPENAI_API_KEY'),
			),
			headers={
				"Cache-Control": "no-cache",
				"Connection": "keep-alive",
				"Content-Type": "text/event-stream",
			}
		)
	except Exception as err:
		tb = traceback.format_exc()
		logger.error("[routes.chat.vector_search] Exception: %s\n%s", err, tb)
		raise HTTPException(status_code=500, detail="Internal Server Error") from err

#################################################
# Langchain Vectorstore Route
#################################################
@router.post(
	"/chat/vectorstore",
	tags=[TAG],
	name='chat_vectorstore',
	response_model=ResponseVectorstoreChat,
	responses={
		200: {
			"content": {
				"text/event-stream": {
					"example": RESPONSE_STREAM_VECTORSTORE_CHAT
				}
			}
		}
	},
)
async def vector_search(
	body: ReqBodyVectorstoreChat,
	chat_controller: ChatController = Depends(get_controller),
):
	"""Chat Vectorstore endpoint."""
	try:
		# Log Context Details
		logger.debug('[POST /chat/vectorstore] Query: %s', str(body))

		# Retrieve User Tokens
		tokens = await chat_controller.user_repo.find_token(
			chat_controller.user_id, 
			['OPENAI_API_KEY', 'PINECONE_API_KEY', 'PINECONE_ENV', 'PINECONE_INDEX', 'REDIS_URL']
		)

		# Generate Embeddings
		embedding = EmbeddingFactory(body.model, tokens.get('OPENAI_API_KEY'))

		if body.provider == 'redis':
			provider_keys={
				'redis_url': tokens.get('REDIS_URL'),
				'index_name': f"{chat_controller.request.state.user_id}::{body.vectorstore}",
			}
		elif body.provider == 'pinecone':
			provider_keys = {
				'api_key': tokens.get('PINECONE_API_KEY'),
				'env': tokens.get('PINECONE_ENV'),
				'index_name': tokens.get('PINECONE_INDEX'),
				'namespace': f"{chat_controller.request.state.user_id}::{body.vectorstore}",
			}
		else:
			raise HTTPException(
				status_code=400,
				detail=f"Invalid retrieval provider: {body.provider}"
			)

		retrieval_provider = RetrievalFactory(
			provider=body.provider,
			embeddings=embedding.create_embedding(),
			provider_keys=provider_keys
		)
		vectostore_service = VectorstoreContext(retrieval_provider.create_strategy())
		vectorstore = vectostore_service.load()

		# Check if the retrieved file is empty
		if not vectorstore:
			raise HTTPException(
				status_code=404,
				detail=f"Vectorstore {body.vectorstore} not found"
			)

		# You can use the stream variable in your function as needed
		if not body.stream:
			# Format Response
			result, cb = await langchain_http_retrieval_chat(
				messages=body.messages,
				model=body.model,
				temperature=body.temperature,
				vectorstore=vectorstore,
				openai_api_key=tokens.get('OPENAI_API_KEY'),
			)
			formatted_docs = []
			for doc in result['source_documents']:
				formatted_docs.append({
					'page_content': doc.page_content,
					'metadata': doc.metadata,
				})
			data = ujson.dumps({
				'message': result['answer'],
				'documents': formatted_docs,
				'usage': {
					'total_tokens': cb.total_tokens,
					'prompt_tokens': cb.prompt_tokens,
					'completion_tokens': cb.completion_tokens,
					'total_cost': cb.total_cost,
					'successful_requests': cb.successful_requests
				},
			})
			logger.debug('[POST /chat/vectorstore] Result: %s', str(data))
			return Response(
				content=data,
				media_type='application/json',
				status_code=200
			)

		# Process Query
		return StreamingResponse(
			langchain_stream_retrieval_chat(
				messages=body.messages,
				model=body.model,
				temperature=body.temperature,
				vectorstore=vectorstore,
				openai_api_key=tokens.get('OPENAI_API_KEY'),
			),
			media_type="text/event-stream"
		)
	except ValidationException as err:
		logger.warning("[routes.chat.vector_search] ValidationException: %s", err)
		raise HTTPException(
			status_code=400,
			detail=str(err)
		) from err
	except HTTPException as err:
		logger.error("[routes.chat.vector_search] HTTPException: %s", err.detail)
		raise
	except Exception as err:
		tb = traceback.format_exc()
		logger.error("[routes.chat.vector_search] Exception: %s\n%s", err, tb)
		raise HTTPException(status_code=500, detail="Internal Server Error") from err
