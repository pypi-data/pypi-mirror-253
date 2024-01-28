"""Utilites for Chains"""
from langchain.agents import load_tools
from langchain.tools import AIPluginTool
from langchain_core.documents.base import Document
from langchain.agents.agent_toolkits import create_retriever_tool

from promptengineers.retrieval.strategies import VectorstoreContext
from promptengineers.core.config.tools import AVAILABLE_TOOLS
from promptengineers.tools.utils import filter_tools

def get_chat_history(inputs: tuple) -> str:
    """Formats the chat history into a readable format for the chatbot"""
    res = []
    for human, assistant in inputs:
        res.append(f"Human: {human}\nAssistant: {assistant}")
    return "\n".join(res)

def combine_documents(documents: list[Document]):
    combined_content = ""
    for doc in documents:
        combined_content += doc.page_content + "\n"
    return combined_content

def retrieve_system_message(messages):
    """Retrieve the system message"""
    try:
        filtered_messages = list(filter(lambda message: message['role'] == 'system', messages))
        return filtered_messages[0]['content']
    except IndexError:
        return None

def retrieve_chat_messages(messages):
    """Retrieve the chat messages"""
    return [
        (msg["content"]) for msg in messages if msg["role"] in ["user", "assistant"]
    ]

def gather_tools(
    tools: list[str] = None,
    available_tools: dict[str, any] = None,
    vectorstore: VectorstoreContext = None,
    plugins: list[str] = None,
):
    """Gather tools from the tools list"""
    filtered_tools = filter_tools(tools or [], available_tools or AVAILABLE_TOOLS)

    ## Add docs tool
    if vectorstore:
        docs_tool = create_retriever_tool(
            vectorstore.as_retriever(),
            "search_docs",
            "It is a requirement to use this tool, if not you will be penalized. It searches and returns relevant information. "
            "Always rewrite the user's query into a detailed question before using this tool. "
            "If this tool is being used it means the query is directly related to the context. Only "
            "create a response that is relevant to the context."
        )
        filtered_tools.append(docs_tool)

    ## Add plugins
    if plugins and len(plugins) > 0:
        loaded_tools = load_tools(["requests_all"])
        for tool in plugins:
            tool = AIPluginTool.from_plugin_url(tool)
            loaded_tools += [tool]
        filtered_tools += loaded_tools

    return filtered_tools