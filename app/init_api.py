from fastapi import FastAPI
from app.state.config import config
from app.state.connections import create_sql_pool
from app.state.connections import create_redis_pool

# Router imports
from app import api

def init_routers(app: FastAPI) -> None:
    app.include_router(api.stats.router)

def init_events(app: FastAPI) -> None:
    @app.on_event("startup")
    async def on_startup() -> None:
        await create_sql_pool()
        await create_redis_pool()

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
