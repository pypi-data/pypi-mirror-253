from promptengineers.models.prompt import PromptSystem

class ReqBodyPromptSystem(PromptSystem): # pylint: disable=too-few-public-methods

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