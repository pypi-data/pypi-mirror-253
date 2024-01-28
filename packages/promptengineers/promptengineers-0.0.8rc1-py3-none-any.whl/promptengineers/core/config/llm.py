from enum import Enum

class OpenAIModels(Enum):
    GPT_3_5_TURBO = 'gpt-3.5-turbo'
    GPT_3_5_TURBO_16K = 'gpt-3.5-turbo-1106'
    GPT_3_5_TURBO_MARCH = 'gpt-3.5-turbo-0301'
    GPT_4 = 'gpt-4'
    GPT_4_MARCH = 'gpt-4-0314'
    GPT_4_32K = 'gpt-4-32k'
    GPT_4_32K_MARCH = 'gpt-4-32k-0314'
    GPT_4_TURBO = 'gpt-4-0125-preview'
    GPT_4_VISION = 'gpt-4-vision-preview'
    EMBED_ADA = 'text-embedding-ada-002'
    TEXT_EMBED_3_SMALL = 'text-embedding-3-small'
    TEXT_EMBED_3_LARGE = 'text-embedding-3-large'

class OllamaModels(Enum):
    LLAMA_2 = 'llama2'
    LLAMA_2_7B = 'llama2:7b'
    CODE_LLAMA = 'codellama'
    VICUNA = 'vicuna'
    MISTRAL = 'mistral'

ACCEPTED_OPENAI_MODELS = {
    OpenAIModels.GPT_3_5_TURBO.value,
    OpenAIModels.GPT_3_5_TURBO_16K.value,
    OpenAIModels.GPT_4.value,
    OpenAIModels.GPT_4_32K.value,
    OpenAIModels.GPT_4_TURBO.value,
    OpenAIModels.GPT_4_VISION.value,
    OpenAIModels.EMBED_ADA.value,
    OpenAIModels.TEXT_EMBED_3_SMALL.value,
    OpenAIModels.TEXT_EMBED_3_LARGE.value
}

ACCEPTED_OLLAMA_MODELS = {
    OllamaModels.LLAMA_2.value,
    OllamaModels.LLAMA_2_7B.value,
    OllamaModels.CODE_LLAMA.value,
    OllamaModels.VICUNA.value,
    OllamaModels.MISTRAL.value
}

ACCEPTED_EMBEDDING_MODELS = {
    OpenAIModels.EMBED_ADA.value,
    OpenAIModels.TEXT_EMBED_3_SMALL.value,
    OpenAIModels.TEXT_EMBED_3_LARGE.value,
    OllamaModels.LLAMA_2.value,
    OllamaModels.LLAMA_2_7B.value,
}