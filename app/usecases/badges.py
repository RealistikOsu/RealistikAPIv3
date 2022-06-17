from app.models.user import PlayerBadgeData
from app.db.sql import Connection

from typing import Optional, Any

async def from_db(badge_id: int, conn: Connection) -> Optional[PlayerBadgeData]:
    """Get basic player badge data from the MySQL Database."""

    badge_db = await conn.fetchone(
        "SELECT id, name, icon FROM badges WHERE id = %s",
        (badge_id,),
    )

    if badge_db:
        return from_row(badge_db)
    return None

def from_row(row: dict[str, Any]) -> PlayerBadgeData:
    """Creates a PlayerBadgeData object from a row from the MySQL Database."""

    return PlayerBadgeData(
        **row
    )
