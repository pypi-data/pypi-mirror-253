from pydantic import BaseModel, Field

class SystemMessage(BaseModel):
	"""A message from the system."""
	role: str = Field(...)
	content: str = Field(...)

	__config__ = {
		"json_schema_extra": {
			"example": {
				"role": "system",
				"content": "You are a helpful assistant."
			}
		}
	}

class UserMessage(BaseModel):
	"""A message from the user."""
	role: str = Field(...)
	content: str = Field(...)

	__config__ = {
		"json_schema_extra": {
			"example": {
				"role": "user",
				"content": "Who won the 2001 world series?"
			}
		}
	}

class AssistantMessage(BaseModel):
	"""A message from the assistant."""
	role: str = Field(...)
	content: str = Field(...)

	__config__ = {
		"json_schema_extra": {
			"example": {
				"role": "assistant",
				"content": "The arizona diamondbacks won the 2001 world series."
			}
		}
	}