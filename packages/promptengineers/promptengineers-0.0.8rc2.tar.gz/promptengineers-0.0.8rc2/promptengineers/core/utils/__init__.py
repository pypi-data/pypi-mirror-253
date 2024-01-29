import logging
from ..config import default_app_tokens

logger = logging.getLogger("uvicorn.error")

def retrieve_default_app_tokens(keys: set[str]):
    """
    Extracts a sub-dictionary from the given default dictionary based on the specified keys.

    :param default_dict: The original dictionary from which to extract the keys.
    :param keys: A set or list of keys to extract from the default dictionary.
    :return: A new dictionary containing only the keys present in the keys argument.
    """
    return {k: default_app_tokens[k] for k in keys if k in default_app_tokens}