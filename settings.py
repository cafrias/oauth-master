from dotenv import load_dotenv
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.core import Settings

def load_settings():
    """
    Loads configurations and initializes the system with specified settings.

    Sets the global embedding model and LLM.
    """
    load_dotenv()

    embed_model = OpenAIEmbedding(model="text-embedding-3-small")
    Settings.embed_model = embed_model

    llm = OpenAI(
        model="gpt-4o-mini",
    )
    Settings.llm = llm
