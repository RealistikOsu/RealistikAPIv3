from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException

from app.state import connections
from app.models.beatmaps import BeatmapData
from app.db.sql import Connection
from app.usecases import beatmaps

router = APIRouter(
    prefix="/api/v3/beatmaps",
)

@router.get("/beatmap/{beatmap_id}", response_model= BeatmapData)
async def beatmap_get(
    beatmap_id: int,
    conn: Connection = Depends(connections.get_sql_conn)
) -> BeatmapData:
    """An endpoint displaying the beatmap data for a given beatmap ID."""
    beatmap = await beatmaps.from_db(beatmap_id, conn)
    if not beatmap:
        raise HTTPException(
            404,
            "Beatmap not found.",
        )
    return beatmap

@router.get("/set/{set_id}", response_model= list[BeatmapData])
async def set_get(
    set_id: int,
    conn: Connection = Depends(connections.get_sql_conn)
) -> list[BeatmapData]:
    
    return await beatmaps.set_from_db(set_id, conn)
