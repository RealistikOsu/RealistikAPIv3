from redis import asyncio as aioredis
from app.constants import modes

from typing import Optional

async def get_rank(
    user_id: int,
    mode: modes.Mode,
    c_mode: modes.CustomMode,
    redis: aioredis.Redis,
) -> Optional[int]:
    """Attempts to fetch a user's rank for a specific mode combo."""
    
    mode_str = mode.db_name
    c_mode_suffix = c_mode.db_suffix
    
    rank_idx = await redis.zrevrank(
        f"ripple:leaderboard{c_mode_suffix}:{mode_str}",
        user_id,
    )
    
    if rank_idx is None:
        return None
    
    return rank_idx + 1

async def get_rank_history(
    user_id: int,
    mode: modes.Mode,
    c_mode: modes.CustomMode,
    redis: aioredis.Redis,
) -> Optional[list[int]]:
    """Fetches a history of the user's ranks stored by the Statistik
    data collector."""
    
    key = f"statistik:rank_graph:{user_id}:{c_mode.short_name}:{mode.db_name}"
    ranks = await redis.lrange(
        key,
        -90,
        90,
    )
    
    return [int(rank) for rank in ranks]
