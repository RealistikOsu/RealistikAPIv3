from typing import Any, Optional

from app.models.beatmaps import BeatmapData
from app.constants import modes, status
from app.db.sql import Connection

def from_row(row: dict[str, Any]) -> BeatmapData:
    mode = modes.Mode(row["mode"])
    return BeatmapData(
        id= row["beatmap_id"],
        set_id= row["beatmapset_id"],
        md5= row["beatmap_md5"],
        name= row["song_name"],
        ar= row["ar"],
        od= row["od"],
        mode= mode,
        rating = row["rating"],
        difficulty= row[f"difficulty_{mode.db_name}"],
        max_combo= row["max_combo"],
        hit_length= row["hit_length"],
        bpm= row["bpm"],
        passcount= row["passcount"],
        playcount= row["playcount"],
        status= status.RankedStatus(row["ranked"]),
    )

async def from_db(beatmap_id: int, conn: Connection) -> Optional[BeatmapData]:
    row = await conn.fetchone(
        "SELECT * FROM beatmaps WHERE beatmap_id = %s",
        (beatmap_id,),
    )
    
    if not row:
        return None
    
    return from_row(row)

async def set_from_db(set_id: int, conn: Connection) -> list[BeatmapData]:
    rows = await conn.fetchall(
        "SELECT * FROM beatmaps WHERE beatmapset_id = %s",
        (set_id,),
    )
    
    return [from_row(row) for row in rows]
