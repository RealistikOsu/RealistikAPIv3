from app.models.user import ClanData
from app.db.sql import Connection

from typing import Optional, Any

async def get_data_db(clan_id: int, conn: Connection) -> Optional[ClanData]:
    """Get basic clan data from the MySQL Database.."""

    clan_db = await conn.fetchone(
        "SELECT id, tag, name, icon AS icon_url FROM clans WHERE id = %s",
        (clan_id,),
    )
    
    if clan_db:
        return get_data_from_row(clan_db)
    return None
    
def get_data_from_row(row: dict[str, Any]) -> ClanData:
    """Creates a ClanData object from a row from the MySQL Database."""

    return ClanData(
        **row
    )
