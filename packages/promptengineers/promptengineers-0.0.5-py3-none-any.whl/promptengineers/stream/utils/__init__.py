"""Stream Utils"""
from typing import Awaitable
import asyncio
import ujson
# import openai

from promptengineers.core.utils import logger


async def wrap_done(fn_name: Awaitable, event: asyncio.Event):
    """Wrap an awaitable with a event to signal when it's done or an exception is raised."""
    try:
        await fn_name
    except asyncio.CancelledError:
        pass
    # except openai.APIError as error:
    #     print(f"Caught API error: {error}")
    finally:
        # Signal the aiter to stop.
        event.set()

def token_stream(token: str or dict = None, action_type: str = None):
    """ Use server-sent-events to stream the response"""
    if not token and not action_type:
        data = {
            'sender': 'assistant',
            'message': "",
            'type': 'end'
        }
        logger.debug('[utils.stream.token_stream] End: %s', str(data))
    elif action_type == 'tool':
        data = {
            'sender': 'assistant',
            'message': token,
            'type': 'tool'
        }
        logger.debug('[utils.stream.token_stream] Action: %s', str(data))
    elif action_type == 'doc':
        data = {
            'sender': 'assistant',
            'message': token,
            'type': 'doc'
        }
        logger.debug('[utils.stream.token_stream] Document: %s', str(data))
    elif action_type == 'log':
        data = {
            'sender': 'assistant',
            'message': token,
            'type': 'log'
        }
        logger.debug('[utils.stream.token_stream] Log: %s', str(data))
    else:
        data = {
            'sender': 'assistant',
            'message': token,
            'type': 'stream'
        }
        logger.debug('[utils.stream.token_stream] Token: %s', str(data))
    return f"data: {ujson.dumps(data)}\n\n"