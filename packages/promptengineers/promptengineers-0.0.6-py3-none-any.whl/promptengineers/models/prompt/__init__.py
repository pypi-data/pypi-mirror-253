from typing import Optional
from pydantic import BaseModel


class PromptSystem(BaseModel): # pylint: disable=too-few-public-methods
	"""Prompt System Template"""
	title: str
	system: str
	variables: Optional[dict] = None

	__config__ = {
		"json_schema_extra": {
			"example": {
				"title": "Helpful Assistant Prompt",
				"system": "You are a helpful {ASSISTANT_TYPE} assistant. You have have been given context to {INDEX_NAME} to answer user questions.",
				"variables": {
					"ASSISTANT_TYPE": 'document retreival',
					"INDEX_NAME": 'Stripe API docs'
                }
			}
		}
	}