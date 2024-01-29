"""Chat Controller"""
import asyncio
from typing import Any, AsyncIterable

# from fastapi import Request
from langchain.chains import LLMChain
from langchain.callbacks import AsyncIteratorCallbackHandler, get_openai_callback

from promptengineers.core.config.llm import ACCEPTED_OLLAMA_MODELS, ACCEPTED_OPENAI_MODELS
from promptengineers.llms.services.langchain.callbacks import AgentStreamCallbackHandler
from promptengineers.llms.strategies import OllamaStrategy, OpenAIStrategy, ModelContext
from promptengineers.llms.utils import retrieve_chat_messages, retrieve_system_message, get_chat_history
from promptengineers.stream.utils import token_stream, wrap_done
from promptengineers.prompts.templates import get_system_template

##############################################################################
## Normal Chat
##############################################################################
async def langchain_http_chat(
    messages: list[dict],
    model: str,
    temperature: float or int = 0.0,
    openai_api_key: str = None,
    ollama_base_url: str = None,
) -> (str, Any):
    # Retrieve the chat messages
    filtered_messages = retrieve_chat_messages(messages)
    # Retrieve the chat history
    chat_history = list(zip(filtered_messages[::2], filtered_messages[1::2]))
    # Retrieve the system message
    system_message = retrieve_system_message(messages)
    # Check allowed
    if model in ACCEPTED_OPENAI_MODELS:
        model_service = ModelContext(strategy=OpenAIStrategy(api_key=openai_api_key))
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
## Langchain Chat Stream
##############################################################################
async def langchain_stream_chat(
    messages: list[dict],
    model:str,
    temperature: float or int = 0.0,
    openai_api_key: str = None,
    ollama_base_url: str = None,
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
        model_service = ModelContext(strategy=OpenAIStrategy(api_key=openai_api_key))
        callback = AsyncIteratorCallbackHandler()
        model = model_service.chat(
            model_name=model,
            temperature=temperature,
            streaming=True,
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
        template = get_system_template(system_message)
        prompt = template.format(
            context=get_chat_history(chat_history),
            question=filtered_messages[-1]
        )
        # Yield the tokens as they come in.
        for token in llm._stream(prompt):
            yield token_stream(token.text)
        yield token_stream()