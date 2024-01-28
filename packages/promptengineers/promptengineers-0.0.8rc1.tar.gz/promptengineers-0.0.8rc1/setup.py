import os
from setuptools import setup, find_packages

VERSION = os.environ.get('VERSION', '0.0.1') 

setup(
    name='promptengineers',
    version=VERSION,
    packages=find_packages(exclude=["tests*", ".github*", "scripts*"]),
    install_requires=[
        'ujson',
    ],
    extras_require={
        'llms':[
            'langchain==0.0.354',
            'langchain-openai', 
            'openai', 
        ],
        'mongo': [
            'motor', 
            'pymongo', 
            'cryptography',
        ],
        'prompts':[
            'promptengineers[llms]',
        ],
        'storage': [
            'minio', 
            'python-multipart',
        ],
        'retrieval': [
            'jq',
            'promptengineers[llms]',
            'redis', 
            'pinecone-client==2.2.4', 
            'youtube-transcript-api', 
            'pypdf', 
            'numexpr', 
            'tiktoken', 
            'nest_asyncio', 
            'beautifulsoup4',
            # 'unstructured[all-docs]'
        ],
        'tools': [
            'promptengineers[llms]',
        ],
        'fastapi': [
            'fastapi',
            'uvicorn',
            ## History
            'promptengineers[mongo]',
            ## Storage
            'promptengineers[storage]',
            ## Chat
            'promptengineers[retrieval]',
        ],
    },
    author='Ryan Eggleston',
    author_email='kre8mymedia@gmail.com',
    description='A collection of utilities by Prompt Engineers',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/promptengineers-ai/core',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
