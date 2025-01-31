"""
This module is designed for reading data and calculating the number of tokens
required to create embeddings.
"""
from llama_index.core.llms import MockLLM
from llama_index.core import MockEmbedding
import tools
from index.create_index import create_index
import tiktoken
from llama_index.core.callbacks import CallbackManager, TokenCountingHandler
from llama_index.core import Settings

def run_dry():
    llm = MockLLM(max_tokens=256)
    embed_model = MockEmbedding(embed_dim=1536)


    token_counter = TokenCountingHandler(
        tokenizer=tiktoken.encoding_for_model("gpt-4o-mini").encode
    )

    callback_manager = CallbackManager([token_counter])


    Settings.llm = llm
    Settings.embed_model = embed_model
    Settings.callback_manager = callback_manager

    index = create_index()

    print("===")
    print("For indexing:")
    print(
        "Embedding Tokens: ",
        token_counter.total_embedding_token_count,
        "\n",
        "LLM Prompt Tokens: ",
        token_counter.prompt_llm_token_count,
        "\n",
        "LLM Completion Tokens: ",
        token_counter.completion_llm_token_count,
        "\n",
        "Total LLM Token Count: ",
        token_counter.total_llm_token_count,
        "\n",
    )


    tools.calculate_cost(token_counter.total_embedding_token_count, token_counter.prompt_llm_token_count, token_counter.completion_llm_token_count)

    # reset counts
    token_counter.reset_counts()

    query_engine = index.as_query_engine()

    query = "For mobile apps, what is the best flow?"
    response = query_engine.query(query)

    print("===")
    print(f'For query {query}:')
    print(
        "Embedding Tokens: ",
        token_counter.total_embedding_token_count,
        "\n",
        "LLM Prompt Tokens: ",
        token_counter.prompt_llm_token_count,
        "\n",
        "LLM Completion Tokens: ",
        token_counter.completion_llm_token_count,
        "\n",
        "Total LLM Token Count: ",
        token_counter.total_llm_token_count,
        "\n",
    )

    tools.calculate_cost(token_counter.total_embedding_token_count, token_counter.prompt_llm_token_count, token_counter.completion_llm_token_count)
