from typing import List

from promptengineers.models.prompt import PromptSystem

STRIPE_API_DOC_PROMPT = {
	"title": "Stripe Document Retreival Prompt",
	"system": "You are a helpful {ASSISTANT_TYPE} assistant. You have have been given context to {INDEX_NAME} to answer user questions.",
	"variables": {
		"ASSISTANT_TYPE": 'document retreival',
		"INDEX_NAME": 'Stripe API docs'
	}
}

class ResponsePromptSystemList(PromptSystem): # pylint: disable=too-few-public-methods
	prompts: List[PromptSystem] = []

	__config__ = {
		"json_schema_extra": {
			"example": {
				"prompts": [STRIPE_API_DOC_PROMPT]
			}
		}
	}

class ResponsePromptSystem(PromptSystem): # pylint: disable=too-few-public-methods

	__config__ = {
		"json_schema_extra": {
			"example": {
				"prompt": STRIPE_API_DOC_PROMPT
			}
		}
	}