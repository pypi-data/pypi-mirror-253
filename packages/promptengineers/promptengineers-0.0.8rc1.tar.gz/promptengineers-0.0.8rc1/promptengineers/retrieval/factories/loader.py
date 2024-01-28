import nest_asyncio
from langchain.document_loaders import (CSVLoader, DirectoryLoader, GitbookLoader,
										PyPDFLoader, TextLoader, JSONLoader, RecursiveUrlLoader,
										ReadTheDocsLoader, DataFrameLoader, UnstructuredHTMLLoader, 
										UnstructuredMarkdownLoader,
										UnstructuredURLLoader, WebBaseLoader,
										YoutubeLoader, SitemapLoader, BlockchainDocumentLoader)
from langchain.document_loaders.blockchain import BlockchainType
from promptengineers.core.config import ALCHEMY_API_KEY
from promptengineers.retrieval.loaders import CopyPasteLoader

nest_asyncio.apply()

class LoaderFactory:
    LOADER_CLASSES = {
        'gitbook': GitbookLoader,
        'web_base': WebBaseLoader,
        'website': RecursiveUrlLoader,               # Alias for 'web_base
        'youtube': YoutubeLoader,
        'polygon': BlockchainDocumentLoader,
        'ethereum': BlockchainDocumentLoader,
        'sitemap': SitemapLoader,
        'urls': UnstructuredURLLoader,          # Requires `unstructred` pip package (2.07 GB)
        'copy': CopyPasteLoader,
        'txt': TextLoader,
        'html': UnstructuredHTMLLoader,			# Requires `unstructred` pip package (2.07 GB)
        'md': UnstructuredMarkdownLoader,       # Requires `unstructred` pip package (2.07 GB)
        'directory': DirectoryLoader,           # Requires `unstructred` pip package (2.07 GB)
        'csv': CSVLoader,
        'pdf': PyPDFLoader,
        'json': JSONLoader,
        'pandas': DataFrameLoader,              # Requires `pandas`
        'readthedocs': ReadTheDocsLoader,       # Requires `beautifulsoup4`
    }

    @staticmethod
    def create(
        loader_type: ('gitbook', 'web_base', 'website', 'youtube', 'polygon', 'ethereum', 'sitemap', 'urls', 'copy', 'txt', 'html', 'md', 'directory', 'csv', 'pdf', 'json', 'pandas', 'readthedocs'), 
        loader_config
    ):
        loader_class = LoaderFactory.LOADER_CLASSES.get(loader_type)
        if not loader_class:
            raise ValueError(f'Unsupported document loader type: {loader_type}')

        # Special handling for blockchain loaders
        if loader_type in {'polygon', 'ethereum'}:
            blockchain_type = BlockchainType.POLYGON_MAINNET if loader_type == 'polygon' else None
            return loader_class(
                contract_address=loader_config.get('contract_address', ''),
                blockchainType=blockchain_type,
                api_key=ALCHEMY_API_KEY
            )

        # Special handling for the 'copy' loader
        if loader_type == 'copy':
            return loader_class(text=loader_config.get('text'))

        if loader_type == 'pandas':
            return loader_class(loader_config.get('df'), 
                                page_content_column=loader_config.get('page_content_column'))
        
        if loader_type == 'readthedocs':
            return loader_class(path=loader_config.get('path'), features='html.parser')
        
        if loader_type == 'gitbook':
            urls = loader_config.get('urls', [])
            return loader_class(urls=urls[0], load_all_paths=True)

        # Handling for loaders that require URLs or file paths
        if loader_type in {'web_base', 'sitemap', 'website', 'urls'}:
            urls = loader_config.get('urls', [])
            return loader_class(urls[0])

        if loader_type == 'youtube':
            urls = loader_config.get('urls', [])
            return loader_class.from_youtube_url(urls[0], add_video_info=False)
        
        if loader_type == 'json':
            return loader_class(file_path=loader_config.get('file_path'),
                                jq_schema=loader_config.get('jq_schema'),
                                text_content=loader_config.get('text_content'),
                                json_lines=loader_config.get('json_lines'))

        # Handling for file-based loaders
        return loader_class(loader_config.get('file_path'))
