# Oauth Master

This is my first RAG project, it indexes the OAuth 2.0 spec and some reference material, you can then query this data.

## Scripts

API is implemented using FastAPI:
```bash
# Start the dev server
fastapi dev main.py
```

Handy scripts for quick checks:
```bash
# Run a cost calculation for the indexing and a demo query
python run_dry.py

# Creates the index and saves it
python create_index.py

# It prompts you to write a query, them submits this query to OpenAI
# and returns the response.
python run_query.py
```

## Tech Stack:

- LlamaIndex
- Decoder Model: 4o-mini
- Embedding Model: text-embedding-3-small
- FastAPI

## TODO:

- [X] Parse URLs.
- [X] Create and Store Index
- [X] Can make query
- [X] REST API
- [X] Logging and tracing
- [ ] Generate test questions for the data
- [ ] Add retrieval evaluation
- [ ] Add Relevancy Evaluator
- [ ] Add Faithfulness Evaluator
- [ ] Combine metrics with Opik + Comet ML experiments
- [ ] Use custom prompts
