from langchain_groq import ChatGroq
from tavily import TavilyClient
from functools import lru_cache
from dotenv import load_dotenv
load_dotenv()


LLM_MODEL = "openai/gpt-oss-120b"
TEMPERATURE = 0

@lru_cache(maxsize=1)
def get_llm():
    """
    Initializes and returns a cached LLM instance.

    Returns:
        ChatGroq: Configured LLM instance.
    """
    return ChatGroq(model=LLM_MODEL, temperature=TEMPERATURE)


@lru_cache(maxsize=1)
def get_search_tool():
    """
    Initializes and returns a cached Tavily client.

    Returns:
        TavilyClient: Configured Tavily search client.
    """
    return TavilyClient()
