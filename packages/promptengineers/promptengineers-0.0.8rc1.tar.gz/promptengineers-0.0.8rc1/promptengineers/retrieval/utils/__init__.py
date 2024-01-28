import requests
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup
from langchain.callbacks import get_openai_callback
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS

from promptengineers.core.utils import logger

def get_links(url: str):
	response = requests.get(url, timeout=5)
	soup = BeautifulSoup(response.text, 'html.parser')
	links = []
	for link in soup.find_all('a'):
		href = link.get('href')
		if href and urlparse(href).netloc == '':
			links.append(urljoin(url, href))
	return links

def split_docs(
    documents,
    chunk_size: int = 1000,
    chunk_overlap: int = 100,
    recursive: bool = True,
):
    ## Text Spliter
    if recursive:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
    else:
        text_splitter = CharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
    docs = text_splitter.split_documents(documents)
    return docs

def create_faiss_vectorstore(
    docs,
    chunk_size: int = 1000,
    chunk_overlap: int = 0
):
    """Load the vectorstore."""
    with get_openai_callback() as callback:
        logger.info('[utils.retrieval.create_vectorstore] Tokens: %s', callback.total_tokens)
        embeddings = OpenAIEmbeddings(max_retries=2)
        return FAISS.from_documents(
            split_docs(docs, chunk_size, chunk_overlap),
            embeddings
        )
