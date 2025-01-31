EMBEDDING_COST_PER_TOKEN = 0.020 / 1000000
LLM_INPUT_COST_PER_TOKEN = 0.150 / 1000000
LLM_OUTPUT_COST_PER_TOKEN = 0.600 / 1000000

def calculate_cost(embedding_tokens, llm_input_tokens, llm_output_tokens):
    embedding_cost = embedding_tokens * EMBEDDING_COST_PER_TOKEN
    llm_input_cost = llm_input_tokens * LLM_INPUT_COST_PER_TOKEN
    llm_output_cost = llm_output_tokens * LLM_OUTPUT_COST_PER_TOKEN
    print(f"Embedding cost: {embedding_cost:.2f} USD")
    print(f"LLM input cost: {llm_input_cost:.2f} USD")
    print(f"LLM output cost: {llm_output_cost:.2f} USD")
    print(f"Total cost: {embedding_cost + llm_output_cost + llm_input_cost} USD")
