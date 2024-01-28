from typing import Optional
from pydantic import BaseModel

from promptengineers.models import Retrieval

CHAT_SETTINGS = {
	"title": "Prompt Engineers Core Repository Agent Settings",
    "model": "gpt-3.5-turbo",
    "system": """You are a helpful assistant. You are equipped with the following tools: {tools} for accomplishing tasks. If you to ask questions to perform a task, you can ask {vectorstore} for assistance.""",
    "temperature": 0.5,
	"stream": True,
    "tools": ["calculator", "github_new_issue", "github_edit_issue", "github_create_pull_request"],
    "plugins": ["https://domain-to-plugin-api.com/.well-known/ai-plugin.json"],
    "retrieval": {
		"provider": "pinecone",
		"index_name": "promptengineers-core-repository",
    },
	"tags": ["core", "repository", "promptengineers"]
}

CHAT_SETTING_DOCUMENT = {
	"_id": "532e147a126c8e67d951f234",
	"title": "Prompt Engineers Core Repository Agent Settings",
    "model": "gpt-3.5-turbo",
    "system": """You are a helpful assistant. You are equipped with the following tools: {tools} for accomplishing tasks. If you to ask questions to perform a task, you can ask {vectorstore} for assistance.""",
    "temperature": 0.5,
	"stream": True,
    "tools": ["calculator", "github_new_issue", "github_edit_issue", "github_create_pull_request"],
    "plugins": ["https://domain-to-plugin-api.com/.well-known/ai-plugin.json"],
    "retrieval": {
		"provider": "pinecone",
		"index_name": "promptengineers-core-repository",
    },
	"tags": ["core", "repository", "promptengineers"],
	"created_at": 1698523723,
	"updated_at": 1698562747
}

class ChatSettings(BaseModel): # pylint: disable=too-few-public-methods
	"""Chat Settings Template"""
	title: str
	model: str
	system: str
	temperature: Optional[float] = 0.5
	stream: Optional[bool] = False
	tools: Optional[list[str]] = None
	plugins: Optional[list[str]] = None
	retrieval: Retrieval = None
	tags: Optional[list[str]] = None

	__config__ = {
		"json_schema_extra": {
			"example": CHAT_SETTINGS
		}
	}

class ChatSettingDocument(ChatSettings): # pylint: disable=too-few-public-methods
	"""Chat Settings Template"""
	"""A message to send to the chatbot."""
	_id: str
	created_at: int
	updated_at: int

	__config__ = {
		"json_schema_extra": {
			"example": CHAT_SETTING_DOCUMENT
		}
	}

class ChatSettingIndex(ChatSettingDocument): # pylint: disable=too-few-public-methods
	"""Chat Settings Template"""
	"""A message to send to the chatbot."""
	settings: list[ChatSettings]

	__config__ = {
		"json_schema_extra": {
			"example": {
				"settings": [CHAT_SETTING_DOCUMENT]
			}
		}
	}