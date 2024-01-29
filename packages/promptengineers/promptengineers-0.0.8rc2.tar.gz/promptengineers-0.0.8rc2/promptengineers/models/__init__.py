from typing import Optional
from pydantic import BaseModel

class Retrieval(BaseModel):
    """Contains the information needed to document retrieval augmented generation."""

    provider: Optional[str] = None
    index_name: Optional[str] = None

    __config__ = {
		"json_schema_extra": {
            "example": {
                "provider": "pinecone",
                "index_name": "Formio",
            }
        }
    }