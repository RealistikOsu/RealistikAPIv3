from fastapi import FastAPI
from state.config import config

app = FastAPI(
    title= "RealistikAPI v3",
    description= "The modern API for RealistikOsu!",
    docs_url= "/api/v3/docs",
    openapi_url= "/api/v3/openapi.json",
)
