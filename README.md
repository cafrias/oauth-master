# Oauth Master

This is my first RAG project, it indexes the OAuth 2.0 spec and some reference material, you can then query this data.

## Scripts

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

## TODO:

- [X] Parse URLs.
- [X] Create and Store Index
- [X] Can make query
- [ ] REST API
- [ ] Logging and tracing
- [ ] Add evals and observability tools
