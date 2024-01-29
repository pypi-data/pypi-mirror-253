"""Request Models"""
from typing import List
from pydantic import BaseModel, Field

from promptengineers.core.config.llm import OpenAIModels

class RequestMultiLoader(BaseModel):
    index_name: str = Field(...)
    provider: str = ("pinecone", "redis")
    embedding: str = (OpenAIModels.TEXT_EMBED_3_SMALL.value, "llama2:7b", "llama2")
    files: List[str] or None = Field(...)
    loaders: List[dict] or None = Field(...)

    __config__ = {
		"json_schema_extra": {
            "example": {
                "provider": "pinecone",
                "embedding": OpenAIModels.TEXT_EMBED_3_SMALL.value,
                "index_name": "formio-docs-and-website",
                "files": [
                    "formio-customer-issue.pdf",
                ],
                "loaders": [
                    {"type": "gitbook", "urls": ["https://help.form.io"]},
                    {"type": "web_base", "urls": ["https://form.io"]},
                ],
            }
        }
    }


class RequestDataLoader(BaseModel):
    index_name: str = Field(...)
    provider: str = ("pinecone", "redis")
    embedding: str = (OpenAIModels.TEXT_EMBED_3_SMALL.value, "llama2:7b", "llama2")
    loaders: List[dict] or None = Field(...)

    __config__ = {
		"json_schema_extra": {
            "example": {
                "provider": "pinecone",
                "embedding": OpenAIModels.TEXT_EMBED_3_SMALL.value,
                "index_name": "formio-docs-and-website",
                "loaders": [
                    {"type": "gitbook", "urls": ["https://help.form.io"]},
                    {"type": "web_base", "urls": ["https://form.io"]},
                    {"type": "copy", "text": "This is a test."},
                ],
            }
        }
    }