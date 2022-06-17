from fastapi import FastAPI
from state.config import config

from state.connections import create_sql_pool

def init_routers(app: FastAPI) -> None:
    ...

def init_events(app: FastAPI) -> None:
    @app.on_event("startup")
    async def on_startup() -> None:
        await create_sql_pool()

def init_app() -> FastAPI:
    app = FastAPI(
        title= "RealistikAPI v3",
        description= "The modern API for RealistikOsu!",
        docs_url= "/api/v3/docs",
        openapi_url= "/api/v3/openapi.json",
    )
    
    init_events(app)
    init_routers(app)
    
    return app

fastapi_app = init_app()
