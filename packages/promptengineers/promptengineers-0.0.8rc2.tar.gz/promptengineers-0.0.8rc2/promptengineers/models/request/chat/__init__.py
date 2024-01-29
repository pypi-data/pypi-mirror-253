"""Request Models"""
from typing import Any, List, Optional, Union
from pydantic import BaseModel, Field

from promptengineers.models import Retrieval

#################################################
## ChatGPT
#################################################
class ReqBodyChat(BaseModel):  # pylint: disable=too-few-public-methods
    """A message to send to the chatbot."""

    title: Optional[str] = None
    model: Optional[str] = None
    messages: Optional[Any] = None
    temperature: Optional[float or int] = None
    stream: Optional[bool] = None

    __config__ = {
		"json_schema_extra": {
            "example": {
                "model": "gpt-3.5-turbo",
                "temperature": 0.8,
                "stream": False,
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": "Who won the 2001 world series?"},
                    {
                        "role": "assistant",
                        "content": "The arizona diamondbacks won the 2001 world series.",
                    },
                    {"role": "user", "content": "Who were the pitchers?"},
                ],
            }
        }
    }

class ReqBodyAgentChat(ReqBodyChat):  # pylint: disable=too-few-public-methods
    """A message to send to the chatbot."""

    tools: list[str] = None
    plugins: list[str] = None
    retrieval: Retrieval = None

    __config__ = {
		"json_schema_extra": {
            "example": {
                "model": "gpt-3.5-turbo",
                "temperature": 0.8,
                "stream": False,
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {
                        "role": "user",
                        "content": "What will $2000 compounded at 5 percent for 10 years be?",
                    },
                ],
                "tools": ["math_tool"],
                "plugins": ["https://api.speak.com/.well-known/ai-plugin.json"],
                "retrieval": {
                    "provider": "pinecone",
                    "index_name": "Formio",
                }
            }
        }
    }


class ReqBodyAgentPluginsChat(ReqBodyChat):  # pylint: disable=too-few-public-methods
    """A message to send to the chatbot."""

    plugins: list[str] = None

    __config__ = {
		"json_schema_extra": {
            "example": {
                "model": "gpt-3.5-turbo-16k",
                "temperature": 0.8,
                "stream": False,
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {
                        "role": "user",
                        "content": "Using the Speak tool, how should I politely greet shop employees when I enter, in French?",
                    },
                ],
                "plugins": ["https://api.speak.com/.well-known/ai-plugin.json"],
            }
        }
    }

class ReqBodyVectorstoreChat(ReqBodyChat):  # pylint: disable=too-few-public-methods
    """A message to send to the chatbot."""

    vectorstore: Optional[str] = None
    provider: Optional[str] = None

    __config__ = {
		"json_schema_extra": {
            "example": {
                "provider": "pinecone",
                "vectorstore": "Formio",
                "model": "gpt-3.5-turbo",
                "temperature": 0.8,
                "stream": False,
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": "Can you summarize the context?"},
                ],
            }
        }
    }


class ReqBodyFunctionChat(ReqBodyChat):  # pylint: disable=too-few-public-methods
    """A message to send to the chatbot."""

    functions: list[str] = []

    __config__ = {
		"json_schema_extra": {
            "example": {
                "model": "gpt-3.5-turbo",
                "temperature": 0.8,
                "messages": [
					{"role": "system", "content": "You are a helpful assistant."},
					{"role": "user", "content": 'What is the length of supercalifragilisticexpialidocious?'},
				],
                "functions": ["get_word_length"],
            }
        }
    }