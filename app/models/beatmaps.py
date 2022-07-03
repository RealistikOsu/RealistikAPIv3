from pydantic import BaseModel
from app.constants import modes
from app.constants import status

class BeatmapData(BaseModel):
    id: int
    set_id: int
    md5: str
    name: str
    ar: float
    od: float
    mode: modes.Mode
    rating: float
    difficulty: float
    max_combo: int
    hit_length: int
    bpm: float
    passcount: int
    playcount: int
    status: status.RankedStatus
