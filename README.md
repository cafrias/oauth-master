# Oauth Master

This is my first RAG project, it indexes the OAuth 2.0 spec and some reference material, you can then query this data.

## Scripts

```bash
# Run a cost calculation for the indexing and a demo query
python run_dry.py
```

## Tech Stack:

- LlamaIndex
- Decoder Model: 4o-mini
- Embedding Model: text-embedding-3-small

## TODO:

- [X] Parse URLs.
- [X] Create and Store Index
- [ ] Can make query
- [ ] REST API
