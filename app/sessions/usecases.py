from .session import UserSession
from app.db.sql import Connection

from typing import (
    Optional,
    TypedDict,
)
import string
import random
import time

TOKEN_CHARS = string.ascii_letters + string.digits

class SessionRedis(TypedDict):
    user_id: int
    expiry: int
    
def generate_random_token() -> str:
    """Generates a random token of 128 characters to identify sessions."""
    
    return "".join(random.choice(TOKEN_CHARS) for _ in range(128))

def get_session_end_time() -> int:
    """Generates a timestamp at which a session created now should end."""
    
    # 1 day expiration period.
    return int(time.time()) + 86400

def create_session_dict(user_id: int) -> SessionRedis:
    return {
        "user_id": user_id,
        "expiry": get_session_end_time(),
    }

async def session_from_id(
    user_id: int,
    expity_ts: int,
    conn: Connection,
) -> Optional[UserSession]:
    """Creates a session object from a user ID and session expiry."""

    # Fetch data from db.
    user_data_db = await conn.fetchone(
        "SELECT username, privileges FROM users WHERE id = %s",
        (user_id,),
    )
    
    if not user_data_db:
        return None
    
    return UserSession(
        id= user_id,
        name= user_data_db["username"],
        privileges= user_data_db["privileges"],
        expiry= expity_ts,
    )
