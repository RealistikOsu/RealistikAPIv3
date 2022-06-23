from app.state.config import config
from app.db.sql import Connection

from typing import AsyncIterator
from redis import asyncio as aioredis
import aiomysql

sql_pool: aiomysql.Pool
redis_pool: aioredis.Redis

async def create_sql_pool() -> None:
    global sql_pool
    
    sql_pool = await aiomysql.create_pool(
        user= config.sql_user,
        password= config.sql_password,
        db= config.sql_db,
    )

async def create_redis_pool() -> None:
    global redis_pool
    
    redis_pool = aioredis.from_url(
        config.redis_dsn,
    )

async def get_sql_conn() -> AsyncIterator[Connection]:
    """A FastAPI dependency that manages the lifetime of a MySQL connection."""
    
    async with sql_pool.acquire() as conn:
        yield Connection(conn)

async def get_redis_conn() -> AsyncIterator[aioredis.Redis]:
    """A FastAPI dependency that manages the lifetime of a Redis connection."""
    
    async with redis_pool.client() as conn:
        yield conn
