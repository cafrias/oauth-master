from contextlib import asynccontextmanager

from fastapi import FastAPI
from llama_index.core.base.base_query_engine import BaseQueryEngine
from pydantic import BaseModel
from starlette.datastructures import State

import index
from settings import load_settings

class AppState(State):
    engine: BaseQueryEngine

class MyApp(FastAPI):
    state: AppState

@asynccontextmanager
async def lifespan(a: MyApp):
    load_settings()
    engine = index.get_index().as_query_engine()
    a.state.engine = engine
    yield

app = MyApp(lifespan=lifespan)

class SearchBody(BaseModel):
    prompt: str

@app.post("/search")
async def search(search_body: SearchBody):
    res = await app.state.engine.aquery(search_body.prompt)
    if not res.response:
        return {"error": "Nothing returned from the LLM"}, 500

    return {"message": res.response}
