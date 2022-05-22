from pydantic import BaseModel, Field
from .user import PlayerCardData

class TopPlayData(BaseModel):
    """Data for a top play."""

    beatmap_id: int
    pp: float
    user: PlayerCardData
    mode: int = Field(..., ge= 0, le= 3)
    c_mode: int = Field(..., ge= 0, le= 2)
