from app.state.config import config
from app.db.sql import Connection

from typing import AsyncIterator
import aiomysql

sql_pool: aiomysql.Pool

async def create_sql_pool() -> None:
    global sql_pool
    
    sql_pool = await aiomysql.create_pool(
        user= config.sql_user,
        password= config.sql_password,
        db= config.sql_db,
    )

async def get_db_connection() -> AsyncIterator[Connection]:
    """A FastAPI dependency that manages the lifetime of a MySQL connection."""
    
    async with sql_pool.acquire() as conn:
        yield Connection(conn)
