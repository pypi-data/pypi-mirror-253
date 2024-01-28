"""Chat History Request Models"""
from typing import Optional
from pydantic import BaseModel

HISTORY = {
	"title": "World Series 2001 Chat History",
	"messages": [
		{"role": "system", "content": "You are a helpful assistant."},
		{"role": "user", "content": 'Who won the 2001 world series?'},
		{
			"role": "assistant", 
			"content": 'The arizona diamondbacks won the 2001 world series.',
			"actions": []
		},
	],
	"setting": "abcd147a12abcdefd9512345",
	"tags": ["baseball", "world series", "2001"],
}

HISTORY_DOCUMENT = {
	"_id": "653e147a126c8e67d951fd20",
	"title": "World Series 2001 Chat History",
	"messages": [
		{"role": "system", "content": "You are a helpful assistant."},
		{"role": "user", "content": 'Who won the 2001 world series?'},
		{
			"role": "assistant", 
			"content": 'The arizona diamondbacks won the 2001 world series.',
			"actions": []
		},
	],
	"setting": "abcd147a12abcdefd9512345",
	"tags": ["baseball", "world series", "2001"],
	"created_at": 1698523723,
	"updated_at": 1698562747
}

class History(BaseModel): # pylint: disable=too-few-public-methods
	"""A message to send to the chatbot."""
	messages: Optional[list]
	title: Optional[str] = None
	setting: Optional[str] = None
	tags: Optional[list[str]] = None

	__config__ = {
		"json_schema_extra": {
			"example": HISTORY
		}
	}

class HistoryDocument(History): # pylint: disable=too-few-public-methods
	"""A message to send to the chatbot."""
	_id: str
	created_at: int
	updated_at: int

	__config__ = {
		"json_schema_extra": {
			"example": HISTORY_DOCUMENT
		}
	}

class HistoryIndex(HistoryDocument): # pylint: disable=too-few-public-methods
	"""A message to send to the chatbot."""
	histories: list[History]

	__config__ = {
		"json_schema_extra": {
			"example": {
				"histories": [HISTORY_DOCUMENT]
			}
		}
	}
