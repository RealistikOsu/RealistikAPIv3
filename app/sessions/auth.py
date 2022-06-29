from app.db.sql import Connection

from typing import Optional
import bcrypt

async def get_user_password_bcrypt(
    user_id: int,
    conn: Connection,
) -> Optional[str]:
    """Attempts to fetch a player password bcrypt hash from the database."""

    return await conn.fetchcol(
        "SELECT password_md5 FROM users WHERE id = %s",
        (user_id,),
    )

async def compare_user_password_bcrypt(
    user_id: int,
    password: str,
    conn: Connection,
) -> bool:
    """Attempts to compare a player password bcrypt hash with the given password."""

    password_hash = await get_user_password_bcrypt(user_id, conn)

    if not password_hash:
        return False

    return bcrypt.checkpw(password.encode(), password_hash.encode())