"""Chat GPT Clone Prompt Template"""
from langchain.prompts import PromptTemplate

def get_system_template(system_message: str):
    prompt_template = f"""{system_message}
---
{{chat_history}}
User: {{question}}
Assistant: """
    template = PromptTemplate(
        template=prompt_template,
        input_variables=["chat_history", "question"]
    )
    return template

def get_retrieval_template(system_message: str):
    prompt_template = f"""{system_message}
---
{{context}}
---
{{chat_history}}
User: {{question}}
Assistant: """
    template = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question", "chat_history"]
    )
    return template