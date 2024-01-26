"""Response models for the API."""
from pydantic import BaseModel, Field

from promptengineers.models.response.http import (
    ResponseStatus,
    ResponseChat,
    ResponseAgentChat,
    ResponseAgentPluginsChat,
    ResponseVectorstoreChat,
    ResponseCreateVectorStore,
    ResponseListPineconeVectorStores,
)
from promptengineers.models.response.stream import (
    RESPONSE_STREAM_AGENT_CHAT,
    RESPONSE_STREAM_VECTORSTORE_CHAT,
    RESPONSE_STREAM_AGENT_PLUGINS_CHAT,
    RESPONSE_STREAM_CHAT,
)
from .prompt import ResponsePromptSystemList, ResponsePromptSystem
from .settings import ResponseSetting, ResponseSettingsList
from .history import ResponseHistoryIndex, ResponseHistoryShow

class ResponseFileLoader(BaseModel):
    __config__ = {
		"json_schema_extra": {
            "example": {
                "message": "Vectorstore Created!",
                "vectorstore": "index_name",
            }
        }
    }


class ResponseChatStream(BaseModel):
    """A message to send to the chatbot."""

    sender: str = Field(default="assistant")
    message: str = Field(default="Dialog started.")
    type: str = Field(default="stream")


class ResponseRetrieveVectorstores(BaseModel):
    """A message to send to the chatbot."""

    __config__ = {
		"json_schema_extra": {"example": {"vectorstores": ["formio.pkl", "bullmq.pkl"]}}}


class ResponseRetrieveFiles(BaseModel):
    __config__ = {
		"json_schema_extra": {
            "example": {
                "files": [
                    "A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT.pdf",
                    "ai-village.pdf",
                ]
            }
        }
    }


class ResponseFileStorage(BaseModel):
    __config__ = {
		"json_schema_extra": {
            "example": {
                "message": "File(s) Uploaded!",
                "bucket_name": "prompt-engineers-dev",
                "files": [
                    "formio-standard-procedure.pdf",
                    "formio-interview-questions.pdf",
                ],
            }
        }
    }

class ResponseCreate(BaseModel):
    _id: str

    __config__ = {
		"json_schema_extra": {
            "example": {
                "_id": "5f7d0f0d5c3a3e2e3a3e2e3a",
            }
        }
    }

class ResponseUpdate(BaseModel):
    message: str

    __config__ = {
		"json_schema_extra": {
            "example": {
                "message": "Resource [{id}] updated successfully.",
            }
        }
    }

__all__ = [
    "ResponseStatus",
    "ResponseChat",
    "ResponseAgentChat",
    "ResponseAgentPluginsChat",
    "ResponseVectorstoreChat",
    "RESPONSE_STREAM_AGENT_CHAT",
    "RESPONSE_STREAM_AGENT_PLUGINS_CHAT",
    "RESPONSE_STREAM_VECTORSTORE_CHAT",
    "RESPONSE_STREAM_CHAT",
    "ResponseCreateVectorStore",
    "ResponseListPineconeVectorStores",
    "ResponsePromptSystemList",
    "ResponsePromptSystem",
    "ResponseSettingsList",
    "ResponseSetting",
    "ResponseHistoryIndex",
    "ResponseHistoryShow",
]
