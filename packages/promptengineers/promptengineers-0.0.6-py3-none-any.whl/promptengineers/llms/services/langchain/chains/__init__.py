"""Chain Service"""
from langchain.agents import AgentExecutor, OpenAIFunctionsAgent
from langchain.agents.openai_functions_agent.agent_token_buffer_memory import AgentTokenBufferMemory
from langchain.callbacks.base import BaseCallbackHandler
from langchain.chains import (
    ConversationChain,
	ConversationalRetrievalChain,
	LLMChain
)
from langchain.memory import ConversationBufferMemory, ConversationSummaryBufferMemory
from langchain.prompts import MessagesPlaceholder
from langchain.schema import SystemMessage
from langchain.chains.chat_vector_db.prompts import QA_PROMPT
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    HumanMessagePromptTemplate,
)
from promptengineers.core.config import APP_ENV
from promptengineers.prompts.templates import get_system_template, get_retrieval_template


def _handle_error(error) -> str:
    return str(error)[:500]

class ChainService:
	"""Chain Service"""
	def __init__(self, model):
		self.model = model

	#########################################################
	## Conversation
	#########################################################
	def conversation(self):
		prompt_template = ChatPromptTemplate.from_messages(
			[
				MessagesPlaceholder(variable_name="context"),
				HumanMessagePromptTemplate.from_template("{input}")
			]
		)
		memory = ConversationBufferMemory(return_messages=True, memory_key="context")
		llm_chain = ConversationChain(llm=self.model, prompt=prompt_template, memory=memory, verbose=False)

		return llm_chain

	#########################################################
	## Question Answering
	#########################################################
	def condense_question(self, system_message):
		"""Condense a question into a single sentence."""
		return LLMChain(
			llm=self.model,
			prompt=get_system_template(system_message),
		)

	def collect_docs(self, system_message):
		"""Collect documents from the vectorstore."""
		return load_qa_chain(
			self.model,
			chain_type='stuff',
			prompt=get_system_template(system_message)
		)
	
	def conversation_retrieval(
		self,
		vectorstore,
		system_message,
		chat_history,
		callbacks = None
	):
		"""Retrieve a conversation."""
		memory = ConversationSummaryBufferMemory(llm=self.model,
												memory_key="chat_history",
												return_messages=True,
												output_key='answer')
		for message in chat_history:
			if message[0] and message[1]:
				memory.chat_memory.add_user_message(message[0])
				memory.chat_memory.add_ai_message(message[1])
			else:
				memory.chat_memory.add_user_message(message[0])
		return ConversationalRetrievalChain.from_llm(
			llm=self.model,
			condense_question_llm=self.model,
			retriever=vectorstore.as_retriever(),
			memory=memory,
			combine_docs_chain_kwargs={"prompt": get_retrieval_template(system_message)},
			return_source_documents=True,
			verbose=True if APP_ENV == 'local' or APP_ENV == 'development' else False,
			callbacks=callbacks or []
		)


	#########################################################
	## Agent
	#########################################################
	def create_executor(
		self,
		content,
		tools,
		chat_history,
		verbose=True if APP_ENV == 'local' or APP_ENV == 'development' else False,
		return_messages = True,
		callbacks = [],
		return_intermediate_steps = True,
		handle_parsing_errors = True
	):
		system_message = SystemMessage(content=content)
		prompt = OpenAIFunctionsAgent.create_prompt(
			system_message=system_message,
			extra_prompt_messages=[MessagesPlaceholder(variable_name="chat_history")]
		)
		memory = AgentTokenBufferMemory(memory_key="chat_history", 
								  		llm=self.model, 
										return_messages=return_messages)
		if len(chat_history) > 0:
			for message in chat_history:
				if message[0] and message[1]:
					memory.chat_memory.add_user_message(message[0])
					memory.chat_memory.add_ai_message(message[1])
				else:
					memory.chat_memory.add_user_message(message[0])
		agent = OpenAIFunctionsAgent(llm=self.model, tools=tools, prompt=prompt)
		return AgentExecutor(
			agent=agent,
			tools=tools,
			memory=memory,
			verbose=verbose,
			callbacks=callbacks,
			return_intermediate_steps=return_intermediate_steps,
			handle_parsing_errors=handle_parsing_errors
		)

	def agent_with_tools(
			self,
			system_message: str,
			chat_history,
			tools,
			callbacks: list[BaseCallbackHandler] = None
		):
		"""Agent with tools."""
		agent_executor = self.create_executor(system_message, tools, chat_history, callbacks=callbacks)
		return agent_executor