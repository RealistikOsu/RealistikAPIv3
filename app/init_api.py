from fastapi import FastAPI
from state.config import config

def init_events(app: FastAPI) -> None:
    @app.on_event("startup")
    async def on_startup() -> None:
        ...

def init_app() -> FastAPI:
    app = FastAPI(
        title= "RealistikAPI v3",
        description= "The modern API for RealistikOsu!",
        docs_url= "/api/v3/docs",
        openapi_url= "/api/v3/openapi.json",
    )
    
    init_events(app)
    
    return app

fastapi_app = init_app()