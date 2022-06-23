from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from redis import asyncio as aioredis

from app.state import connections
from app.constants import modes
from app.usecases import ranks

router = APIRouter(
    prefix="/api/v3/stats",
)

@router.get("/graph")
async def rank_graph_get(
    user_id: int,
    mode: modes.Mode,
    c_mode: modes.CustomMode,
    redis: aioredis.Redis = Depends(connections.get_redis_conn),
) -> JSONResponse:
    """An endpoint displaying the user's rank history over 24hr intervals."""
    
    cur_rank = await ranks.get_rank(
        user_id,
        mode,
        c_mode,
        redis,
    )
    
    history = await ranks.get_rank_history(
        user_id,
        mode,
        c_mode,
        redis,
    )
    
    if not (cur_rank and history):
        raise HTTPException(
            403,
            "No rank history stored for user.",
        )
        
    # Add the current rank to the history.
    history.append(cur_rank)
    
    return JSONResponse({
        "status": 200,
        "graph": history,
    })
