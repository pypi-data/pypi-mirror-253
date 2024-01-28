"""Agent Chat"""
import ujson
from typing import Any

from langchain.callbacks import get_openai_callback
from promptengineers.core.config.llm import ACCEPTED_OPENAI_MODELS
from promptengineers.llms.services.langchain.callbacks import AgentStreamCallbackHandler
from promptengineers.llms.services.langchain.chains import ChainService
from promptengineers.llms.strategies import OpenAIStrategy, ModelContext
from promptengineers.llms.utils import retrieve_chat_messages, retrieve_system_message
from promptengineers.stream.utils import token_stream

############################################################################
## Prompt Engineers AI - Agent HTTP Chat
############################################################################
async def langchain_http_agent_chat(
    messages,
    model: str,
    tools,
    temperature: float or int = 0.0,
    openai_api_key: str = None,
) -> (str, Any):
    """Send a message to the chatbot and yield the response."""
    filtered_messages = retrieve_chat_messages(messages)
    # Retrieve the chat history
    chat_history = list(zip(filtered_messages[::2], filtered_messages[1::2]))
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
        chain = ChainService(model).agent_with_tools(system_message=system_message,
                                                    chat_history=chat_history,
                                                    tools=tools)
        # Begin a task that runs in the background.
        response = await chain.ainvoke(filtered_messages[-1])
    return response, cb


############################################################################
## Prompt Engineers AI - Agent Stream Chat
############################################################################
async def langchain_stream_agent_chat(
    messages,
    model: str,
    tools,
    temperature: float or int = 0.9,
    openai_api_key: str = None,
):
    """Send a message to the chatbot and yield the response."""
    filtered_messages = retrieve_chat_messages(messages)
    # Retrieve the chat history
    chat_history = list(zip(filtered_messages[::2], filtered_messages[1::2]))
    # Retrieve the system message
    system_message = retrieve_system_message(messages)
    # Create the model
    if model in ACCEPTED_OPENAI_MODELS:
        model_service = ModelContext(strategy=OpenAIStrategy(api_key=openai_api_key))
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
